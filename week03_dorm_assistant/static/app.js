'use strict';

const STORAGE_KEY = 'move-in-ready.progress.v1';
const VALID_STATES = new Set(['ready', 'missing', 'unknown']);
const VALID_PROFILES = new Set(['standard', 'international', 'unknown']);
const STATE_LABELS = { ready: '已准备', missing: '待准备', unknown: '待确认' };
const PROFILE_LABELS = { standard: '已确认按一般入住说明办理', international: '留学生（文件要求待确认）', unknown: '暂未确认适用身份' };
const CATEGORY_LABELS = { document: '材料与证明', step: '办理与确认', supply: '生活用品', rule: '规则与注意事项' };
const CATEGORY_ORDER = ['document', 'step', 'supply', 'rule'];
const STATUS_LABELS = { ready: '已准备 · 仍需审核', missing: '待准备', unknown: '待确认', confirm: '确认适用要求', invalid_date: '日期需处理', reference: '参考说明' };
const PROFILE_HELP = {
  standard: '适用于你已向学校确认按一般入住说明办理的情况。',
  international: '资料中的文件要求可能因留学生流程而不同；先向办公室确认，不直接套用。',
  unknown: '先整理共同准备事项；证明与办理要求需确认适用身份。',
};

const $ = (id) => document.getElementById(id);
let catalog = null;
let health = { ai_configured: false };
let progress = { profile: 'unknown', move_in_date: '', states: {}, dates: {}, preparation_text: '' };
let filter = 'all';
let report = null;
let suggestions = [];
let toastTimer = null;
let saveTimer = null;
let booting = false;
let formRevision = 0;
let sessionEpoch = 0;

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== null) node.textContent = String(text);
  return node;
}

function safeUrl(value) {
  if (typeof value !== 'string') return null;
  try {
    const url = new URL(value);
    return url.protocol === 'https:' || url.protocol === 'http:' ? url.href : null;
  } catch (_) { return null; }
}

function externalLink(label, value) {
  const url = safeUrl(value);
  if (!url) return element('span', '', label);
  const link = element('a', '', label);
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  link.setAttribute('aria-label', `${label}（新标签页打开）`);
  return link;
}

function stringValue(value) {
  if (typeof value === 'string') return value;
  if (value && typeof value === 'object') return value.message || value.text || value.notice || '';
  return '';
}

function announce(message, error = false) {
  const node = $('live-message');
  clearTimeout(toastTimer);
  node.textContent = message;
  node.classList.toggle('error', error);
  node.hidden = false;
  toastTimer = setTimeout(() => { node.hidden = true; }, error ? 8500 : 4000);
}

async function request(path, payload) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 65000);
  try {
    const options = { signal: controller.signal, headers: { Accept: 'application/json' } };
    if (payload !== undefined) {
      options.method = 'POST';
      options.headers['Content-Type'] = 'application/json';
      options.body = JSON.stringify(payload);
    }
    const response = await fetch(path, options);
    let result;
    try { result = await response.json(); } catch (_) { throw new Error('服务未返回有效结果，请检查本地服务后重试。'); }
    if (!response.ok) throw new Error(stringValue(result?.message) || stringValue(result?.error) || '请求未完成，请稍后重试。');
    return result;
  } catch (error) {
    if (error.name === 'AbortError') throw new Error('请求超时，已保留输入。请稍后重试。');
    throw error;
  } finally { clearTimeout(timeout); }
}

function checkableItems() { return (catalog?.items || []).filter(item => item.checkable === true); }
function itemById(id) { return catalog?.items.find(item => item.id === id); }
function sourceById(id) { return catalog?.sources.find(source => source.id === id); }
function stateOf(id) { return VALID_STATES.has(progress.states[id]) ? progress.states[id] : 'unknown'; }
function isDate(value) { return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value); }

function readSaved() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    const saved = JSON.parse(raw);
    if (!saved || typeof saved !== 'object') return;
    progress.profile = VALID_PROFILES.has(saved.profile) ? saved.profile : 'unknown';
    progress.move_in_date = isDate(saved.move_in_date) ? saved.move_in_date : '';
    // Free text is intentionally never restored or persisted.
    checkableItems().forEach(item => {
      progress.states[item.id] = VALID_STATES.has(saved.states?.[item.id]) ? saved.states[item.id] : 'unknown';
      if (item.date_field && isDate(saved.dates?.[item.id])) progress.dates[item.id] = saved.dates[item.id];
    });
    // Rewrite old records too, removing any fields outside the allowlist.
    saveProgress();
    $('save-status').textContent = '已恢复流程、日期与逐项状态';
  } catch (_) {
    $('save-status').textContent = '无法读取本地记录，当前仍可核对';
  }
}

function saveProgress(explicit = false) {
  clearTimeout(saveTimer);
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ profile: progress.profile, move_in_date: progress.move_in_date, states: progress.states, dates: progress.dates, saved_at: new Date().toISOString(), catalog_version: catalog?.schema_version }));
    $('save-status').textContent = '已保存 · 仅在本浏览器';
    if (explicit) announce('准备进度已保存在本浏览器。');
  } catch (_) {
    $('save-status').textContent = '本地保存不可用，请导出行动清单';
    if (explicit) announce('浏览器未允许保存。表单仍保留在当前页面，可生成并导出行动清单。', true);
  }
}

function changed({ invalidateSuggestions = false } = {}) {
  formRevision += 1;
  if (report) $('report-stale').hidden = false;
  if (invalidateSuggestions) clearSuggestions();
  $('save-status').textContent = '正在保存…';
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => saveProgress(), 250);
  renderProgress();
}

function renderHealth() {
  const configured = health.ai_configured === true;
  $('mode-indicator').classList.toggle('configured', configured);
  $('mode-text').textContent = configured ? '手动可用 · AI已配置' : '手动检查可用';
  $('interpret-button').disabled = !configured || !catalog;
  $('ask-button').disabled = !configured || !catalog;
  $('interpret-mode').textContent = configured ? '点击后将文字发送给AI；文字不写入本地进度。建议经你确认后应用，请勿填写证件号码。' : 'AI尚未配置。你仍可逐项手动标记并生成行动清单。';
  $('ask-mode').textContent = configured ? 'AI已配置。以实际返回为准，回答会附资料依据。' : '规则问答需要AI配置。现在可直接查看各项原文与资料来源。';
}

function makeEvidence(item, overrideSource) {
  const source = overrideSource || sourceById(item.source_id) || {};
  const details = element('details', 'item-evidence');
  details.append(element('summary', '', '查看依据原文'));
  const content = element('div', 'evidence-content');
  const title = source.title || '官方资料';
  content.append(element('p', 'source-meta', `${title}${item.verified_date || source.verified_date ? ' · 核对 ' + (item.verified_date || source.verified_date) : ''}`));
  if (item.source_locator) content.append(element('p', 'source-meta', '原文位置：' + item.source_locator));
  if (item.quote) content.append(element('blockquote', '', item.quote));
  if (item.conditions?.notes_zh) content.append(element('p', '', item.conditions.notes_zh));
  content.append(externalLink('打开官方来源 ↗', item.source_url || source.url));
  if (Array.isArray(item.additional_evidence)) {
    item.additional_evidence.forEach(entry => {
      const extraSource = sourceById(entry.source_id) || {};
      content.append(element('p', 'source-meta', '补充依据：' + (extraSource.title || entry.source_id || '官方资料')));
      if (entry.source_locator) content.append(element('p', 'source-meta', '原文位置：' + entry.source_locator));
      if (entry.quote) content.append(element('blockquote', '', entry.quote));
      content.append(externalLink('打开补充来源 ↗', entry.source_url || extraSource.url));
    });
  }
  details.append(content);
  return details;
}

function renderItem(item) {
  const article = element('article', 'check-item');
  article.dataset.itemId = item.id;
  const top = element('div', 'item-top');
  const copy = element('div', 'item-copy');
  const title = element('h3', '', item.title_zh || item.id);
  title.id = 'title-' + item.id;
  copy.append(title);
  if (item.description_zh) copy.append(element('p', 'item-description', item.description_zh));
  top.append(copy);
  const scope = item.applicability?.[progress.profile];
  let tag = item.checkable ? (item.requirement === 'recommended' ? '建议准备' : item.requirement === 'prohibited' ? '禁止事项' : '需核对') : '资料说明';
  if (scope === 'confirmation_required') tag = '适用要求待确认';
  if (scope === 'reference') tag = '参考 · 请确认适用';
  top.append(element('span', 'item-tag' + ((scope === 'confirmation_required' || scope === 'reference') ? ' conditional' : ''), tag));
  article.append(top);
  if (item.checkable === true) {
    const controls = element('div', 'item-controls');
    const fieldset = element('fieldset', 'status-choice');
    fieldset.append(element('legend', '', (item.title_zh || item.id) + '的准备状态'));
    const labels = item.requirement === 'prohibited' ? { ready: '已核对', missing: '需处理', unknown: '待确认' } : STATE_LABELS;
    for (const state of ['ready', 'missing', 'unknown']) {
      const label = element('label', 'status-option');
      const input = element('input');
      input.type = 'radio'; input.name = 'state-' + item.id; input.value = state;
      input.checked = stateOf(item.id) === state;
      input.addEventListener('change', () => {
        progress.states[item.id] = state;
        changed({ invalidateSuggestions: true });
        if (filter !== 'all') renderChecklist();
      });
      label.append(input, element('span', '', labels[state]));
      fieldset.append(label);
    }
    controls.append(fieldset);
    if (item.date_field === true) {
      const dateWrap = element('div', 'item-date');
      const label = element('label', '', '证明日期');
      label.htmlFor = 'date-' + item.id;
      const input = element('input');
      input.type = 'date'; input.id = 'date-' + item.id;
      input.setAttribute('aria-label', (item.title_zh || item.id) + '的证明日期');
      input.value = progress.dates[item.id] || '';
      input.addEventListener('change', () => {
        if (input.value) progress.dates[item.id] = input.value;
        else delete progress.dates[item.id];
        changed();
      });
      dateWrap.append(label, input); controls.append(dateWrap);
    }
    article.append(controls);
  }
  article.append(makeEvidence(item));
  return article;
}

function renderChecklist() {
  if (!catalog) return;
  const list = $('checklist'); list.replaceChildren();
  const items = catalog.items.filter(item => filter === 'all' || (item.checkable && stateOf(item.id) === filter));
  if (!items.length) {
    list.append(element('p', 'empty-note', `当前没有标记为“${STATE_LABELS[filter] || '符合条件'}”的事项。`));
  } else {
    const knownCategories = [...CATEGORY_ORDER, ...new Set(items.map(item => item.category).filter(c => !CATEGORY_ORDER.includes(c)))];
    knownCategories.forEach(category => {
      const group = items.filter(item => item.category === category);
      if (!group.length) return;
      list.append(element('h3', 'item-group-title', `${CATEGORY_LABELS[category] || '其他事项'} · ${group.length}`));
      group.forEach(item => list.append(renderItem(item)));
    });
  }
  $('profile-help').textContent = PROFILE_HELP[progress.profile];
  $('item-count').textContent = `${checkableItems().length}项可核对 · ${catalog.items.length - checkableItems().length}项参考`;
  renderProgress();
}

function renderProgress() {
  const items = checkableItems();
  const counts = { ready: 0, missing: 0, unknown: 0 };
  items.forEach(item => { counts[stateOf(item.id)] += 1; });
  const percent = items.length ? Math.round(counts.ready / items.length * 100) : 0;
  $('progress-count').textContent = `${counts.ready} / ${items.length}`;
  $('progress-label').textContent = '自报已准备 / 可核对事项';
  $('progress-fill').style.width = percent + '%';
  $('progress-bar').setAttribute('aria-valuenow', String(percent));
  $('progress-bar').setAttribute('aria-valuetext', `${items.length}项可核对事项中，${counts.ready}项标记已准备；不代表已通过审核。`);
  Object.keys(counts).forEach(state => { $(state + '-count').textContent = STATE_LABELS[state] + ' ' + counts[state]; });
}

function renderSources() {
  const list = $('source-list'); list.replaceChildren();
  catalog.sources.forEach(source => {
    const article = element('article', 'source-entry');
    article.append(element('h3', '', source.title || source.id));
    if (source.scope) article.append(element('p', '', source.scope));
    article.append(element('p', '', `资料核对：${source.verified_date || catalog.verified_date || '未注明'}`));
    article.append(externalLink('查看原始资料 ↗', source.url));
    const referenced = catalog.items.flatMap(item => {
      const entries = item.source_id === source.id && item.quote ? [{ title: item.title_zh || item.id, quote: item.quote, locator: item.source_locator }] : [];
      (Array.isArray(item.additional_evidence) ? item.additional_evidence : []).forEach(entry => {
        if (entry.source_id === source.id && entry.quote) entries.push({ title: (item.title_zh || item.id) + ' · 补充依据', quote: entry.quote, locator: entry.source_locator });
      });
      return entries;
    });
    if (referenced.length) {
      const details = element('details', 'item-evidence');
      details.append(element('summary', '', `展开收录的 ${referenced.length} 段原文`));
      referenced.forEach(entry => {
        details.append(element('p', 'source-meta', entry.title));
        if (entry.locator) details.append(element('p', 'source-meta', '原文位置：' + entry.locator));
        details.append(element('blockquote', '', entry.quote));
      });
      article.append(details);
    }
    list.append(article);
  });
  $('verified-note').textContent = `资料核对日期 ${catalog.verified_date || '未注明'} · ${catalog.sources.length}份来源 · 查看原文可追溯`;
  if (catalog.disclaimer_zh) $('sources-description').textContent = catalog.disclaimer_zh;
}

function clearSuggestions() {
  suggestions = [];
  $('suggestions-panel').hidden = true;
  $('suggestion-list').replaceChildren();
}

function renderSuggestions() {
  const list = $('suggestion-list'); list.replaceChildren();
  suggestions.forEach((suggestion, index) => {
    const item = itemById(suggestion.item_id);
    const row = element('div', 'suggestion-row');
    const input = element('input');
    input.type = 'checkbox'; input.id = 'suggestion-' + index; input.checked = true;
    input.dataset.suggestionIndex = String(index);
    input.addEventListener('change', updateSuggestionButton);
    const label = element('label', '', item.title_zh || item.id);
    label.htmlFor = input.id;
    label.append(element('span', 'suggestion-change', `当前：${STATE_LABELS[stateOf(item.id)]} → 建议：${STATE_LABELS[suggestion.state]}`));
    if (suggestion.reason) label.append(element('small', '', suggestion.reason));
    row.append(input, label); list.append(row);
  });
  $('suggestions-panel').hidden = !suggestions.length;
  updateSuggestionButton();
}

function updateSuggestionButton() {
  const count = $('suggestion-list').querySelectorAll('input:checked').length;
  $('apply-suggestions').textContent = `确认并应用 ${count} 条建议`;
  $('apply-suggestions').disabled = count === 0;
}

async function interpret() {
  const text = $('preparation-text').value.trim();
  if (!text) { $('preparation-text').focus(); announce('先描述你的准备情况。'); return; }
  const button = $('interpret-button');
  const profile = progress.profile;
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = '正在整理…';
  clearSuggestions(); $('interpret-notices').hidden = true;
  try {
    const result = await request('/api/interpret', { text, profile });
    if (epoch !== sessionEpoch) return;
    if (text !== $('preparation-text').value.trim() || profile !== progress.profile) {
      announce('输入或入住流程已变化，请重新整理，避免应用旧建议。'); return;
    }
    const notices = Array.isArray(result.notices) ? result.notices.map(stringValue).filter(Boolean) : [stringValue(result.notices)].filter(Boolean);
    const valid = Array.isArray(result.suggestions) ? result.suggestions.filter(s => itemById(s.item_id)?.checkable === true && VALID_STATES.has(s.state)) : [];
    // Deduplicate item IDs while retaining the last explicit suggestion.
    suggestions = [...new Map(valid.map(s => [s.item_id, s])).values()];
    if (!suggestions.length) notices.push('没有可直接应用的状态建议。请继续手动标记，或补充更明确的准备情况。');
    $('interpret-notices').textContent = notices.join('\n');
    $('interpret-notices').hidden = !notices.length;
    renderSuggestions();
    if (suggestions.length) announce('AI建议已整理，请核对并确认后应用。');
  } catch (error) {
    if (epoch !== sessionEpoch) return;
    $('interpret-notices').textContent = `${error.message} 已保留输入；手动标记与规则检查仍可使用。`;
    $('interpret-notices').hidden = false;
  } finally {
    button.textContent = '整理为状态建议';
    button.disabled = !health.ai_configured;
  }
}

function applySuggestions() {
  let count = 0;
  $('suggestion-list').querySelectorAll('input:checked').forEach(input => {
    const suggestion = suggestions[Number(input.dataset.suggestionIndex)];
    if (suggestion && itemById(suggestion.item_id)?.checkable === true && VALID_STATES.has(suggestion.state)) {
      progress.states[suggestion.item_id] = suggestion.state; count += 1;
    }
  });
  clearSuggestions(); changed(); renderChecklist();
  announce(`已应用 ${count} 条经你确认的状态建议，可随时手动更改。`);
}

function renderReport(result) {
  const summary = result.summary || {};
  const summaryNode = $('report-summary'); summaryNode.replaceChildren();
  const titles = { needs_action: '还有几件事，值得提前处理。', ready_for_review: '准备已整理好，下一步确认与审核。', scope_unconfirmed: '先确认适用流程，再核对具体要求。' };
  summaryNode.append(element('h3', '', titles[result.overall] || '按下面的事项安排下一步。'));
  if (result.notice) summaryNode.append(element('p', '', result.notice));
  const stats = element('div', 'report-stats');
  [['missing', '待准备'], ['unknown', '待确认'], ['needs_confirmation', '需确认要求']].forEach(([key, label]) => {
    if (Number.isFinite(summary[key])) { const unit = element('span'); unit.append(element('strong', '', summary[key]), document.createTextNode(label)); stats.append(unit); }
  });
  summaryNode.append(stats);
  const content = $('report-content'); content.replaceChildren();
  const items = Array.isArray(result.items) ? result.items : [];
  const priority = { invalid_date: 0, missing: 1, confirm: 2, unknown: 3, ready: 4, reference: 5 };
  [...items].sort((a, b) => (priority[a.status] ?? 3) - (priority[b.status] ?? 3)).forEach(item => {
    const article = element('article', 'report-item');
    const header = element('div', 'report-item-header');
    header.append(element('h3', '', item.title_zh || itemById(item.id)?.title_zh || item.id || '准备事项'));
    header.append(element('span', 'severity-label' + (item.status === 'ready' || item.status === 'reference' ? ' good' : ''), STATUS_LABELS[item.status] || '待确认'));
    article.append(header);
    if (item.message) article.append(element('p', '', item.message));
    if (item.next_action) article.append(element('p', 'report-action-text', '下一步：' + item.next_action));
    const merged = { ...(itemById(item.id) || {}), ...item };
    if (merged.quote || merged.source_id || merged.source?.url) article.append(makeEvidence(merged, merged.source));
    content.append(article);
  });
  const notes = Array.isArray(result.notes) ? result.notes.map(stringValue).filter(Boolean) : [];
  if (notes.length) {
    const note = element('div', 'notice notice-info');
    notes.forEach(text => note.append(element('p', '', text))); content.append(note);
  }
  let timestamp = '';
  if (result.generated_at && !Number.isNaN(Date.parse(result.generated_at))) timestamp = new Date(result.generated_at).toLocaleString('zh-CN', { hour12: false });
  $('report-meta').textContent = [PROFILE_LABELS[result.profile] || PROFILE_LABELS[progress.profile], result.move_in_date ? '计划入住 ' + result.move_in_date : '入住日期未填写', timestamp ? '生成于 ' + timestamp : '', '按资料规则检查 · 无需AI'].filter(Boolean).join(' · ');
  $('report-section').hidden = false;
}

async function generateReport() {
  const button = $('check-button');
  const revision = formRevision;
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = '正在检查…';
  const payload = { profile: progress.profile, move_in_date: progress.move_in_date, states: { ...progress.states }, dates: { ...progress.dates } };
  try {
    const result = await request('/api/check', payload);
    if (epoch !== sessionEpoch) return;
    if (!result || !Array.isArray(result.items) || !result.summary) throw new Error('检查结果格式不完整，未替换上一次报告。');
    report = result; renderReport(result);
    $('report-stale').hidden = revision === formRevision;
    saveProgress();
    $('report-section').focus({ preventScroll: true });
    $('report-section').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    announce(revision === formRevision ? '行动清单已生成，每项均可查看依据。' : '已生成报告，但输入刚刚变化，请重新生成。');
  } catch (error) { announce(`${error.message} 表单内容已保留。`, true); }
  finally { button.disabled = !catalog; button.textContent = '生成行动清单 →'; }
}

async function askQuestion(event) {
  event.preventDefault();
  const question = $('question').value.trim();
  if (!question) { $('question').focus(); return; }
  const button = $('ask-button');
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = '查询中…';
  const panel = $('answer-panel'); panel.hidden = false;
  panel.replaceChildren(element('p', 'answer-label', '正在根据收录资料查找依据…'));
  try {
    const result = await request('/api/ask', { question });
    if (epoch !== sessionEpoch || question !== $('question').value.trim()) { panel.hidden = true; return; }
    if (!result || typeof result.answer !== 'string') throw new Error('未收到有效回答，请查看原文或稍后重试。');
    panel.replaceChildren(element('p', 'answer-label', '根据收录资料回答'), element('p', 'answer-text', result.answer));
    if (result.notice) panel.append(element('p', 'answer-notice', result.notice));
    const evidence = Array.isArray(result.evidence) ? result.evidence : [];
    if (evidence.length) {
      const evidencePanel = element('div', 'answer-evidence');
      evidencePanel.append(element('p', 'answer-label', '回答依据'));
      evidence.forEach(entry => {
        const item = itemById(entry.item_id) || {};
        const source = sourceById(entry.source_id) || {};
        const block = element('div', 'evidence-content');
        if (entry.quote) block.append(element('blockquote', '', entry.quote));
        block.append(externalLink(source.title || '打开原始资料 ↗', source.url || item.source_url));
        evidencePanel.append(block);
      });
      panel.append(evidencePanel);
    } else {
      panel.append(element('p', 'answer-notice', '本次回答没有返回可展示的原文依据。请查看资料原文或向宿舍确认，勿据此视为已核实。'));
    }
  } catch (error) {
    if (epoch !== sessionEpoch) return;
    panel.replaceChildren(element('p', 'answer-notice', `${error.message} 问题已保留。你仍可查看来源原文，或使用无需AI的手动检查。`));
  } finally { button.textContent = '查规则'; button.disabled = !health.ai_configured; }
}

function exportReport() {
  if (!report) return;
  const blob = new Blob([JSON.stringify({ exported_at: new Date().toISOString(), report_is_stale: !$('report-stale').hidden, catalog_verified_date: catalog?.verified_date, report }, null, 2)], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = element('a'); link.href = url; link.download = `move-in-ready-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  announce('行动清单已导出为JSON。');
}

function resetProgress() {
  clearTimeout(saveTimer);
  let storageCleared = true;
  try { localStorage.removeItem(STORAGE_KEY); } catch (_) { storageCleared = false; }
  progress = { profile: 'unknown', move_in_date: '', states: {}, dates: {}, preparation_text: '' };
  formRevision += 1; sessionEpoch += 1; report = null; filter = 'all'; clearSuggestions();
  $('profile').value = 'unknown'; $('move-in-date').value = ''; $('preparation-text').value = ''; $('question').value = '';
  $('interpret-notices').hidden = true; $('answer-panel').hidden = true; $('report-section').hidden = true;
  document.querySelectorAll('[data-filter]').forEach(button => { const active = button.dataset.filter === 'all'; button.classList.toggle('is-active', active); button.setAttribute('aria-pressed', String(active)); });
  $('save-status').textContent = storageCleared ? '已清空 · 进度仅在本浏览器' : '页面已清空，但本地记录移除失败'; renderChecklist();
  $('clear-dialog').close(); announce(storageCleared ? '准备记录已清空。' : '当前页面已清空，但浏览器存储未允许移除记录；刷新后可能恢复旧记录。', !storageCleared); $('profile').focus();
}

async function boot() {
  if (booting) return;
  booting = true; $('load-error').hidden = true; $('workspace').setAttribute('aria-busy', 'true');
  const results = await Promise.allSettled([request('/api/catalog'), request('/api/health')]);
  if (results[1].status === 'fulfilled') health = results[1].value || { ai_configured: false };
  else health = { ai_configured: false };
  try {
    if (results[0].status === 'rejected') throw results[0].reason;
    const data = results[0].value;
    if (!data || !Array.isArray(data.items) || !Array.isArray(data.sources) || !data.items.length) throw new Error('资料清单不完整，请检查本地服务提供的catalog。');
    catalog = data;
    readSaved();
    $('profile').value = progress.profile; $('move-in-date').value = progress.move_in_date; $('preparation-text').value = progress.preparation_text;
    renderChecklist(); renderSources();
    $('check-button').disabled = false;
  } catch (error) {
    catalog = null; $('load-error').hidden = false; $('load-error-message').textContent = error.message || '请确认本地服务已启动。';
    $('checklist').replaceChildren(element('p', 'empty-note', '需要先成功读取资料，才能核对准备事项。'));
    $('item-count').textContent = '资料未加载'; $('verified-note').textContent = '资料暂未读取成功'; $('check-button').disabled = true;
  } finally {
    renderHealth();
    if (results[1].status === 'rejected') $('interpret-mode').textContent = 'AI配置状态暂时无法读取。手动核对可用，可重新读取资料后再试AI。';
    $('workspace').setAttribute('aria-busy', 'false'); booting = false;
  }
}

$('profile').addEventListener('change', () => { progress.profile = $('profile').value; changed({ invalidateSuggestions: true }); renderChecklist(); });
$('move-in-date').addEventListener('change', () => { progress.move_in_date = $('move-in-date').value; changed(); });
$('preparation-text').addEventListener('input', () => { progress.preparation_text = $('preparation-text').value; clearSuggestions(); });
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  filter = button.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(other => { const active = other === button; other.classList.toggle('is-active', active); other.setAttribute('aria-pressed', String(active)); });
  renderChecklist();
}));
$('save-progress').addEventListener('click', () => saveProgress(true));
$('clear-progress').addEventListener('click', () => $('clear-dialog').showModal());
$('cancel-clear').addEventListener('click', () => $('clear-dialog').close());
$('confirm-clear').addEventListener('click', resetProgress);
$('interpret-button').addEventListener('click', interpret);
$('apply-suggestions').addEventListener('click', applySuggestions);
$('check-button').addEventListener('click', generateReport);
$('ask-form').addEventListener('submit', askQuestion);
$('export-json').addEventListener('click', exportReport);
$('print-report').addEventListener('click', () => { if (report) window.print(); });
$('retry-load').addEventListener('click', boot);
boot();
