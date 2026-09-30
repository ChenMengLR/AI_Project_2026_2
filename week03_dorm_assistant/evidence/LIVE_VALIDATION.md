# 真实 API 与合成情境验证

执行时间（UTC）：2026-09-30T14:31:59.794255+00:00
模型：qwen3.8-flash；自动检查：14/14。

这些是工程测试，未开展真实用户测试；不能解释成用户效果或通用准确率。

## CHECK_NORMAL — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "standard",
    "move_in_date": "2026-11-01",
    "states": {
      "DOC_TB": "ready",
      "SUPPLY_BEDDING": "ready"
    },
    "dates": {
      "DOC_TB": "2026-09-30"
    }
  },
  "expected": {
    "item_id": "DOC_TB",
    "status": "ready"
  },
  "actual": {
    "profile": "standard",
    "move_in_date": "2026-11-01",
    "generated_at": "2026-09-30T14:31:43.415229+00:00",
    "summary": {
      "ready": 2,
      "missing": 0,
      "unknown": 7,
      "needs_confirmation": 0,
      "total": 9
    },
    "overall": "needs_action",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "ready",
        "status": "ready",
        "message": "你已标记完成；日期处于一般说明的 3 个日历月范围内。",
        "next_action": "携带要求的材料；真实性和具体适用条件仍由学校确认。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "ready",
        "status": "ready",
        "message": "你已标记准备完成；这不是材料真实性或入住资格审核。",
        "next_action": "入住前再次核对官方最新通知。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## CHECK_MISSING — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "standard",
    "states": {
      "SUPPLY_BEDDING": "missing"
    }
  },
  "expected": {
    "item_id": "SUPPLY_BEDDING",
    "status": "missing"
  },
  "actual": {
    "profile": "standard",
    "move_in_date": "",
    "generated_at": "2026-09-30T14:31:43.415278+00:00",
    "summary": {
      "ready": 0,
      "missing": 1,
      "unknown": 8,
      "needs_confirmation": 0,
      "total": 9
    },
    "overall": "needs_action",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "missing",
        "status": "missing",
        "message": "你已标记尚未准备。",
        "next_action": "按原文确认适用要求后完成准备。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## CHECK_AMBIGUOUS — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "standard",
    "states": {
      "SUPPLY_BEDDING": "unknown"
    }
  },
  "expected": {
    "item_id": "SUPPLY_BEDDING",
    "status": "unknown"
  },
  "actual": {
    "profile": "standard",
    "move_in_date": "",
    "generated_at": "2026-09-30T14:31:43.415300+00:00",
    "summary": {
      "ready": 0,
      "missing": 0,
      "unknown": 9,
      "needs_confirmation": 0,
      "total": 9
    },
    "overall": "needs_action",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## CHECK_INTERNATIONAL — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "international",
    "states": {
      "DOC_ADDRESS": "ready"
    }
  },
  "expected": {
    "item_id": "DOC_ADDRESS",
    "status": "confirm"
  },
  "actual": {
    "profile": "international",
    "move_in_date": "",
    "generated_at": "2026-09-30T14:31:43.415330+00:00",
    "summary": {
      "ready": 0,
      "missing": 0,
      "unknown": 7,
      "needs_confirmation": 2,
      "total": 9
    },
    "overall": "scope_unconfirmed",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "confirm",
        "message": "现有公开资料不足以确认这项要求适用于你的身份。",
        "next_action": "向生活馆或国际事务部门确认适用要求；勿将一般说明直接视为个人结论。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "ready",
        "status": "confirm",
        "message": "现有公开资料不足以确认这项要求适用于你的身份。",
        "next_action": "向生活馆或国际事务部门确认适用要求；勿将一般说明直接视为个人结论。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## CHECK_OLD_DATE — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "standard",
    "move_in_date": "2026-11-01",
    "states": {
      "DOC_TB": "ready"
    },
    "dates": {
      "DOC_TB": "2026-07-01"
    }
  },
  "expected": {
    "item_id": "DOC_TB",
    "status": "invalid_date"
  },
  "actual": {
    "profile": "standard",
    "move_in_date": "2026-11-01",
    "generated_at": "2026-09-30T14:31:43.415359+00:00",
    "summary": {
      "ready": 0,
      "missing": 0,
      "unknown": 8,
      "needs_confirmation": 1,
      "total": 9
    },
    "overall": "needs_action",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "ready",
        "status": "invalid_date",
        "message": "按填写日期，材料超出一般入住说明的 3 个日历月范围。",
        "next_action": "核对原文及最新通知，确认是否需要更新材料。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## CHECK_MISSING_DATE — 通过

类型：deterministic_synthetic

```json
{
  "input": {
    "profile": "standard",
    "states": {
      "DOC_TB": "ready"
    }
  },
  "expected": {
    "item_id": "DOC_TB",
    "status": "confirm"
  },
  "actual": {
    "profile": "standard",
    "move_in_date": "",
    "generated_at": "2026-09-30T14:31:43.415379+00:00",
    "summary": {
      "ready": 0,
      "missing": 0,
      "unknown": 8,
      "needs_confirmation": 1,
      "total": 9
    },
    "overall": "needs_action",
    "items": [
      {
        "id": "DOC_TB",
        "category": "document",
        "title_zh": "准备结核检查证明",
        "title_ko": "결핵검진 확인서",
        "requirement": "required",
        "description_zh": "一般说明要求结核检查证明，可用健康证明或兵役体检结果通知书替代。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "材料种类和替代材料对国际生或对象不明者须先确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "ready",
        "status": "confirm",
        "message": "缺少入住日期或材料出具日期，暂不能核对日期范围。",
        "next_action": "补充日期，或向生活馆确认后再核对。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_ADDRESS",
        "category": "document",
        "title_zh": "准备居民登记誊本",
        "title_ko": "주민등록등본",
        "requirement": "required",
        "description_zh": "一般说明列居民登记誊本；核对家长地址后返还。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未找到护照、外国人登记证等替代材料的适用依据。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": true,
        "valid_months": 3,
        "checkable": true,
        "privacy": {
          "collect": "status_and_issue_date_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_RECENCY",
        "category": "rule",
        "title_zh": "核对材料开具时间",
        "title_ko": "서류 발급 시점",
        "requirement": "required",
        "description_zh": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "适用对象先确认；边界日期算法是教学辅助，学校最终核定。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "confirmation_required",
          "unknown": "confirmation_required"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "quote_kind": "short_original_excerpt",
        "source_locator": "1) 입사 전 서류 준비 标题",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": 3,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "上述入住前材料需为入住日起三个月以内开具的版本。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "CHECKIN_OFFICE",
        "category": "step",
        "title_zh": "到行政支援室办理入住",
        "title_ko": "행정지원실 방문",
        "requirement": "required",
        "description_zh": "正常入住期间，在09:00–17:00到行政支援室办理。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅指正常入住期间，不能据此判断任意日期可入住。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (1)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "DOC_LATE_SUBMISSION",
        "category": "rule",
        "title_zh": "缺材料时确认补交安排",
        "title_ko": "서류 제출",
        "requirement": "information",
        "description_zh": "一般说明允许未带材料先入住，但须在一周内补交。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不能据此批准个人或留学生延期；先联系所属馆。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "일주일 이내로 제출 필요",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明允许未带材料先入住，但须在一周内补交。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_NOTICE",
        "category": "rule",
        "title_zh": "留意分配房间短信",
        "title_ko": "호실 안내",
        "requirement": "information",
        "description_zh": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这里不查询个人房号，也不能保证个人收到短信的时间。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "문자 발송",
        "quote_kind": "short_original_excerpt",
        "source_locator": "2) 입사 당일 (3)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "一般说明在正常入住日前一天，向学生手机发送房间通知。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_HYGIENE",
        "category": "supply",
        "title_zh": "准备洗漱和日用物品",
        "title_ko": "위생용품 준비",
        "requirement": "recommended",
        "description_zh": "按个人需要备洗发用品、牙刷牙膏、毛巾、纸巾等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "这是官网个人准备物品的教学清单，不判断学校强制购买。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "위생용품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (1)、(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_BEDDING",
        "category": "supply",
        "title_zh": "准备合适季节的床品",
        "title_ko": "침구류 준비",
        "requirement": "recommended",
        "description_zh": "准备适合夏季或冬季的床品。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未据此判断具体床尺寸、学校提供或租赁情况。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "침구류",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (2)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_LAUNDRY",
        "category": "supply",
        "title_zh": "准备衣物洗护用品",
        "title_ko": "세탁용품 준비",
        "requirement": "recommended",
        "description_zh": "可备衣架、晾衣架和洗涤剂；共用洗衣机、烘干机付费使用。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "未公开本页机器价格；胶囊、液体、粉末洗涤剂均列为可用。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "유료로 이용",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (3)、(4)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "SUPPLY_NETWORK",
        "category": "supply",
        "title_zh": "按需准备网络用品",
        "title_ko": "인터넷용품 준비",
        "requirement": "recommended",
        "description_zh": "个人用品列表列有路由器和网线，可按实际需要准备。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "不保证房内已装Wi-Fi或某型号兼容。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "공유기, 랜선",
        "quote_kind": "short_original_excerpt",
        "source_locator": "3) 개인 준비물 (6)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "PROHIBITED_ITEMS",
        "category": "rule",
        "title_zh": "检查禁带用品",
        "title_ko": "반입금지 물품",
        "requirement": "prohibited",
        "description_zh": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "举例并非完整禁带清单，打包前打开原文核对。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 (1)–(5)",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "禁带电热毯、取暖器、电饭锅、电热水壶、冰箱、火源危险品及酒类等。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "HEALTH_ITEM_INQUIRY",
        "category": "rule",
        "title_zh": "特殊健康用途物品先询问",
        "title_ko": "사전 문의",
        "requirement": "required",
        "description_zh": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅在需要此类物品时适用；询问不等于已获许可。此项仅作条件提醒，不计完成率。",
          "trigger": "health_related_item_needed"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "quote_kind": "short_original_excerpt",
        "source_locator": "4) 반입금지 물품 最后注释",
        "source_url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "state": "unknown",
        "status": "reference",
        "message": "因健康原因需要使用相关物品时，先向行政支援室询问。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_MOVEIN",
          "title": "한림생활관 입/퇴사 안내（翰林生活馆入住/退宿说明）",
          "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
          "verified_date": "2026-09-30",
          "scope": "一般公开入住说明；页面未显示具体适用学期或发布日期；不证明留学生材料或个人入住资格。"
        }
      },
      {
        "id": "ROOM_ASSIGNMENT",
        "category": "rule",
        "title_zh": "不要自行调换分配房间",
        "title_ko": "호실 배정",
        "requirement": "prohibited",
        "description_zh": "按学校分配入住，住宿生之间不能自行换房。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅适用翰林生活馆，调换需求先走官方确认。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "임의로 변경할 수 없다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제9조(호실 배정)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": false,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "reference",
        "message": "按学校分配入住，住宿生之间不能自行换房。",
        "next_action": "阅读适用条件及官方原文。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "ACCESS_CARD",
        "category": "step",
        "title_zh": "领取并妥善携带出入证",
        "title_ko": "출입증",
        "requirement": "required",
        "description_zh": "入住办理时领取出入证；在馆内佩戴，工作人员要求时出示。",
        "conditions": {
          "stage": "move_in_day",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "仅记录是否完成，不保存出入证号码或照片。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "출입증을 항상 패용하여야 하며",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제10조(출입증)；入住说明 2)(3)",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "additional_source_ids": [
          "HANLIM_MOVEIN"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      },
      {
        "id": "NOTICE_REVIEW",
        "category": "step",
        "title_zh": "阅读所属馆最新公告",
        "title_ko": "공고 확인",
        "requirement": "required",
        "description_zh": "入住前检查所属馆公告，了解实际批次与办理安排。",
        "conditions": {
          "stage": "before_move_in",
          "student_types": [
            "standard",
            "international",
            "unknown"
          ],
          "location": "Hanlim only",
          "notes_zh": "公告阅读义务来自守则；将其放在入住前是本工具的安排建议。"
        },
        "applicability": {
          "standard": "general_guidance",
          "international": "reference",
          "unknown": "reference"
        },
        "source_id": "HANLIM_RULES_DMS",
        "quote": "공고 내용을 숙지하여야 한다.",
        "quote_kind": "short_original_excerpt",
        "source_locator": "제24조(게시 및 광고물 부착) ①",
        "source_url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
        "verified_date": "2026-09-30",
        "date_field": false,
        "valid_months": null,
        "checkable": true,
        "privacy": {
          "collect": "status_only",
          "upload_allowed": false,
          "do_not_collect": [
            "证件号码",
            "真实证件图片",
            "体检结果",
            "病史",
            "房间密码"
          ]
        },
        "crosscheck_source_ids": [
          "HANLIM_RULES_CURRENT"
        ],
        "state": "unknown",
        "status": "unknown",
        "message": "尚未确认准备状态。",
        "next_action": "阅读来源并确认自己的准备情况。",
        "source": {
          "id": "HANLIM_RULES_DMS",
          "title": "한림생활관 사생수칙（住宿生守则，DMS 站）",
          "url": "https://dms.donga.ac.kr/hanlim/15139/subview.do",
          "verified_date": "2026-09-30",
          "scope": "公开住宿生守则；本版仅使用第9、10、24条，并与现站交叉核对。"
        }
      }
    ],
    "notice": "这是按公开资料和你的自报状态生成的准备检查，不代表官方审核通过。",
    "notes": [
      "未采集证件、体检报告或其他真实材料；只记录准备状态和可选日期。",
      "日期按日历月核对；不同学期、身份或具体通知的要求需单独确认。"
    ]
  },
  "passed": true
}
```

## QA_ANSWER_01 — 通过

类型：real_ai_synthetic_question

```json
{
  "input": "一般入住说明要求准备哪两类材料，开具时间有什么要求？",
  "expected": {
    "id": "QA_ANSWER_01",
    "answerable": true,
    "student_type": "standard",
    "question": "一般入住说明要求准备哪两类材料，开具时间有什么要求？",
    "expected_answer": "结核检查证明和居民登记誊本；按一般说明，入住日起三个月以内开具。",
    "evidence_item_ids": [
      "DOC_TB",
      "DOC_ADDRESS",
      "DOC_RECENCY"
    ],
    "must_qualify": "这是一般说明；留学生和适用对象不明者须先确认。",
    "evidence_ids": [
      "DOC_TB",
      "DOC_ADDRESS",
      "DOC_RECENCY"
    ]
  },
  "actual": {
    "answer": "一般入住说明要求准备结核检查证明（可用健康证明或兵役体检结果通知书替代）和居民登记誊本。上述材料需为入住日起三个月以内开具的版本。\n相关条件（资料中文释义）：上述入住前材料需为入住日起三个月以内开具的版本。",
    "evidence": [
      {
        "item_id": "DOC_TB",
        "source_id": "HANLIM_MOVEIN",
        "quote": "결핵검진 확인서",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "准备结核检查证明"
      },
      {
        "item_id": "DOC_ADDRESS",
        "source_id": "HANLIM_MOVEIN",
        "quote": "주민등록등본",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "准备居民登记誊本"
      },
      {
        "item_id": "DOC_RECENCY",
        "source_id": "HANLIM_MOVEIN",
        "quote": "3개월 이내 발급분",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "核对材料开具时间"
      }
    ],
    "answered": true,
    "mode": "ai",
    "notice": "引用来自已核对的本地资料；引用存在不等于模型解释必然正确，请对照原文。"
  },
  "passed": true,
  "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。",
  "elapsed_seconds": 3.46
}
```

## QA_ANSWER_02 — 通过

类型：real_ai_synthetic_question

```json
{
  "input": "正常入住期间应该在几点到哪里办理入住？",
  "expected": {
    "id": "QA_ANSWER_02",
    "answerable": true,
    "student_type": "standard",
    "question": "正常入住期间应该在几点到哪里办理入住？",
    "expected_answer": "正常入住期间09:00–17:00到行政支援室。",
    "evidence_item_ids": [
      "CHECKIN_OFFICE"
    ],
    "must_qualify": "不能用这一时间窗断言某个日期属于正常入住期间。",
    "evidence_ids": [
      "CHECKIN_OFFICE"
    ]
  },
  "actual": {
    "answer": "正常入住期间，请在09:00–17:00到行政支援室办理。",
    "evidence": [
      {
        "item_id": "CHECKIN_OFFICE",
        "source_id": "HANLIM_MOVEIN",
        "quote": "09:00~17:00",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "到行政支援室办理入住"
      }
    ],
    "answered": true,
    "mode": "ai",
    "notice": "引用来自已核对的本地资料；引用存在不等于模型解释必然正确，请对照原文。"
  },
  "passed": true,
  "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。",
  "elapsed_seconds": 2.07
}
```

## QA_ANSWER_03 — 通过

类型：real_ai_synthetic_question

```json
{
  "input": "可以带电热毯和电饭锅吗？",
  "expected": {
    "id": "QA_ANSWER_03",
    "answerable": true,
    "student_type": "standard",
    "question": "可以带电热毯和电饭锅吗？",
    "expected_answer": "一般入住说明将电热毯和电饭锅列为禁带用品。",
    "evidence_item_ids": [
      "PROHIBITED_ITEMS"
    ],
    "must_qualify": "健康原因需使用相关物品，应事先询问行政支援室，不能自行视为获准。",
    "evidence_ids": [
      "PROHIBITED_ITEMS"
    ]
  },
  "actual": {
    "answer": "不可以。根据规定，电热毯和电饭锅属于禁止携带物品。\n相关条件（资料中文释义）：因健康原因需要使用相关物品时，先向行政支援室询问。",
    "evidence": [
      {
        "item_id": "PROHIBITED_ITEMS",
        "source_id": "HANLIM_MOVEIN",
        "quote": "반입금지 물품",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "检查禁带用品"
      },
      {
        "item_id": "HEALTH_ITEM_INQUIRY",
        "source_id": "HANLIM_MOVEIN",
        "quote": "사전 문의",
        "url": "https://hanlim.donga.ac.kr/hanlim/CMS/Contents/Contents.do?mCode=MN075",
        "title": "特殊健康用途物品先询问"
      }
    ],
    "answered": true,
    "mode": "ai",
    "notice": "引用来自已核对的本地资料；引用存在不等于模型解释必然正确，请对照原文。"
  },
  "passed": true,
  "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。",
  "elapsed_seconds": 1.9
}
```

## QA_UNKNOWN_01 — 通过

类型：real_ai_synthetic_question

```json
{
  "input": "我是留学生，可以用护照或外国人登记证代替居民登记誊本吗？",
  "expected": {
    "id": "QA_UNKNOWN_01",
    "answerable": false,
    "student_type": "international",
    "question": "我是留学生，可以用护照或外国人登记证代替居民登记誊本吗？",
    "expected_answer": "当前资料没有说明留学生替代材料，无法确认；请询问所属馆或国际交流部门。",
    "evidence_item_ids": [],
    "must_not_claim": [
      "可以替代",
      "必须提交护照",
      "必须提交外国人登记证"
    ],
    "evidence_ids": []
  },
  "actual": {
    "answer": "无法从提供的资料确认。请查看最新官方通知或联系生活馆。",
    "evidence": [],
    "answered": false,
    "mode": "ai",
    "notice": "资料未覆盖该问题，未生成推测结论。"
  },
  "passed": true,
  "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。",
  "elapsed_seconds": 1.43
}
```

## QA_UNKNOWN_02 — 通过

类型：real_ai_synthetic_question

```json
{
  "input": "我2026年10月5日可以入住吗，我被分到哪个房间？",
  "expected": {
    "id": "QA_UNKNOWN_02",
    "answerable": false,
    "student_type": "unknown",
    "question": "我2026年10月5日可以入住吗，我被分到哪个房间？",
    "expected_answer": "现有资料未给这个人的入住批次或房号，无法确认；请查个人通知并联系所属馆。",
    "evidence_item_ids": [],
    "must_not_claim": [
      "10月5日可以入住",
      "具体房号",
      "已核实本人资格"
    ],
    "evidence_ids": []
  },
  "actual": {
    "answer": "无法从提供的资料确认。请查看最新官方通知或联系生活馆。",
    "evidence": [],
    "answered": false,
    "mode": "ai",
    "notice": "资料未覆盖该问题，未生成推测结论。"
  },
  "passed": true,
  "check_scope": "回答/拒答状态及必要引用ID；完整语义仍需人工核对。",
  "elapsed_seconds": 1.2
}
```

## AI_PREP_CLEAR — 通过

类型：real_ai_synthetic_preparation

```json
{
  "input": "我的床上用品和洗漱用品已经准备好了，洗衣液还没买。",
  "expected": {
    "SUPPLY_BEDDING": "ready",
    "SUPPLY_HYGIENE": "ready",
    "SUPPLY_LAUNDRY": "missing"
  },
  "actual": {
    "suggestions": [
      {
        "item_id": "SUPPLY_BEDDING",
        "state": "ready",
        "reason": "用户明确表述“床上用品...已经准备好了”"
      },
      {
        "item_id": "SUPPLY_HYGIENE",
        "state": "ready",
        "reason": "用户明确表述“洗漱用品已经准备好了”"
      },
      {
        "item_id": "SUPPLY_LAUNDRY",
        "state": "missing",
        "reason": "用户明确表述“洗衣液还没买”，属于衣物洗护用品的一部分"
      }
    ],
    "notices": [
      "这是 AI 理解的建议，请逐项确认后应用。"
    ],
    "mode": "ai"
  },
  "passed": true,
  "check_scope": "提取项目及状态精确一致；未经用户确认不应用。",
  "elapsed_seconds": 2.73
}
```

## AI_PREP_AMBIGUOUS — 通过

类型：real_ai_synthetic_preparation

```json
{
  "input": "我不确定床上用品准备好了没有。",
  "expected": {
    "SUPPLY_BEDDING": "unknown"
  },
  "actual": {
    "suggestions": [
      {
        "item_id": "SUPPLY_BEDDING",
        "state": "unknown",
        "reason": "用户表述含糊，称不确定是否准备好"
      }
    ],
    "notices": [
      "这是 AI 理解的建议，请逐项确认后应用。"
    ],
    "mode": "ai"
  },
  "passed": true,
  "check_scope": "提取项目及状态精确一致；未经用户确认不应用。",
  "elapsed_seconds": 2.01
}
```

## AI_PREP_CONTRADICTION — 通过

类型：real_ai_synthetic_preparation

```json
{
  "input": "床上用品我已经准备好了。但刚才说错了，我还没有准备床上用品。",
  "expected": {
    "SUPPLY_BEDDING": "unknown"
  },
  "actual": {
    "suggestions": [
      {
        "item_id": "SUPPLY_BEDDING",
        "state": "unknown",
        "reason": "用户先称已准备好，随后更正说没有准备，表述互相矛盾"
      }
    ],
    "notices": [
      "这是 AI 理解的建议，请逐项确认后应用。"
    ],
    "mode": "ai"
  },
  "passed": true,
  "check_scope": "提取项目及状态精确一致；未经用户确认不应用。",
  "elapsed_seconds": 1.57
}
```
