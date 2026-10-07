'use strict';

const STORAGE_KEY = 'move-in-ready.progress.v1';
const LANGUAGE_KEY = 'move-in-ready.language.v1';
const VALID_STATES = new Set(['ready', 'missing', 'unknown']);
const VALID_PROFILES = new Set(['standard', 'international', 'unknown']);
const CATEGORY_ORDER = ['document', 'step', 'supply', 'rule'];

// Course data and official Korean excerpts stay in the catalog. This map only
// translates application copy; unknown policy details must never be invented.
const KO = Object.freeze({
  '入住有数 · Move-in Ready': '입주 준비 한눈에 · Move-in Ready',
  '入住有数': '입주 준비 한눈에',
  '跳到准备清单': '준비 목록으로 건너뛰기',
  '入住有数首页': '입주 준비 한눈에 홈',
  '页面导航': '페이지 탐색',
  '界面语言': '화면 언어',
  '准备清单': '준비 목록',
  '规则问答': '규정 질문',
  '资料来源': '자료 출처',
  '正在读取资料': '자료를 불러오는 중',
  '宿舍入住准备助手': '기숙사 입주 준비 도우미',
  '课程项目': '수업 프로젝트',
  '入住之前，': '입주 전에,',
  '把准备的事理清。': '준비할 일을 정리하세요.',
  '按你的入住流程核对资料与物品，找出缺失和待确认项。每一条建议，都能回到资料原文。': '본인의 입주 절차에 따라 서류와 물품을 확인하고, 빠진 항목과 확인할 항목을 찾으세요. 각 제안은 자료 원문으로 확인할 수 있습니다.',
  '正在读取资料版本…': '자료 버전을 불러오는 중…',
  '使用说明': '이용 안내',
  '选流程，标记准备状态，': '절차와 상태를 고르고,',
  '得到下一步行动清单。': '다음 단계를 확인하세요.',
  '手动核对无需AI。': '수동 확인에는 AI가 필요하지 않습니다.',
  '文字理解与规则问答使用已配置的AI。': '문장 이해와 규정 질의에는 설정된 AI를 사용합니다.',
  '资料暂时没有加载成功': '자료를 불러오지 못했습니다',
  '重新读取': '다시 불러오기',
  '入住信息与快捷操作': '입주 정보와 빠른 작업',
  '先确定入住信息': '먼저 입주 정보 확인',
  '你的准备起点': '준비 시작점',
  '入住流程': '입주 절차',
  '暂未确认适用身份': '적용 대상 미확인',
  '已确认按一般入住说明办理': '일반 입주 안내 적용을 학교에 확인함',
  '留学生（文件要求待确认）': '유학생 (서류 요건 확인 필요)',
  '不确定流程时，需向宿舍办公室确认适用要求。': '적용 절차가 불확실하면 생활관 행정실에 확인하세요.',
  '计划入住日期': '예정 입주일',
  '可选': '선택',
  '用于检查有时间要求的准备事项。': '기한이 있는 준비 항목을 확인하는 데 사용합니다.',
  '进度只保存在本浏览器': '진행 상황은 이 브라우저에만 저장됩니다',
  '保存进度': '진행 상황 저장',
  '清空': '지우기',
  '把“不确定”保留下来': '불확실한 내용은 그대로 표시하세요',
  '已准备不等于已通过审核。缺少信息时，先标记待确认，再根据原文或宿舍答复补充。': '준비 완료 표시가 심사 통과를 뜻하지 않습니다. 정보가 부족하면 확인 필요로 표시하고 원문이나 생활관 답변에 따라 보완하세요.',
  '可选 · AI辅助': '선택 · AI 도움',
  '用一段话整理准备情况': '문장으로 준비 상황 정리',
  '例如：床品已经买好，洗衣液还没买，洗漱用品不确定。': '예: 침구는 준비했고 세제는 아직 사지 않았으며 세면도구는 확실하지 않습니다.',
  '你已经准备了什么，还有什么没准备？': '무엇을 준비했고, 무엇이 아직 없나요?',
  '直接描述当前情况，AI会提出状态建议，由你确认后再应用。': '현재 상황을 적으면 AI가 상태를 제안합니다. 확인한 뒤 적용하세요.',
  '正在检查AI配置…': 'AI 설정 확인 중…',
  '整理为状态建议': '상태 제안 만들기',
  '确认后再更新清单': '확인 후 목록 업데이트',
  '检查每条解释，取消不准确的建议。': '각 설명을 확인하고 부정확한 제안은 선택 해제하세요.',
  '应用所选建议': '선택한 제안 적용',
  '逐项核对': '항목별 확인',
  '入住准备清单': '입주 준비 목록',
  '读取中': '불러오는 중',
  '逐项标记你的实际准备情况': '실제 준비 상황을 항목별로 표시하세요',
  '已标记为准备好的适用事项比例': '준비 완료로 표시한 적용 항목의 비율',
  '已准备 0': '준비 완료 0',
  '待准备 0': '준비 필요 0',
  '待确认 0': '확인 필요 0',
  '筛选清单状态': '목록 상태 필터',
  '全部': '전체',
  '待准备': '준비 필요',
  '待确认': '확인 필요',
  '已准备': '준비 완료',
  '正在读取经过整理的官方资料…': '정리된 공식 자료를 불러오는 중…',
  '准备好后，生成下一步。': '준비 상태를 표시한 뒤 다음 단계를 만드세요.',
  '检查按资料规则执行，不需要AI。': '자료에 따른 확인이며 AI가 필요하지 않습니다.',
  '生成行动清单': '실행 목록 만들기',
  '安排下一步': '다음 단계 정리',
  '你的行动清单': '나의 실행 목록',
  '导出JSON': 'JSON 내보내기',
  '打印': '인쇄',
  '准备信息已经变化，请重新生成行动清单。': '준비 정보가 변경되었습니다. 실행 목록을 다시 만드세요.',
  '为你推荐的下一步': '추천하는 다음 단계',
  'PERSONALIZED NEXT STEPS': '맞춤형 다음 단계',
  '根据你选择的身份与准备状态，从待处理事项中选出最多三项；仅作准备辅助。': '선택한 대상과 준비 상태에 따라 처리할 항목을 최대 세 개 추천합니다. 준비를 돕기 위한 안내입니다.',
  '有疑问，查依据': '궁금한 점은 근거 확인',
  '规则怎么说？': '규정에는 어떻게 나와 있나요?',
  '回答只依据已收录资料。资料没有说明的内容，会明确提示无法确认。': '답변은 수록된 자료만 근거로 합니다. 자료에 없는 내용은 확인할 수 없다고 안내합니다.',
  '输入你的规则问题': '규정 관련 질문 입력',
  '例如：入住前需要准备哪些证明？': '예: 입주 전에 어떤 증명서를 준비해야 하나요?',
  '查规则': '규정 확인',
  '可追溯的资料': '출처를 확인할 수 있는 자료',
  '来源与原文': '출처와 원문',
  '每条核对事项均可展开查看依据；这里列出完整来源。': '각 항목에서 근거를 펼쳐 볼 수 있습니다. 여기에는 전체 출처가 표시됩니다.',
  '课程项目 · 资料辅助核对工具': '수업 프로젝트 · 자료 확인 보조 도구',
  '最终办理要求与安排以学校最新通知为准。': '최종 절차와 일정은 학교의 최신 공지를 따르세요.',
  '清空当前准备记录？': '현재 준비 기록을 지울까요?',
  '将移除本浏览器保存的流程、日期与状态。已导出的文件不受影响。': '이 브라우저에 저장된 절차, 날짜와 상태가 삭제됩니다. 이미 내보낸 파일은 유지됩니다.',
  '保留记录': '기록 유지',
  '清空记录': '기록 삭제',
  '材料与证明': '서류 및 증명',
  '办理与确认': '절차 및 확인',
  '生活用品': '생활용품',
  '规则与注意事项': '규정 및 유의 사항',
  '已准备 · 仍需审核': '준비 완료 · 심사 별도',
  '确认适用要求': '적용 요건 확인',
  '日期需处理': '날짜 확인 필요',
  '参考说明': '참고 안내',
  '适用于你已向学校确认按一般入住说明办理的情况。': '학교에 일반 입주 안내가 적용됨을 확인한 경우입니다.',
  '资料中的文件要求可能因留学生流程而不同；先向办公室确认，不直接套用。': '유학생의 서류 요건은 다를 수 있습니다. 일반 안내를 그대로 적용하지 말고 담당 부서에 먼저 확인하세요.',
  '先整理共同准备事项；证明与办理要求需确认适用身份。': '공통 준비 항목부터 정리하세요. 증명서와 절차는 본인에게 적용되는 요건을 확인해야 합니다.',
  '新标签页打开': '새 탭에서 열림',
  '查看依据原文': '근거 원문 보기',
  '官方资料': '공식 자료',
  '原文位置：': '원문 위치: ',
  '打开官方来源 ↗': '공식 출처 열기 ↗',
  '补充依据：': '추가 근거: ',
  '打开补充来源 ↗': '추가 출처 열기 ↗',
  '建议准备': '준비 권장',
  '禁止事项': '금지 사항',
  '需核对': '확인 필요',
  '资料说明': '자료 안내',
  '适用要求待确认': '적용 요건 확인 필요',
  '参考 · 请确认适用': '참고 · 적용 여부 확인',
  '已核对': '확인 완료',
  '需处理': '처리 필요',
  '证明日期': '증명서 발급일',
  '符合条件': '조건에 맞는',
  '其他事项': '기타 항목',
  '自报已准备 / 可核对事项': '본인이 준비 완료로 표시 / 확인 가능 항목',
  '资料核对：': '자료 확인: ',
  '查看原始资料 ↗': '원본 자료 보기 ↗',
  '资料核对日期': '자료 확인일',
  '未注明': '표기 없음',
  '查看原文可追溯': '원문으로 확인 가능',
  '准备事项': '준비 항목',
  '还有几件事，值得提前处理。': '미리 처리할 항목이 있습니다.',
  '准备已整理好，下一步确认与审核。': '준비를 정리했습니다. 다음은 확인과 심사입니다.',
  '先确认适用流程，再核对具体要求。': '적용 절차를 먼저 확인한 뒤 세부 요건을 살펴보세요.',
  '按下面的事项安排下一步。': '아래 항목에 따라 다음 단계를 정하세요.',
  '需确认要求': '요건 확인 필요',
  '下一步：': '다음 단계: ',
  '计划入住 ': '예정 입주일 ',
  '入住日期未填写': '입주일 미입력',
  '生成于 ': '생성 시각 ',
  '按资料规则检查 · 无需AI': '자료에 따른 확인 · AI 불필요',
  '根据收录资料回答': '수록 자료에 근거한 답변',
  '回答依据': '답변 근거',
  '本次回答没有返回可展示的原文依据。请查看资料原文或向宿舍确认，勿据此视为已核实。': '이번 답변에는 제시할 원문 근거가 없습니다. 원문을 확인하거나 생활관에 문의하세요. 검증된 사실로 간주하지 마세요.',
  '行动清单已导出为JSON。': '실행 목록을 JSON으로 내보냈습니다.',
  '已清空 · 进度仅在本浏览器': '삭제 완료 · 진행 상황은 이 브라우저에만 저장됩니다',
  '页面已清空，但本地记录移除失败': '화면은 비웠지만 저장 기록을 삭제하지 못했습니다',
  '准备记录已清空。': '준비 기록을 삭제했습니다.',
  '当前页面已清空，但浏览器存储未允许移除记录；刷新后可能恢复旧记录。': '화면은 비웠지만 브라우저 저장소의 기록을 삭제하지 못했습니다. 새로고침하면 이전 기록이 복원될 수 있습니다.',
  '资料清单不完整，请检查本地服务提供的catalog。': '자료 목록이 불완전합니다. 로컬 서비스의 catalog를 확인하세요.',
  '请确认本地服务已启动。': '로컬 서비스가 실행 중인지 확인하세요.',
  '需要先成功读取资料，才能核对准备事项。': '자료를 불러온 뒤 준비 항목을 확인할 수 있습니다.',
  '资料未加载': '자료를 불러오지 못함',
  '资料暂未读取成功': '자료를 아직 불러오지 못함',
  'AI配置状态暂时无法读取。手动核对可用，可重新读取资料后再试AI。': 'AI 설정 상태를 읽지 못했습니다. 수동 확인은 가능하며, 자료를 다시 불러온 뒤 AI를 다시 시도하세요.',
  '切换语言后，请重新运行 AI 整理或问答。': '언어를 변경했습니다. AI 정리나 질의를 다시 실행하세요.',
  '暂无需要推荐的待办事项。请继续核对最新官方通知。': '추천할 대기 항목이 없습니다. 최신 공식 공지를 계속 확인하세요.',
  '服务未返回有效结果，请检查本地服务后重试。': '서비스가 유효한 결과를 반환하지 않았습니다. 로컬 서비스를 확인한 뒤 다시 시도하세요.',
  '请求未完成，请稍后重试。': '요청을 완료하지 못했습니다. 잠시 후 다시 시도하세요.',
  '请求超时，已保留输入。请稍后重试。': '요청 시간이 초과되었습니다. 입력은 유지됩니다. 잠시 후 다시 시도하세요.',
  '已恢复流程、日期与逐项状态': '절차, 날짜와 항목별 상태를 복원했습니다',
  '无法读取本地记录，当前仍可核对': '로컬 기록을 읽지 못했지만 지금도 확인할 수 있습니다',
  '已保存 · 仅在本浏览器': '저장 완료 · 이 브라우저에만 저장됨',
  '准备进度已保存在本浏览器。': '준비 진행 상황을 이 브라우저에 저장했습니다.',
  '本地保存不可用，请导出行动清单': '로컬 저장을 사용할 수 없습니다. 실행 목록을 내보내세요',
  '浏览器未允许保存。表单仍保留在当前页面，可生成并导出行动清单。': '브라우저에서 저장을 허용하지 않았습니다. 입력은 현재 화면에 유지되며 실행 목록을 만들어 내보낼 수 있습니다.',
  '正在保存…': '저장 중…',
  '手动可用 · AI已配置': '수동 확인 가능 · AI 설정 완료',
  '手动检查可用': '수동 확인 가능',
  '点击后将文字发送给AI；文字不写入本地进度。建议经你确认后应用，请勿填写证件号码。': '클릭하면 입력 문장을 AI로 보냅니다. 문장은 로컬 진행 기록에 저장하지 않습니다. 제안은 확인 후 적용하며 증명서 번호를 입력하지 마세요.',
  'AI尚未配置。你仍可逐项手动标记并生成行动清单。': 'AI가 설정되지 않았습니다. 항목을 직접 표시하고 실행 목록을 만들 수 있습니다.',
  'AI已配置。以实际返回为准，回答会附资料依据。': 'AI가 설정되었습니다. 실제 응답을 확인하세요. 답변에는 자료 근거가 함께 표시됩니다.',
  '规则问答需要AI配置。现在可直接查看各项原文与资料来源。': '규정 질의에는 AI 설정이 필요합니다. 지금은 각 항목의 원문과 출처를 직접 볼 수 있습니다.',
  ' · 核对 ': ' · 확인 ',
  ' · 补充依据': ' · 추가 근거',
  '先描述你的准备情况。': '먼저 준비 상황을 적어 주세요.',
  '正在整理…': '정리 중…',
  '输入或入住流程已变化，请重新整理，避免应用旧建议。': '입력이나 입주 절차가 바뀌었습니다. 이전 제안을 적용하지 않도록 다시 정리하세요.',
  '没有可直接应用的状态建议。请继续手动标记，或补充更明确的准备情况。': '바로 적용할 상태 제안이 없습니다. 직접 표시하거나 준비 상황을 더 구체적으로 적어 주세요.',
  'AI建议已整理，请核对并确认后应用。': 'AI 제안을 정리했습니다. 내용을 확인한 뒤 적용하세요.',
  '已保留输入；手动标记与规则检查仍可使用。': '입력은 유지됩니다. 수동 표시와 규정 확인은 계속 사용할 수 있습니다.',
  '正在检查…': '확인 중…',
  '检查结果格式不完整，未替换上一次报告。': '확인 결과 형식이 불완전하여 이전 보고서를 교체하지 않았습니다.',
  '行动清单已生成，每项均可查看依据。': '실행 목록을 만들었습니다. 각 항목의 근거를 확인할 수 있습니다.',
  '已生成报告，但输入刚刚变化，请重新生成。': '보고서를 만들었지만 입력이 변경되었습니다. 다시 생성하세요.',
  '表单内容已保留。': '입력 내용은 유지됩니다.',
  '查询中…': '조회 중…',
  '正在根据收录资料查找依据…': '수록 자료에서 근거를 찾는 중…',
  '未收到有效回答，请查看原文或稍后重试。': '유효한 답변을 받지 못했습니다. 원문을 보거나 잠시 후 다시 시도하세요.',
  '打开原始资料 ↗': '원본 자료 열기 ↗',
  '问题已保留。你仍可查看来源原文，或使用无需AI的手动检查。': '질문은 유지됩니다. 출처 원문을 보거나 AI가 필요 없는 수동 확인을 사용할 수 있습니다.',
  '只允许本机访问。': '이 컴퓨터에서만 접속할 수 있습니다.',
  '界面文件尚未就绪。': '화면 파일을 사용할 수 없습니다.',
  '本地资料或配置读取失败。': '로컬 자료나 설정을 읽지 못했습니다.',
  '页面不存在。': '페이지를 찾을 수 없습니다.',
  '请求来源不匹配。': '요청 출처가 일치하지 않습니다.',
  '请发送 JSON。': 'JSON으로 요청하세요.',
  '接口不存在。': '요청한 API가 없습니다.',
  '请求为空或内容过长。': '요청이 비어 있거나 너무 깁니다.',
  '输入格式无效，请核对身份、状态和日期。': '입력 형식이 올바르지 않습니다. 대상, 상태와 날짜를 확인하세요.',
  '处理失败，请保留当前记录并重试。': '처리에 실패했습니다. 현재 기록을 유지하고 다시 시도하세요.',
  'AI 尚未配置，手动清单核对仍可使用。': 'AI가 설정되지 않았습니다. 수동 목록 확인은 계속 사용할 수 있습니다.',
  '已有 AI 请求处理中，请稍后重试。': '다른 AI 요청이 처리 중입니다. 잠시 후 다시 시도하세요.',
  'AI 服务暂不可用或返回格式无效；你的手动记录已保留，请重试。': 'AI 서비스를 사용할 수 없거나 응답 형식이 올바르지 않습니다. 수동 기록은 유지되므로 다시 시도하세요.',
  'AI 返回的建议无法校验，请继续使用手动选择。': 'AI 제안을 검증할 수 없습니다. 수동 선택을 계속 사용하세요.',
  'AI 返回了无效清单项目，建议未应用。': 'AI가 올바르지 않은 목록 항목을 반환했습니다. 제안은 적용되지 않았습니다.',
  'AI 返回了未知或重复项目，建议未应用。': 'AI가 알 수 없거나 중복된 항목을 반환했습니다. 제안은 적용되지 않았습니다.',
  'AI 返回了无效说明，建议未应用。': 'AI가 올바르지 않은 설명을 반환했습니다. 제안은 적용되지 않았습니다.',
  'AI 答案格式无效，未展示未经校验的结果。': 'AI 답변 형식이 올바르지 않아 검증되지 않은 결과를 표시하지 않았습니다.',
  'AI 答案含有无法核对的引用，未展示该结果。': 'AI 답변에 확인할 수 없는 인용이 있어 결과를 표시하지 않았습니다.',
});

const tr = (text) => currentLanguage === 'ko' ? (KO[text] || text) : text;
const labels = (entries) => Object.fromEntries(Object.entries(entries).map(([key, value]) => [key, tr(value)]));
const stateLabels = () => labels({ ready: '已准备', missing: '待准备', unknown: '待确认' });
const profileLabels = () => labels({ standard: '已确认按一般入住说明办理', international: '留学生（文件要求待确认）', unknown: '暂未确认适用身份' });
const categoryLabels = () => labels({ document: '材料与证明', step: '办理与确认', supply: '生活用品', rule: '规则与注意事项' });
const statusLabels = () => labels({ ready: '已准备 · 仍需审核', missing: '待准备', unknown: '待确认', confirm: '确认适用要求', invalid_date: '日期需处理', reference: '参考说明' });
const profileHelp = () => labels({ standard: '适用于你已向学校确认按一般入住说明办理的情况。', international: '资料中的文件要求可能因留学生流程而不同；先向办公室确认，不直接套用。', unknown: '先整理共同准备事项；证明与办理要求需确认适用身份。' });
const itemTitle = (item) => currentLanguage === 'ko' ? item?.title_ko || item?.title_zh : item?.title_zh;
const itemDescription = (item) => currentLanguage === 'ko' ? item?.description_ko || item?.description_zh : item?.description_zh;
const itemNote = (item) => currentLanguage === 'ko' ? item?.conditions?.notes_ko || item?.conditions?.notes_zh : item?.conditions?.notes_zh;
const sourceTitle = (source) => currentLanguage === 'ko' ? source?.title_ko || source?.title : source?.title;
const sourceScope = (source) => currentLanguage === 'ko' ? source?.scope_ko || source?.scope : source?.scope;
const sourceLocator = (value) => currentLanguage === 'ko' ? String(value).replaceAll('标题', '제목').replaceAll('最后注释', '마지막 주석').replaceAll('入住说明', '입사 안내').replaceAll('、', ', ') : value;
let currentLanguage = 'zh';

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

const staticTextNodes = [];
const textWalker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
while (textWalker.nextNode()) {
  const node = textWalker.currentNode;
  const value = node.nodeValue.trim();
  if (KO[value]) staticTextNodes.push({ node, original: node.nodeValue, value });
}
const staticAttributes = [];
document.querySelectorAll('[aria-label], [placeholder], [title]').forEach(node => {
  for (const attribute of ['aria-label', 'placeholder', 'title']) {
    const value = node.getAttribute(attribute);
    if (value && KO[value]) staticAttributes.push({ node, attribute, value });
  }
});

function readLanguage() {
  try { return localStorage.getItem(LANGUAGE_KEY) === 'ko' ? 'ko' : 'zh'; }
  catch (_) { return 'zh'; }
}

function renderStaticLanguage() {
  document.documentElement.lang = currentLanguage === 'ko' ? 'ko' : 'zh-CN';
  document.title = tr('入住有数 · Move-in Ready');
  staticTextNodes.forEach(({ node, original, value }) => {
    if (node.isConnected) node.nodeValue = original.replace(value, tr(value));
  });
  staticAttributes.forEach(({ node, attribute, value }) => {
    if (node.isConnected) node.setAttribute(attribute, tr(value));
  });
  document.querySelectorAll('[data-language]').forEach(button => {
    const active = button.dataset.language === currentLanguage;
    button.classList.toggle('is-active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}

async function changeLanguage(language) {
  if (!['zh', 'ko'].includes(language) || language === currentLanguage) return;
  currentLanguage = language;
  try { localStorage.setItem(LANGUAGE_KEY, language); } catch (_) { /* Language still works for this session. */ }
  sessionEpoch += 1;
  clearSuggestions();
  $('interpret-notices').hidden = true;
  $('interpret-notices').textContent = '';
  $('answer-panel').hidden = true;
  $('answer-panel').replaceChildren();
  renderStaticLanguage();
  renderHealth();
  $('interpret-button').textContent = tr('整理为状态建议');
  $('ask-button').textContent = tr('查规则');
  $('check-button').textContent = tr('生成行动清单') + ' →';
  if (catalog) { renderChecklist(); renderSources(); saveProgress(); }
  if (report) {
    report = null;
    $('report-section').hidden = true;
    await refreshReportLanguage();
  }
  if (!catalog) await boot();
  announce(tr('切换语言后，请重新运行 AI 整理或问答。'));
}

async function refreshReportLanguage() {
  const epoch = sessionEpoch;
  const revision = formRevision;
  const payload = { profile: progress.profile, move_in_date: progress.move_in_date, states: { ...progress.states }, dates: { ...progress.dates }, language: currentLanguage };
  try {
    const result = await request('/api/check', payload);
    if (epoch !== sessionEpoch || revision !== formRevision || !Array.isArray(result.items) || !result.summary) return;
    report = result;
    renderReport(result);
    $('report-stale').hidden = true;
  } catch (error) {
    if (epoch === sessionEpoch) announce(error.message, true);
  }
}

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
  link.setAttribute('aria-label', `${label}（${tr('新标签页打开')}）`);
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
    try { result = await response.json(); } catch (_) { throw new Error(tr('服务未返回有效结果，请检查本地服务后重试。')); }
    if (!response.ok) throw new Error(tr(stringValue(result?.message) || stringValue(result?.error) || '请求未完成，请稍后重试。'));
    return result;
  } catch (error) {
    if (error.name === 'AbortError') throw new Error(tr('请求超时，已保留输入。请稍后重试。'));
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
    $('save-status').textContent = tr('已恢复流程、日期与逐项状态');
  } catch (_) {
    $('save-status').textContent = tr('无法读取本地记录，当前仍可核对');
  }
}

function saveProgress(explicit = false) {
  clearTimeout(saveTimer);
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ profile: progress.profile, move_in_date: progress.move_in_date, states: progress.states, dates: progress.dates, saved_at: new Date().toISOString(), catalog_version: catalog?.schema_version }));
    $('save-status').textContent = tr('已保存 · 仅在本浏览器');
    if (explicit) announce(tr('准备进度已保存在本浏览器。'));
  } catch (_) {
    $('save-status').textContent = tr('本地保存不可用，请导出行动清单');
    if (explicit) announce(tr('浏览器未允许保存。表单仍保留在当前页面，可生成并导出行动清单。'), true);
  }
}

function changed({ invalidateSuggestions = false } = {}) {
  formRevision += 1;
  if (report) $('report-stale').hidden = false;
  if (invalidateSuggestions) clearSuggestions();
  $('save-status').textContent = tr('正在保存…');
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => saveProgress(), 250);
  renderProgress();
}

function renderHealth() {
  const configured = health.ai_configured === true;
  $('mode-indicator').classList.toggle('configured', configured);
  $('mode-text').textContent = tr(configured ? '手动可用 · AI已配置' : '手动检查可用');
  $('interpret-button').disabled = !configured || !catalog;
  $('ask-button').disabled = !configured || !catalog;
  $('interpret-mode').textContent = tr(configured ? '点击后将文字发送给AI；文字不写入本地进度。建议经你确认后应用，请勿填写证件号码。' : 'AI尚未配置。你仍可逐项手动标记并生成行动清单。');
  $('ask-mode').textContent = tr(configured ? 'AI已配置。以实际返回为准，回答会附资料依据。' : '规则问答需要AI配置。现在可直接查看各项原文与资料来源。');
}

function makeEvidence(item, overrideSource) {
  const source = overrideSource || sourceById(item.source_id) || {};
  const details = element('details', 'item-evidence');
  details.append(element('summary', '', tr('查看依据原文')));
  const content = element('div', 'evidence-content');
  const title = sourceTitle(source) || tr('官方资料');
  content.append(element('p', 'source-meta', `${title}${item.verified_date || source.verified_date ? tr(' · 核对 ') + (item.verified_date || source.verified_date) : ''}`));
  if (item.source_locator) content.append(element('p', 'source-meta', tr('原文位置：') + sourceLocator(item.source_locator)));
  if (item.quote) content.append(element('blockquote', '', item.quote));
  if (itemNote(item)) content.append(element('p', '', itemNote(item)));
  content.append(externalLink(tr('打开官方来源 ↗'), item.source_url || source.url));
  if (Array.isArray(item.additional_evidence)) {
    item.additional_evidence.forEach(entry => {
      const extraSource = sourceById(entry.source_id) || {};
      content.append(element('p', 'source-meta', tr('补充依据：') + (sourceTitle(extraSource) || entry.source_id || tr('官方资料'))));
      if (entry.source_locator) content.append(element('p', 'source-meta', tr('原文位置：') + sourceLocator(entry.source_locator)));
      if (entry.quote) content.append(element('blockquote', '', entry.quote));
      content.append(externalLink(tr('打开补充来源 ↗'), entry.source_url || extraSource.url));
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
  const title = element('h3', '', itemTitle(item) || item.id);
  title.id = 'title-' + item.id;
  copy.append(title);
  if (itemDescription(item)) copy.append(element('p', 'item-description', itemDescription(item)));
  top.append(copy);
  const scope = item.applicability?.[progress.profile];
  let tag = item.checkable ? (item.requirement === 'recommended' ? '建议准备' : item.requirement === 'prohibited' ? '禁止事项' : '需核对') : '资料说明';
  if (scope === 'confirmation_required') tag = '适用要求待确认';
  if (scope === 'reference') tag = '参考 · 请确认适用';
  tag = tr(tag);
  top.append(element('span', 'item-tag' + ((scope === 'confirmation_required' || scope === 'reference') ? ' conditional' : ''), tag));
  article.append(top);
  if (item.checkable === true) {
    const controls = element('div', 'item-controls');
    const fieldset = element('fieldset', 'status-choice');
    fieldset.append(element('legend', '', currentLanguage === 'ko' ? `${itemTitle(item) || item.id} 상태` : `${itemTitle(item) || item.id}的准备状态`));
    const stateNames = item.requirement === 'prohibited' ? labels({ ready: '已核对', missing: '需处理', unknown: '待确认' }) : stateLabels();
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
      label.append(input, element('span', '', stateNames[state]));
      fieldset.append(label);
    }
    controls.append(fieldset);
    if (item.date_field === true) {
      const dateWrap = element('div', 'item-date');
      const label = element('label', '', tr('证明日期'));
      label.htmlFor = 'date-' + item.id;
      const input = element('input');
      input.type = 'date'; input.id = 'date-' + item.id;
      input.setAttribute('aria-label', currentLanguage === 'ko' ? `${itemTitle(item) || item.id} 증명서 발급일` : `${itemTitle(item) || item.id}的证明日期`);
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
    list.append(element('p', 'empty-note', currentLanguage === 'ko' ? `현재 “${stateLabels()[filter] || tr('符合条件')}” 상태인 항목이 없습니다.` : `当前没有标记为“${stateLabels()[filter] || '符合条件'}”的事项。`));
  } else {
    const knownCategories = [...CATEGORY_ORDER, ...new Set(items.map(item => item.category).filter(c => !CATEGORY_ORDER.includes(c)))];
    knownCategories.forEach(category => {
      const group = items.filter(item => item.category === category);
      if (!group.length) return;
      list.append(element('h3', 'item-group-title', `${categoryLabels()[category] || tr('其他事项')} · ${group.length}`));
      group.forEach(item => list.append(renderItem(item)));
    });
  }
  $('profile-help').textContent = profileHelp()[progress.profile];
  $('item-count').textContent = currentLanguage === 'ko' ? `확인 가능 ${checkableItems().length}개 · 참고 ${catalog.items.length - checkableItems().length}개` : `${checkableItems().length}项可核对 · ${catalog.items.length - checkableItems().length}项参考`;
  renderProgress();
}

function renderProgress() {
  const items = checkableItems();
  const counts = { ready: 0, missing: 0, unknown: 0 };
  items.forEach(item => { counts[stateOf(item.id)] += 1; });
  const percent = items.length ? Math.round(counts.ready / items.length * 100) : 0;
  $('progress-count').textContent = `${counts.ready} / ${items.length}`;
  $('progress-label').textContent = tr('自报已准备 / 可核对事项');
  $('progress-fill').style.width = percent + '%';
  $('progress-bar').setAttribute('aria-valuenow', String(percent));
  $('progress-bar').setAttribute('aria-valuetext', currentLanguage === 'ko' ? `확인 가능 항목 ${items.length}개 중 ${counts.ready}개를 준비 완료로 표시했습니다. 심사 통과를 의미하지 않습니다.` : `${items.length}项可核对事项中，${counts.ready}项标记已准备；不代表已通过审核。`);
  Object.keys(counts).forEach(state => { $(state + '-count').textContent = stateLabels()[state] + ' ' + counts[state]; });
}

function renderSources() {
  const list = $('source-list'); list.replaceChildren();
  catalog.sources.forEach(source => {
    const article = element('article', 'source-entry');
    article.append(element('h3', '', sourceTitle(source) || source.id));
    if (sourceScope(source)) article.append(element('p', '', sourceScope(source)));
    article.append(element('p', '', `${tr('资料核对：')}${source.verified_date || catalog.verified_date || tr('未注明')}`));
    article.append(externalLink(tr('查看原始资料 ↗'), source.url));
    const referenced = catalog.items.flatMap(item => {
      const entries = item.source_id === source.id && item.quote ? [{ title: itemTitle(item) || item.id, quote: item.quote, locator: item.source_locator }] : [];
      (Array.isArray(item.additional_evidence) ? item.additional_evidence : []).forEach(entry => {
        if (entry.source_id === source.id && entry.quote) entries.push({ title: (itemTitle(item) || item.id) + tr(' · 补充依据'), quote: entry.quote, locator: entry.source_locator });
      });
      return entries;
    });
    if (referenced.length) {
      const details = element('details', 'item-evidence');
      details.append(element('summary', '', currentLanguage === 'ko' ? `수록된 원문 ${referenced.length}개 펼치기` : `展开收录的 ${referenced.length} 段原文`));
      referenced.forEach(entry => {
        details.append(element('p', 'source-meta', entry.title));
        if (entry.locator) details.append(element('p', 'source-meta', tr('原文位置：') + sourceLocator(entry.locator)));
        details.append(element('blockquote', '', entry.quote));
      });
      article.append(details);
    }
    list.append(article);
  });
  $('verified-note').textContent = currentLanguage === 'ko' ? `자료 확인일 ${catalog.verified_date || tr('未注明')} · 출처 ${catalog.sources.length}개 · 원문으로 확인 가능` : `资料核对日期 ${catalog.verified_date || '未注明'} · ${catalog.sources.length}份来源 · 查看原文可追溯`;
  const disclaimer = currentLanguage === 'ko' ? catalog.disclaimer_ko : catalog.disclaimer_zh;
  if (disclaimer) $('sources-description').textContent = disclaimer;
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
    const label = element('label', '', itemTitle(item) || item.id);
    label.htmlFor = input.id;
    label.append(element('span', 'suggestion-change', currentLanguage === 'ko' ? `현재: ${stateLabels()[stateOf(item.id)]} → 제안: ${stateLabels()[suggestion.state]}` : `当前：${stateLabels()[stateOf(item.id)]} → 建议：${stateLabels()[suggestion.state]}`));
    if (suggestion.reason) label.append(element('small', '', suggestion.reason));
    row.append(input, label); list.append(row);
  });
  $('suggestions-panel').hidden = !suggestions.length;
  updateSuggestionButton();
}

function updateSuggestionButton() {
  const count = $('suggestion-list').querySelectorAll('input:checked').length;
  $('apply-suggestions').textContent = currentLanguage === 'ko' ? `제안 ${count}개 확인 후 적용` : `确认并应用 ${count} 条建议`;
  $('apply-suggestions').disabled = count === 0;
}

async function interpret() {
  const text = $('preparation-text').value.trim();
  if (!text) { $('preparation-text').focus(); announce(tr('先描述你的准备情况。')); return; }
  const button = $('interpret-button');
  const profile = progress.profile;
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = tr('正在整理…');
  clearSuggestions(); $('interpret-notices').hidden = true;
  try {
    const result = await request('/api/interpret', { text, profile, language: currentLanguage });
    if (epoch !== sessionEpoch) return;
    if (text !== $('preparation-text').value.trim() || profile !== progress.profile) {
      announce(tr('输入或入住流程已变化，请重新整理，避免应用旧建议。')); return;
    }
    const notices = Array.isArray(result.notices) ? result.notices.map(stringValue).filter(Boolean) : [stringValue(result.notices)].filter(Boolean);
    const valid = Array.isArray(result.suggestions) ? result.suggestions.filter(s => itemById(s.item_id)?.checkable === true && VALID_STATES.has(s.state)) : [];
    // Deduplicate item IDs while retaining the last explicit suggestion.
    suggestions = [...new Map(valid.map(s => [s.item_id, s])).values()];
    if (!suggestions.length) notices.push(tr('没有可直接应用的状态建议。请继续手动标记，或补充更明确的准备情况。'));
    $('interpret-notices').textContent = notices.join('\n');
    $('interpret-notices').hidden = !notices.length;
    renderSuggestions();
    if (suggestions.length) announce(tr('AI建议已整理，请核对并确认后应用。'));
  } catch (error) {
    if (epoch !== sessionEpoch) return;
    $('interpret-notices').textContent = `${error.message} ${tr('已保留输入；手动标记与规则检查仍可使用。')}`;
    $('interpret-notices').hidden = false;
  } finally {
    button.textContent = tr('整理为状态建议');
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
  announce(currentLanguage === 'ko' ? `확인한 상태 제안 ${count}개를 적용했습니다. 언제든 직접 수정할 수 있습니다.` : `已应用 ${count} 条经你确认的状态建议，可随时手动更改。`);
}

function renderRecommendations(result) {
  const list = $('recommendations');
  const notice = $('recommendation-notice');
  list.replaceChildren();
  const recommendations = Array.isArray(result.recommendations) ? result.recommendations.slice(0, 3) : [];
  notice.hidden = recommendations.length > 0;
  if (!recommendations.length) {
    notice.textContent = result.recommendation_notice || tr('暂无需要推荐的待办事项。请继续核对最新官方通知。');
    return;
  }
  recommendations.forEach((recommendation, index) => {
    const item = itemById(recommendation.id) || {};
    const source = recommendation.source || sourceById(item.source_id) || {};
    const article = element('article', 'recommendation-card');
    const header = element('div', 'recommendation-card-header');
    header.append(element('span', 'recommendation-rank', String(index + 1).padStart(2, '0')));
    const title = element('div', 'recommendation-title');
    title.append(element('h4', '', itemTitle(item) || recommendation.id || tr('准备事项')));
    title.append(element('span', 'severity-label', statusLabels()[recommendation.status] || tr('待确认')));
    header.append(title); article.append(header);
    if (recommendation.reason) article.append(element('p', 'recommendation-reason', recommendation.reason));
    if (recommendation.next_action) article.append(element('p', 'recommendation-action', tr('下一步：') + recommendation.next_action));
    if (item.quote || source.url) article.append(makeEvidence(item, source));
    list.append(article);
  });
}

function renderReport(result) {
  const summary = result.summary || {};
  const summaryNode = $('report-summary'); summaryNode.replaceChildren();
  const titles = { needs_action: '还有几件事，值得提前处理。', ready_for_review: '准备已整理好，下一步确认与审核。', scope_unconfirmed: '先确认适用流程，再核对具体要求。' };
  summaryNode.append(element('h3', '', tr(titles[result.overall] || '按下面的事项安排下一步。')));
  if (result.notice) summaryNode.append(element('p', '', result.notice));
  const stats = element('div', 'report-stats');
  [['missing', '待准备'], ['unknown', '待确认'], ['needs_confirmation', '需确认要求']].forEach(([key, label]) => {
    if (Number.isFinite(summary[key])) { const unit = element('span'); unit.append(element('strong', '', summary[key]), document.createTextNode(tr(label))); stats.append(unit); }
  });
  summaryNode.append(stats);
  renderRecommendations(result);
  const content = $('report-content'); content.replaceChildren();
  const items = Array.isArray(result.items) ? result.items : [];
  const priority = { invalid_date: 0, missing: 1, confirm: 2, unknown: 3, ready: 4, reference: 5 };
  [...items].sort((a, b) => (priority[a.status] ?? 3) - (priority[b.status] ?? 3)).forEach(item => {
    const article = element('article', 'report-item');
    const header = element('div', 'report-item-header');
    header.append(element('h3', '', itemTitle(item) || itemTitle(itemById(item.id)) || item.id || tr('准备事项')));
    header.append(element('span', 'severity-label' + (item.status === 'ready' || item.status === 'reference' ? ' good' : ''), statusLabels()[item.status] || tr('待确认')));
    article.append(header);
    if (item.message) article.append(element('p', '', item.message));
    if (item.next_action) article.append(element('p', 'report-action-text', tr('下一步：') + item.next_action));
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
  if (result.generated_at && !Number.isNaN(Date.parse(result.generated_at))) timestamp = new Date(result.generated_at).toLocaleString(currentLanguage === 'ko' ? 'ko-KR' : 'zh-CN', { hour12: false });
  $('report-meta').textContent = [profileLabels()[result.profile] || profileLabels()[progress.profile], result.move_in_date ? tr('计划入住 ') + result.move_in_date : tr('入住日期未填写'), timestamp ? tr('生成于 ') + timestamp : '', tr('按资料规则检查 · 无需AI')].filter(Boolean).join(' · ');
  $('report-section').hidden = false;
}

async function generateReport() {
  const button = $('check-button');
  const revision = formRevision;
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = tr('正在检查…');
  const payload = { profile: progress.profile, move_in_date: progress.move_in_date, states: { ...progress.states }, dates: { ...progress.dates }, language: currentLanguage };
  try {
    const result = await request('/api/check', payload);
    if (epoch !== sessionEpoch) return;
    if (!result || !Array.isArray(result.items) || !result.summary) throw new Error(tr('检查结果格式不完整，未替换上一次报告。'));
    report = result; renderReport(result);
    $('report-stale').hidden = revision === formRevision;
    saveProgress();
    $('report-section').focus({ preventScroll: true });
    $('report-section').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    announce(tr(revision === formRevision ? '行动清单已生成，每项均可查看依据。' : '已生成报告，但输入刚刚变化，请重新生成。'));
  } catch (error) { announce(`${error.message} ${tr('表单内容已保留。')}`, true); }
  finally { button.disabled = !catalog; button.textContent = tr('生成行动清单') + ' →'; }
}

async function askQuestion(event) {
  event.preventDefault();
  const question = $('question').value.trim();
  if (!question) { $('question').focus(); return; }
  const button = $('ask-button');
  const epoch = sessionEpoch;
  button.disabled = true; button.textContent = tr('查询中…');
  const panel = $('answer-panel'); panel.hidden = false;
  panel.replaceChildren(element('p', 'answer-label', tr('正在根据收录资料查找依据…')));
  try {
    const result = await request('/api/ask', { question, language: currentLanguage });
    if (epoch !== sessionEpoch || question !== $('question').value.trim()) { panel.hidden = true; return; }
    if (!result || typeof result.answer !== 'string') throw new Error(tr('未收到有效回答，请查看原文或稍后重试。'));
    panel.replaceChildren(element('p', 'answer-label', tr('根据收录资料回答')), element('p', 'answer-text', result.answer));
    if (result.notice) panel.append(element('p', 'answer-notice', result.notice));
    const evidence = Array.isArray(result.evidence) ? result.evidence : [];
    if (evidence.length) {
      const evidencePanel = element('div', 'answer-evidence');
      evidencePanel.append(element('p', 'answer-label', tr('回答依据')));
      evidence.forEach(entry => {
        const item = itemById(entry.item_id) || {};
        const source = sourceById(entry.source_id) || {};
        const block = element('div', 'evidence-content');
        if (entry.quote) block.append(element('blockquote', '', entry.quote));
        block.append(externalLink(sourceTitle(source) || tr('打开原始资料 ↗'), source.url || item.source_url));
        evidencePanel.append(block);
      });
      panel.append(evidencePanel);
    } else {
      panel.append(element('p', 'answer-notice', tr('本次回答没有返回可展示的原文依据。请查看资料原文或向宿舍确认，勿据此视为已核实。')));
    }
  } catch (error) {
    if (epoch !== sessionEpoch) return;
    panel.replaceChildren(element('p', 'answer-notice', `${error.message} ${tr('问题已保留。你仍可查看来源原文，或使用无需AI的手动检查。')}`));
  } finally { button.textContent = tr('查规则'); button.disabled = !health.ai_configured; }
}

function exportReport() {
  if (!report) return;
  const blob = new Blob([JSON.stringify({ exported_at: new Date().toISOString(), language: currentLanguage, report_is_stale: !$('report-stale').hidden, catalog_verified_date: catalog?.verified_date, report }, null, 2)], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = element('a'); link.href = url; link.download = `move-in-ready-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  announce(tr('行动清单已导出为JSON。'));
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
  $('save-status').textContent = tr(storageCleared ? '已清空 · 进度仅在本浏览器' : '页面已清空，但本地记录移除失败'); renderChecklist();
  $('clear-dialog').close(); announce(tr(storageCleared ? '准备记录已清空。' : '当前页面已清空，但浏览器存储未允许移除记录；刷新后可能恢复旧记录。'), !storageCleared); $('profile').focus();
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
    if (!data || !Array.isArray(data.items) || !Array.isArray(data.sources) || !data.items.length) throw new Error(tr('资料清单不完整，请检查本地服务提供的catalog。'));
    catalog = data;
    readSaved();
    $('profile').value = progress.profile; $('move-in-date').value = progress.move_in_date; $('preparation-text').value = progress.preparation_text;
    renderChecklist(); renderSources();
    $('check-button').disabled = false;
  } catch (error) {
    catalog = null; $('load-error').hidden = false; $('load-error-message').textContent = error.message || tr('请确认本地服务已启动。');
    $('checklist').replaceChildren(element('p', 'empty-note', tr('需要先成功读取资料，才能核对准备事项。')));
    $('item-count').textContent = tr('资料未加载'); $('verified-note').textContent = tr('资料暂未读取成功'); $('check-button').disabled = true;
  } finally {
    renderHealth();
    if (results[1].status === 'rejected') $('interpret-mode').textContent = tr('AI配置状态暂时无法读取。手动核对可用，可重新读取资料后再试AI。');
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
document.querySelectorAll('[data-language]').forEach(button => button.addEventListener('click', () => changeLanguage(button.dataset.language)));
currentLanguage = readLanguage();
renderStaticLanguage();
boot();
