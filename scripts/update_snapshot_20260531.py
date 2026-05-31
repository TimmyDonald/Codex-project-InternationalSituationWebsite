#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "international-situation.json"
ACCESSED_AT = "2026-05-31"


def upsert_source(sources: list[dict], source: dict) -> None:
    for index, existing in enumerate(sources):
        if existing.get("id") == source["id"]:
            sources[index] = source
            return
    sources.append(source)


def main() -> int:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    sources = [
        {
            "id": "europe-ap-patriot-2026-05-28",
            "publisher": "Associated Press",
            "title": "Zelenskyy says he's being 'very persistent' with the US for more Patriot missiles",
            "url": "https://apnews.com/article/russia-ukraine-war-drones-missiles-sweden-63efe7b5482de04a4fda9884f3bf7ebe",
            "published_at": "2026-05-28",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对乌克兰对美国 Patriot 防空弹药的最新公开诉求，以及俄罗斯弹道导弹压力。",
        },
        {
            "id": "europe-reuters-attack-2026-05-29",
            "publisher": "Reuters via Investing.com",
            "title": "Zelenskiy says Russia is preparing major new attack on Ukraine",
            "url": "https://www.investing.com/news/world-news/zelenskiy-says-russia-is-preparing-major-new-attack-on-ukraine-4717118",
            "published_at": "2026-05-29",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对乌克兰方面关于俄罗斯准备新一轮大规模打击的最新说法。",
        },
        {
            "id": "middle-ap-iran-strikes-2026-05-25",
            "publisher": "Associated Press",
            "title": "US military says it carried out 'self-defense' strikes in Iran, including on missile launch sites",
            "url": "https://apnews.com/article/iran-deal-trump-israel-abrams-01a13e9a63ece786a0a7fa4933dbf09b",
            "published_at": "2026-05-25",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对美伊停火谈判期间南伊朗和霍尔木兹方向的军事摩擦。",
        },
        {
            "id": "middle-ap-gaza-yellow-line-2026-05-30",
            "publisher": "Associated Press",
            "title": "Israeli soldiers describe ongoing killings in Gaza despite ceasefire",
            "url": "https://apnews.com/article/gaza-war-yellow-line-israeli-soldiers-8a6cb8e91ba454ddc80a6335e7466451",
            "published_at": "2026-05-30",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对加沙停火下黄线、以军控制区和冲突伤亡争议。",
        },
        {
            "id": "middle-ap-gaza-force-2026-05-28",
            "publisher": "Associated Press",
            "title": "Iran war complicates plans for Gaza international force",
            "url": "https://apnews.com/article/israel-hamas-gaza-trump-indonesia-stabilization-force-a5e1d4a894746104c1335b6962c0ab69",
            "published_at": "2026-05-28",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对加沙国际稳定力量承诺迟滞与停火第二阶段僵局。",
        },
        {
            "id": "middle-ocha-gaza-2026-05-25",
            "publisher": "OCHA OPT",
            "title": "Humanitarian Situation Report | 25 May 2026",
            "url": "https://www.ochaopt.org/content/humanitarian-situation-report-25-may-2026",
            "published_at": "2026-05-25",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对加沙援助准入、燃料入境和人道行动受阻情况。",
        },
        {
            "id": "east-ap-dprk-weapons-2026-05-27",
            "publisher": "Associated Press",
            "title": "North Korea says it tested new warheads, technology and navigation in latest launches",
            "url": "https://apnews.com/article/north-korea-kim-ballistic-cruise-missiles-nuclear-720cea7dfc5f7ec555ff9bb1f423507c",
            "published_at": "2026-05-27",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对朝鲜 5 月下旬多系统武器测试与战术核相关表述。",
        },
        {
            "id": "east-reuters-ph-threat-2026-05-30",
            "publisher": "Reuters via Investing.com",
            "title": "Philippines remains under threat from China despite Trump-Xi summit, minister says",
            "url": "https://www.investing.com/news/world-news/philippines-remains-under-threat-from-china-despite-trumpxi-summit-minister-says-4717757",
            "published_at": "2026-05-30",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对菲律宾防长在香格里拉对话期间对南海威胁和同盟承诺的表述。",
        },
        {
            "id": "east-reuters-taiwan-patrol-2026-05-26",
            "publisher": "Reuters via Investing.com",
            "title": "Taiwan tracks second Chinese 'combat' patrol in a week, sends ships and jets to monitor",
            "url": "https://www.investing.com/news/world-news/taiwan-tracks-second-chinese-combat-patrol-in-a-week-sends-ships-and-jets-to-monitor-4708672",
            "published_at": "2026-05-26",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对台湾周边解放军联合战备警巡频率和台方监控情况。",
        },
        {
            "id": "central-unama-returnees-2026-05-19",
            "publisher": "UNAMA",
            "title": "UN and NGOs launch 529 million USD response plan for 2.7 million Afghan returnees from Iran and Pakistan",
            "url": "https://unama.unmissions.org/en/news/un-and-ngos-launch-529-million-usd-response-plan-for-27-million-afghan-returnees-from",
            "published_at": "2026-05-19",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对阿富汗回返潮、边境援助和中亚外溢压力。",
        },
        {
            "id": "central-unama-decree-2026-05-21",
            "publisher": "UNAMA",
            "title": "UNAMA Statement on Afghanistan's De Facto Authorities' Decree No. 18 'Code on Judicial Separation of Spouses'",
            "url": "https://unama.unmissions.org/en/news/unama-statement-on-afghanistans-de-facto-authorities-decree-no-18-code-on-judicial",
            "published_at": "2026-05-21",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对阿富汗女性和儿童权利受限对治理风险的影响。",
        },
        {
            "id": "central-unama-journalists-2026-05-14",
            "publisher": "UNAMA",
            "title": "UNAMA expresses concern over detention of journalists in Afghanistan",
            "url": "https://unama.unmissions.org/en/news/unama-expresses-concern-over-detention-journalists-afghanistan",
            "published_at": "2026-05-14",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对阿富汗媒体环境和治理约束。",
        },
        {
            "id": "central-unrcca-mun-2026-05-08",
            "publisher": "UNRCCA",
            "title": "Youth from Central Asia and Afghanistan Convene for Model United Nations Conference",
            "url": "https://unrcca.unmissions.org/en/node/135350",
            "published_at": "2026-05-08",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对中亚和阿富汗青年预防外交、气候与新技术议题。",
        },
        {
            "id": "north-ap-haiti-landau-2026-05-30",
            "publisher": "Associated Press",
            "title": "Senior US diplomat holds talks with Haiti, Dominican Republic on security, economy",
            "url": "https://apnews.com/article/haiti-dominican-republic-landau-visit-gangs-4aba5a24664de1e22badaa23b9bb8a1f",
            "published_at": "2026-05-30",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对美国副国务卿访问海地和多米尼加共和国期间的安全议题。",
        },
        {
            "id": "north-state-haiti-advisory-2026-04-16",
            "publisher": "U.S. Department of State",
            "title": "Haiti Travel Advisory",
            "url": "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/haiti-travel-advisory.html?os=av..",
            "published_at": "2026-04-16",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对美国官方对海地犯罪、绑架、动荡和政府旅行限制的背景判断。",
        },
        {
            "id": "south-ap-guyana-venezuela-2026-05-30",
            "publisher": "Associated Press",
            "title": "Guyanese soldier wounded in gunfight along Venezuela border",
            "url": "https://apnews.com/article/guyana-venezuela-border-shooting-dispute-c7374bf70f8eeb2b46c88cf6e5473f1b",
            "published_at": "2026-05-30",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对圭亚那-委内瑞拉边境交火和埃塞奎博争端背景。",
        },
        {
            "id": "south-ap-brazil-gangs-2026-05-28",
            "publisher": "Associated Press",
            "title": "US government labels Brazil's 2 biggest drug gangs as foreign terrorist organizations",
            "url": "https://apnews.com/article/brazil-pcc-comando-vermelho-foreign-terrorist-organizations-trump-68fe261fa5ab6980864405345970f68f",
            "published_at": "2026-05-28",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对美国对巴西 PCC 和 CV 的恐怖组织指定及巴西政府反应。",
        },
        {
            "id": "south-ap-brazil-operation-2026-05-28",
            "publisher": "Associated Press",
            "title": "Brazil prosecutors target gangs with mega-operation against fraud and money laundering",
            "url": "https://apnews.com/article/brazil-crime-money-laundering-acdda80e981188177be806a1e8776c26",
            "published_at": "2026-05-28",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对巴西国内针对犯罪集团金融网络的执法行动。",
        },
        {
            "id": "south-ap-colombia-election-2026-05-25",
            "publisher": "Associated Press",
            "title": "Safety concerns loom as Colombians vote for a new president",
            "url": "https://apnews.com/article/colombia-election-violence-drones-63d0fcb7d34fca4c92cd1338bec40dd1",
            "published_at": "2026-05-25",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对哥伦比亚大选期间无人机袭击和地方安全担忧。",
        },
        {
            "id": "south-ap-ecuador-security-2026-05-24",
            "publisher": "Associated Press",
            "title": "Ecuador's president Noboa touts US-backed crime-fighting efforts",
            "url": "https://apnews.com/article/ecuador-president-noboa-crime-drug-trafficking-us-b599e99a44297973bc0cfcadbc2d2072",
            "published_at": "2026-05-24",
            "accessed_at": ACCESSED_AT,
            "note": "用于核对厄瓜多尔政府治安军事化、引渡和反毒品行动背景。",
        },
    ]
    for source in sources:
        upsert_source(data["sources"], source)

    data["generated_at"] = "2026-05-31T00:00:00Z"
    data["site"]["snapshot_date"] = "2026-05-31"
    data["site"]["update_process"] = (
        "先人工核验来源，再只修改 data/international-situation.json，最后运行构建与校验脚本生成 data/site.js。"
        "2026 年 5 月 31 日版本优先补入 5 月 19 日至 30 日的新条目，并保留仍有背景价值的早前来源。"
    )

    data["global_overview"] = {
        "headline": "截至 2026 年 5 月 31 日，全球风险主轴转向三条并行线：美伊与霍尔木兹摩擦、加沙停火执行僵局，以及乌克兰防空缺口和俄方新一轮打击预警。",
        "dek": "本轮快照把 2026 年 5 月 19 日至 30 日的新来源前置：中东同时出现美军在伊朗的“自卫”打击、加沙黄线争议和国际稳定力量迟滞；欧洲围绕 Patriot 防空弹药和俄罗斯大规模打击预警继续升压；东亚由南海同盟威慑、台湾周边战备警巡和朝鲜多系统武器测试构成安全信号；中亚侧重阿富汗回返潮、人权限制和预防外交；北美聚焦海地安全和美加墨规则背景；南美则由圭委边境、巴西犯罪集团指定和哥伦比亚选举安全共同牵引。",
        "last_updated_label": "快照时间：2026 年 5 月 31 日",
        "summary_points": [
            "中东最敏感的变化集中在 5 月 25 日美军对伊朗目标的“自卫”打击、霍尔木兹能源通道压力，以及加沙停火下黄线和稳定力量执行僵局。",
            "欧洲的新焦点是乌克兰持续向美国争取 Patriot 防空弹药，同时警告俄罗斯可能准备新一轮大规模打击。",
            "东亚在 5 月下旬同时出现菲律宾对南海威胁的公开表述、台湾周边第二次一周内战备警巡，以及朝鲜多系统武器测试。",
            "中亚烈度仍低于欧洲和中东，但阿富汗回返潮、女性与儿童权利限制和媒体环境收紧使治理风险更突出。",
            "北美安全压力主要外溢到海地：美国高级外交官访问海地和多米尼加共和国时，海地警方仍在阿蒂博尼特与武装团伙交火。",
            "南美的新近压力来自圭亚那-委内瑞拉边境交火、美国对巴西两大犯罪集团的恐怖组织指定，以及哥伦比亚大选前无人机袭击担忧。",
        ],
        "snapshot_note": "本页不是自动抓取后直接发布，而是按来源核验后的结构化快照。2026 年 5 月 31 日版本优先补入 5 月 19 日至 30 日的新条目；对仍在变化的冲突、制裁和安全部署，页面使用“快照”而非预测表述。",
        "source_groups": [
            {
                "label": "一手机构来源",
                "description": "联合国、OCHA、UNAMA、UNRCCA、美国国务院等，用于核对官方立场、人道数据、旅行警示和制度性更新。",
            },
            {
                "label": "通讯社与主流媒体",
                "description": "AP 与 Reuters 用于补充 5 月下旬的现场动态、军事行动、外交访问和选举安全事件。",
            },
            {
                "label": "背景来源",
                "description": "保留 4 月仍有解释价值的军援、贸易和地区安全来源，只作为背景，不替代本轮最新事件来源。",
            },
        ],
        "hotspots": [
            {
                "name": "美伊、霍尔木兹与加沙停火执行",
                "region_id": "middle-east",
                "status": "军事摩擦和停火治理同步承压",
                "summary": "AP 5 月 25 日记录美军在南伊朗实施“自卫”打击，5 月 28 日至 30 日又显示加沙稳定力量迟滞和黄线伤亡争议仍未解决。",
                "risk_level": "high",
                "sources": ["middle-ap-iran-strikes-2026-05-25", "middle-ap-gaza-force-2026-05-28", "middle-ap-gaza-yellow-line-2026-05-30"],
            },
            {
                "name": "乌克兰防空缺口与俄方打击预警",
                "region_id": "europe",
                "status": "战场防空和外交降温均不足",
                "summary": "AP 5 月 28 日显示乌克兰继续向美国争取 Patriot 弹药；Reuters 5 月 29 日报道称泽连斯基称俄罗斯正准备新一轮大规模打击。",
                "risk_level": "high",
                "sources": ["europe-ap-patriot-2026-05-28", "europe-reuters-attack-2026-05-29"],
            },
            {
                "name": "南海、台海与朝鲜半岛联动升压",
                "region_id": "east-asia",
                "status": "同盟威慑与朝鲜武器测试并行",
                "summary": "菲律宾防长 5 月 30 日称菲方仍面临中国“严重威胁”；台湾 5 月 26 日监控一周内第二次解放军战备警巡；朝鲜同日测试多系统武器。",
                "risk_level": "high",
                "sources": ["east-reuters-ph-threat-2026-05-30", "east-reuters-taiwan-patrol-2026-05-26", "east-ap-dprk-weapons-2026-05-27"],
            },
            {
                "name": "阿富汗回返潮与治理约束",
                "region_id": "central-asia",
                "status": "人道和权利压力向区域外溢",
                "summary": "UNAMA 5 月 19 日称阿富汗回返应对计划面向 270 万回返者，5 月 21 日又警告新的婚姻分离规则加深女性和儿童权利限制。",
                "risk_level": "medium",
                "sources": ["central-unama-returnees-2026-05-19", "central-unama-decree-2026-05-21"],
            },
            {
                "name": "海地安全和加勒比边境协作",
                "region_id": "north-america",
                "status": "国际支援和本地治安压力并存",
                "summary": "AP 5 月 30 日记录美国副国务卿访问海地和多米尼加共和国期间，海地警方仍在阿蒂博尼特对武装团伙展开行动并出现伤亡。",
                "risk_level": "high",
                "sources": ["north-ap-haiti-landau-2026-05-30", "north-state-haiti-advisory-2026-04-16"],
            },
            {
                "name": "南美边境、选举和跨国犯罪压力",
                "region_id": "south-america",
                "status": "安全议题进入外交和选举周期",
                "summary": "AP 5 月 30 日记录圭亚那士兵在委内瑞拉边境交火中受伤；美国 5 月 28 日宣布将巴西 PCC 和 CV 指定为外国恐怖组织，哥伦比亚大选前也有无人机袭击担忧。",
                "risk_level": "high",
                "sources": ["south-ap-guyana-venezuela-2026-05-30", "south-ap-brazil-gangs-2026-05-28", "south-ap-colombia-election-2026-05-25"],
            },
        ],
        "latest_developments": [
            {
                "date": "2026-05-30",
                "region_id": "north-america",
                "title": "美国高级外交官访问海地和多米尼加共和国，安全议题置于优先位置",
                "summary": "AP 记录，访问期间美方会见海地总理、警方和联合国支持的反帮派力量；同日海地阿蒂博尼特行动出现警员和平民死亡。",
                "tags": ["海地", "加勒比安全"],
                "sources": ["north-ap-haiti-landau-2026-05-30"],
            },
            {
                "date": "2026-05-30",
                "region_id": "middle-east",
                "title": "加沙停火黄线争议持续，稳定力量仍未实质部署",
                "summary": "AP 采访显示以军黄线周边执法仍造成伤亡争议；另据 AP，计划中的加沙国际稳定力量因政治和安全条件迟滞。",
                "tags": ["加沙", "停火", "稳定力量"],
                "sources": ["middle-ap-gaza-yellow-line-2026-05-30", "middle-ap-gaza-force-2026-05-28"],
            },
            {
                "date": "2026-05-30",
                "region_id": "east-asia",
                "title": "菲律宾防长称南海威胁未因中美元首互动而消退",
                "summary": "Reuters 记录，菲律宾防长在香格里拉对话期间强调菲方面对领土和政治压力，并称美国条约承诺未受影响。",
                "tags": ["南海", "菲律宾", "同盟"],
                "sources": ["east-reuters-ph-threat-2026-05-30"],
            },
            {
                "date": "2026-05-30",
                "region_id": "south-america",
                "title": "圭亚那士兵在委内瑞拉边境交火中受伤",
                "summary": "AP 报道称，边境交火使圭委之间围绕埃塞奎博争端的安全风险重新进入显性议程。",
                "tags": ["圭亚那", "委内瑞拉", "边境"],
                "sources": ["south-ap-guyana-venezuela-2026-05-30"],
            },
            {
                "date": "2026-05-29",
                "region_id": "europe",
                "title": "乌克兰称俄罗斯正准备新一轮大规模打击",
                "summary": "Reuters 记录泽连斯基称乌方获得相关情报，乌克兰防空和外交设施保持高度戒备。",
                "tags": ["乌克兰", "俄罗斯", "防空"],
                "sources": ["europe-reuters-attack-2026-05-29"],
            },
            {
                "date": "2026-05-27",
                "region_id": "east-asia",
                "title": "朝鲜称测试新型弹头、巡航导弹和精确导航火箭炮",
                "summary": "AP 记录，朝鲜称金正恩监督了多系统测试，韩国此前检测到朝方发射近程弹道导弹等武器。",
                "tags": ["朝鲜", "导弹", "半岛"],
                "sources": ["east-ap-dprk-weapons-2026-05-27"],
            },
        ],
    }

    regions = {region["id"]: region for region in data["regions"]}
    region_updates = {
        "east-asia": {
            "summary": "东亚在 2026 年 5 月 31 日快照下由南海同盟威慑、台海战备警巡和朝鲜多系统武器测试共同牵引。5 月 30 日菲律宾防长称菲方仍面临中国“严重威胁”；5 月 26 日台湾监控一周内第二次解放军战备警巡；5 月 27 日 AP 记录朝鲜称测试新型弹头、核能力巡航导弹和精确导航火箭炮。",
            "snapshot_note": "本轮东亚更新优先使用 5 月 26 日至 30 日来源，避免把单一演训或单次发射解释为趋势；南海、台海和朝鲜半岛分别保留独立来源。",
            "key_actors": ["中国", "台湾", "日本", "美国", "菲律宾", "朝鲜"],
            "hotspots": [
                {"name": "南海菲中对峙与同盟韧性", "status": "同盟承诺和地区防务合作继续加密", "summary": "菲律宾防长在香格里拉对话期间称菲方仍面临来自中国的领土和政治威胁，并表示美国对菲条约承诺未被中美元首互动或中东战事削弱。", "risk_level": "high", "sources": ["east-reuters-ph-threat-2026-05-30", "east-ap-balikatan-2026-04-20"]},
                {"name": "台湾周边战备警巡", "status": "一周内第二次同类巡航", "summary": "Reuters 5 月 26 日报道称，台湾派舰机监控解放军一周内第二次“联合战备警巡”，并记录台方称周边同时存在飞机、军舰和海警活动。", "risk_level": "high", "sources": ["east-reuters-taiwan-patrol-2026-05-26"]},
                {"name": "朝鲜半岛武器测试", "status": "多系统展示增加前沿压力", "summary": "AP 5 月 27 日记录朝鲜称测试新型战术核相关弹头、核能力巡航导弹和高精度火箭炮，韩国此前检测到朝方近程弹道导弹等发射。", "risk_level": "high", "sources": ["east-ap-dprk-weapons-2026-05-27"]},
            ],
            "latest_developments": [
                {"date": "2026-05-30", "title": "菲律宾防长称菲方仍面临中国“严重威胁”", "summary": "在香格里拉对话期间，菲律宾防长把南海压力与同盟韧性并列为核心安全议题。", "tags": ["南海", "菲律宾", "中国"], "sources": ["east-reuters-ph-threat-2026-05-30"]},
                {"date": "2026-05-27", "title": "朝鲜称测试新型弹头和核能力巡航导弹", "summary": "朝鲜官方称金正恩监督多系统测试，韩国军方此前检测到朝方发射近程弹道导弹等武器。", "tags": ["朝鲜", "导弹"], "sources": ["east-ap-dprk-weapons-2026-05-27"]},
                {"date": "2026-05-26", "title": "台湾监控一周内第二次解放军战备警巡", "summary": "Reuters 记录台方派舰机应对解放军飞机、军舰和海警在周边活动。", "tags": ["台湾", "战备警巡"], "sources": ["east-reuters-taiwan-patrol-2026-05-26"]},
            ],
            "timeline": [
                {"date": "2026-05-30", "title": "菲律宾防长公开强调南海威胁", "summary": "菲律宾在香格里拉对话期间把南海压力、同盟承诺和防务基础设施升级列为核心议题。", "sources": ["east-reuters-ph-threat-2026-05-30"]},
                {"date": "2026-05-27", "title": "朝鲜公布多系统武器测试", "summary": "测试内容包括新型弹头、核能力巡航导弹和精确导航火箭炮。", "sources": ["east-ap-dprk-weapons-2026-05-27"]},
                {"date": "2026-05-26", "title": "台湾监控第二次战备警巡", "summary": "台湾称一周内再次发现解放军联合战备警巡活动。", "sources": ["east-reuters-taiwan-patrol-2026-05-26"]},
            ],
            "sources": ["east-reuters-ph-threat-2026-05-30", "east-ap-dprk-weapons-2026-05-27", "east-reuters-taiwan-patrol-2026-05-26", "east-ap-balikatan-2026-04-20"],
        },
        "central-asia": {
            "summary": "中亚在 2026 年 5 月 31 日快照下仍属于中低烈度风险区，但阿富汗回返潮、权利限制和治理脆弱性更突出。UNAMA 5 月 19 日称联合国与 NGO 为 270 万阿富汗回返者启动 5.29 亿美元计划，5 月 21 日又警告第 18 号法令进一步限制女性和儿童权利；UNRCCA 则继续通过预防外交学院维持区域对话。",
            "snapshot_note": "本轮中亚更新把阿富汗作为主要外溢源处理：回返、权利、媒体和青年预防外交分别承接人道、治理和区域韧性三类信号。",
            "key_actors": ["哈萨克斯坦", "吉尔吉斯斯坦", "塔吉克斯坦", "乌兹别克斯坦", "阿富汗", "巴基斯坦"],
            "hotspots": [
                {"name": "阿富汗回返潮与边境承压", "status": "大规模回返需要持续资金", "summary": "UNAMA 5 月 19 日称 2026 年回返者应对计划面向 270 万预计从伊朗和巴基斯坦返回的阿富汗人，需求覆盖边境救助与社区重返。", "risk_level": "medium", "sources": ["central-unama-returnees-2026-05-19"]},
                {"name": "女性、儿童和媒体权利限制", "status": "治理约束持续累积", "summary": "UNAMA 5 月 21 日称第 18 号法令加深系统性歧视；5 月 14 日另对至少三名记者被拘表达关切。", "risk_level": "medium", "sources": ["central-unama-decree-2026-05-21", "central-unama-journalists-2026-05-14"]},
                {"name": "区域预防外交和青年网络", "status": "低烈度但具长期韧性意义", "summary": "UNRCCA 5 月 8 日记录中亚和阿富汗青年参加模拟联合国，议题包括青年和平安全、气候行动和新兴技术伦理。", "risk_level": "low", "sources": ["central-unrcca-mun-2026-05-08"]},
            ],
            "latest_developments": [
                {"date": "2026-05-21", "title": "UNAMA 警告第 18 号法令加深女性和儿童权利限制", "summary": "UNAMA 称该法令在婚姻分离、儿童婚姻和女性司法可及性方面进一步制度化不平等。", "tags": ["阿富汗", "人权"], "sources": ["central-unama-decree-2026-05-21"]},
                {"date": "2026-05-19", "title": "联合国和 NGO 为 270 万阿富汗回返者启动 5.29 亿美元计划", "summary": "计划覆盖边境紧急救助和 35 个重点地区的中长期重返支持。", "tags": ["阿富汗", "回返", "人道"], "sources": ["central-unama-returnees-2026-05-19"]},
                {"date": "2026-05-08", "title": "中亚和阿富汗青年参加 UNRCCA 预防外交模拟联合国", "summary": "会议聚焦青年参与、气候行动和新技术在冲突预防中的影响。", "tags": ["预防外交", "青年"], "sources": ["central-unrcca-mun-2026-05-08"]},
            ],
            "timeline": [
                {"date": "2026-05-21", "title": "UNAMA 关注第 18 号法令", "summary": "UNAMA 称该法令进一步削弱阿富汗女性和儿童权利。", "sources": ["central-unama-decree-2026-05-21"]},
                {"date": "2026-05-19", "title": "阿富汗回返者应对计划发布", "summary": "联合国和 NGO 启动 5.29 亿美元应对计划。", "sources": ["central-unama-returnees-2026-05-19"]},
                {"date": "2026-05-08", "title": "预防外交学院模拟联合国举行", "summary": "中亚和阿富汗青年围绕和平、安全、气候和新技术议题开展模拟协商。", "sources": ["central-unrcca-mun-2026-05-08"]},
            ],
            "sources": ["central-unama-returnees-2026-05-19", "central-unama-decree-2026-05-21", "central-unama-journalists-2026-05-14", "central-unrcca-mun-2026-05-08"],
        },
        "middle-east": {
            "summary": "中东在 2026 年 5 月 31 日快照下由美伊与霍尔木兹摩擦、加沙停火执行僵局和人道准入共同构成主线。AP 5 月 25 日记录美军在南伊朗实施“自卫”打击；5 月 28 日至 30 日来源显示，加沙国际稳定力量尚未实质部署，黄线周边伤亡和以军控制区争议继续削弱停火可信度；OCHA 5 月 25 日则继续记录援助准入受阻和燃料供应。",
            "snapshot_note": "本轮中东更新把美伊和加沙分开归因：霍尔木兹属于军事与能源通道风险，加沙属于停火治理、人道和外部稳定力量执行风险。",
            "key_actors": ["以色列", "哈马斯", "伊朗", "美国", "黎巴嫩", "联合国"],
            "hotspots": [
                {"name": "美伊停火、南伊朗打击与霍尔木兹", "status": "谈判仍在但军事接触未消失", "summary": "AP 5 月 25 日记录美军称在南伊朗打击导弹发射点和布雷船只，伊朗方向没有明确官方回应，霍尔木兹通道仍被描述为能源市场压力源。", "risk_level": "high", "sources": ["middle-ap-iran-strikes-2026-05-25"]},
                {"name": "加沙黄线与停火执行", "status": "停火边界和交战规则争议持续", "summary": "AP 5 月 30 日报道以军士兵对加沙黄线执法提供罕见说明，双方互指违反停火，黄线附近伤亡仍是争议焦点。", "risk_level": "high", "sources": ["middle-ap-gaza-yellow-line-2026-05-30"]},
                {"name": "加沙稳定力量和人道准入", "status": "外部承诺迟滞，援助仍受通行限制", "summary": "AP 5 月 28 日称计划中的 2 万人国际稳定力量仍未成形；OCHA 5 月 25 日继续记录人道行动受不安全和通行审批限制影响。", "risk_level": "high", "sources": ["middle-ap-gaza-force-2026-05-28", "middle-ocha-gaza-2026-05-25"]},
            ],
            "latest_developments": [
                {"date": "2026-05-30", "title": "AP 记录加沙黄线执法和伤亡争议", "summary": "以军士兵和官方说明显示，停火下黄线周边仍存在高压交战规则和误判风险。", "tags": ["加沙", "停火"], "sources": ["middle-ap-gaza-yellow-line-2026-05-30"]},
                {"date": "2026-05-28", "title": "加沙国际稳定力量承诺迟滞", "summary": "计划中的稳定力量仍无实质部署，停火第二阶段因解除武装和撤军议题陷入僵局。", "tags": ["加沙", "稳定力量"], "sources": ["middle-ap-gaza-force-2026-05-28"]},
                {"date": "2026-05-25", "title": "美军称在南伊朗实施“自卫”打击", "summary": "美国中央司令部称打击对象包括导弹发射点和布雷船只，谈判进程仍伴随军事摩擦。", "tags": ["伊朗", "霍尔木兹"], "sources": ["middle-ap-iran-strikes-2026-05-25"]},
            ],
            "timeline": [
                {"date": "2026-05-30", "title": "加沙黄线争议继续发酵", "summary": "AP 报道显示黄线周边仍有伤亡和交战规则争议。", "sources": ["middle-ap-gaza-yellow-line-2026-05-30"]},
                {"date": "2026-05-28", "title": "加沙稳定力量尚未成形", "summary": "多国承诺迟滞，国际稳定力量等待停火第二阶段条件。", "sources": ["middle-ap-gaza-force-2026-05-28"]},
                {"date": "2026-05-25", "title": "美军打击南伊朗目标", "summary": "美国称行动属于保护驻军的“自卫”打击。", "sources": ["middle-ap-iran-strikes-2026-05-25"]},
                {"date": "2026-05-25", "title": "OCHA 更新加沙人道行动约束", "summary": "人道组织继续报告通行、安全和市场恢复方面的阻碍。", "sources": ["middle-ocha-gaza-2026-05-25"]},
            ],
            "sources": ["middle-ap-iran-strikes-2026-05-25", "middle-ap-gaza-yellow-line-2026-05-30", "middle-ap-gaza-force-2026-05-28", "middle-ocha-gaza-2026-05-25"],
        },
        "europe": {
            "summary": "欧洲在 2026 年 5 月 31 日快照下仍围绕俄乌战争的防空、外部军援和打击升级风险运转。AP 5 月 28 日记录泽连斯基持续向美国争取 Patriot 防空弹药，并称乌克兰缺口因美方库存和中东消耗而更紧；Reuters 5 月 29 日又记录泽连斯基称俄罗斯正准备新一轮大规模打击。",
            "snapshot_note": "本轮欧洲更新聚焦防空和打击预警两个可核验信号；对外交突破不作预测，只保留“停火呼吁”和“升级风险”两类表述。",
            "key_actors": ["乌克兰", "俄罗斯", "欧盟", "美国", "北约", "联合国"],
            "hotspots": [
                {"name": "Patriot 防空弹药和城市防护", "status": "乌克兰公开加压美国补充弹药", "summary": "AP 5 月 28 日记录泽连斯基称乌克兰正在持续向美国争取更多 Patriot 弹药，以应对俄罗斯弹道导弹对城市和电网的打击。", "risk_level": "high", "sources": ["europe-ap-patriot-2026-05-28"]},
                {"name": "俄罗斯大规模打击预警", "status": "乌方称情报显示新一轮打击准备", "summary": "Reuters 5 月 29 日报道称，泽连斯基称俄罗斯正准备大规模打击；俄罗斯此前警告将对基辅目标实施系统性打击。", "risk_level": "high", "sources": ["europe-reuters-attack-2026-05-29"]},
                {"name": "欧洲军援与外交降温窗口", "status": "支援持续但停火仍缺乏落实机制", "summary": "联合国秘书长在 AP 5 月 28 日报道中呼吁立即降级和全面无条件停火，但战场袭击和军援需求仍保持高位。", "risk_level": "medium", "sources": ["europe-ap-patriot-2026-05-28", "europe-consilium-loan-2026-04-23"]},
            ],
            "latest_developments": [
                {"date": "2026-05-29", "title": "泽连斯基称俄罗斯正准备新一轮大规模打击", "summary": "Reuters 记录乌方称防空和其他天空防御力量将全天候应对。", "tags": ["乌克兰", "俄罗斯", "打击预警"], "sources": ["europe-reuters-attack-2026-05-29"]},
                {"date": "2026-05-28", "title": "乌克兰继续向美国争取 Patriot 弹药", "summary": "泽连斯基称乌方已致信美国总统和国会，要求加快防空弹药交付。", "tags": ["Patriot", "军援"], "sources": ["europe-ap-patriot-2026-05-28"]},
                {"date": "2026-05-28", "title": "联合国秘书长呼吁立即降级和全面无条件停火", "summary": "AP 报道称，秘书长在安理会紧急会议中警告当前升级风险可能失控。", "tags": ["联合国", "停火"], "sources": ["europe-ap-patriot-2026-05-28"]},
            ],
            "timeline": [
                {"date": "2026-05-29", "title": "乌方发布俄罗斯打击预警", "summary": "乌克兰称已获得俄罗斯准备大规模打击的情报。", "sources": ["europe-reuters-attack-2026-05-29"]},
                {"date": "2026-05-28", "title": "乌克兰要求更多 Patriot 弹药", "summary": "泽连斯基在瑞典访问期间强调美国需要更快行动。", "sources": ["europe-ap-patriot-2026-05-28"]},
                {"date": "2026-05-28", "title": "联合国警告升级风险", "summary": "联合国秘书长呼吁降级和全面无条件停火。", "sources": ["europe-ap-patriot-2026-05-28"]},
            ],
            "sources": ["europe-ap-patriot-2026-05-28", "europe-reuters-attack-2026-05-29", "europe-consilium-loan-2026-04-23"],
        },
        "north-america": {
            "summary": "北美在 2026 年 5 月 31 日快照下由海地安全、加勒比边境协作和美加墨经贸规则背景共同牵引。AP 5 月 30 日记录美国副国务卿访问海地和多米尼加共和国，并会见海地总理、警方和联合国支持的反帮派力量；美国国务院 4 月 16 日旅行警示仍把海地列为最高级别风险。",
            "snapshot_note": "本轮北美更新把海地作为主要安全热点；加拿大和 USMCA 议题暂保留 4 月来源，作为经贸规则背景而非本轮主轴。",
            "key_actors": ["美国", "加拿大", "墨西哥", "海地", "多米尼加共和国", "联合国"],
            "hotspots": [
                {"name": "海地安全和国际支援", "status": "本地反帮派行动与外部外交同步进行", "summary": "AP 5 月 30 日记录美国副国务卿访问海地时，海地警方正在阿蒂博尼特对武装团伙行动并出现警员和平民死亡。", "risk_level": "high", "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"name": "多米尼加共和国边境与区域协作", "status": "海地危机外溢到邻国安全议程", "summary": "AP 报道称，美国高级外交官访问议题包括安全、经济和区域优先事项，多米尼加共和国在禁毒和海地边境问题上仍是美方关键伙伴。", "risk_level": "medium", "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"name": "加拿大对美贸易与 USMCA 背景", "status": "经贸规则压力保留为中期背景", "summary": "4 月来源显示加拿大仍强调美国不能单方面决定贸易条件，USMCA 审查和关税冲击仍是北美经贸背景。", "risk_level": "medium", "sources": ["north-ap-canada-trade-2026-04-23", "north-canada-tariff-2026-04-09"]},
            ],
            "latest_developments": [
                {"date": "2026-05-30", "title": "美国副国务卿访问海地和多米尼加共和国", "summary": "访问聚焦安全、经济和区域优先事项，美方会见海地总理、警方和联合国支持的反帮派力量。", "tags": ["海地", "多米尼加共和国"], "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"date": "2026-05-30", "title": "海地阿蒂博尼特行动出现警员和平民死亡", "summary": "AP 记录，海地警方在夺回受帮派控制地区的行动中出现伤亡，并向当地增派支援。", "tags": ["海地", "治安"], "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"date": "2026-04-16", "title": "美国国务院维持海地最高级别旅行警示", "summary": "美国官方警示继续强调犯罪、绑架、动荡和政府服务受限。", "tags": ["海地", "旅行警示"], "sources": ["north-state-haiti-advisory-2026-04-16"]},
            ],
            "timeline": [
                {"date": "2026-05-30", "title": "美国高级外交官访问海地和多米尼加共和国", "summary": "访问议题包括安全、经济和区域优先事项。", "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"date": "2026-05-30", "title": "海地阿蒂博尼特反帮派行动出现伤亡", "summary": "警方行动中三名警员和一名平民死亡。", "sources": ["north-ap-haiti-landau-2026-05-30"]},
                {"date": "2026-04-16", "title": "美国国务院更新海地旅行警示", "summary": "警示维持“不要旅行”级别。", "sources": ["north-state-haiti-advisory-2026-04-16"]},
            ],
            "sources": ["north-ap-haiti-landau-2026-05-30", "north-state-haiti-advisory-2026-04-16", "north-ap-canada-trade-2026-04-23", "north-canada-tariff-2026-04-09"],
        },
        "south-america": {
            "summary": "南美在 2026 年 5 月 31 日快照下由边境争端、跨国犯罪指定和选举安全共同牵引。AP 5 月 30 日记录圭亚那士兵在委内瑞拉边境交火中受伤；美国 5 月 28 日宣布将巴西 PCC 和 CV 指定为外国恐怖组织，巴西国内同日也开展针对犯罪集团金融网络的行动；哥伦比亚大选前无人机袭击担忧和厄瓜多尔治安军事化仍构成区域安全背景。",
            "snapshot_note": "本轮南美更新把安全议题分为三类：国家间边境摩擦、跨国犯罪金融和选举周期暴力风险。",
            "key_actors": ["圭亚那", "委内瑞拉", "巴西", "哥伦比亚", "厄瓜多尔", "美国"],
            "hotspots": [
                {"name": "圭亚那-委内瑞拉边境和埃塞奎博争端", "status": "边境交火使领土争端重新显性化", "summary": "AP 5 月 30 日记录圭亚那士兵在委内瑞拉边境交火中受伤，报道同时回顾委内瑞拉对埃塞奎博地区的主权主张。", "risk_level": "high", "sources": ["south-ap-guyana-venezuela-2026-05-30"]},
                {"name": "巴西犯罪集团与美国恐怖组织指定", "status": "治安议题进入外交和选举场域", "summary": "AP 5 月 28 日记录美国将 PCC 和 CV 指定为外国恐怖组织，巴西政府把该举视为可能干预内政；巴西检方同日继续针对犯罪集团金融网络行动。", "risk_level": "high", "sources": ["south-ap-brazil-gangs-2026-05-28", "south-ap-brazil-operation-2026-05-28"]},
                {"name": "哥伦比亚选举安全和厄瓜多尔治安军事化", "status": "选举周期与反毒品行动叠加", "summary": "AP 5 月 25 日记录哥伦比亚投票前无人机袭击担忧；厄瓜多尔总统 5 月 24 日则强调美国支持的反犯罪和引渡行动。", "risk_level": "medium", "sources": ["south-ap-colombia-election-2026-05-25", "south-ap-ecuador-security-2026-05-24"]},
            ],
            "latest_developments": [
                {"date": "2026-05-30", "title": "圭亚那士兵在委内瑞拉边境交火中受伤", "summary": "事件让埃塞奎博争端和边境安全重新成为南美北部风险焦点。", "tags": ["圭亚那", "委内瑞拉"], "sources": ["south-ap-guyana-venezuela-2026-05-30"]},
                {"date": "2026-05-28", "title": "美国将巴西 PCC 和 CV 指定为外国恐怖组织", "summary": "AP 记录，美国指定将于 6 月 5 日生效，巴西政府此前称会将该举视作内政干预。", "tags": ["巴西", "跨国犯罪"], "sources": ["south-ap-brazil-gangs-2026-05-28"]},
                {"date": "2026-05-25", "title": "哥伦比亚大选前无人机袭击引发安全担忧", "summary": "AP 记录，部分投票地附近警察设施遭无人机投爆物袭击，居民对投票安全保持警惕。", "tags": ["哥伦比亚", "选举安全"], "sources": ["south-ap-colombia-election-2026-05-25"]},
            ],
            "timeline": [
                {"date": "2026-05-30", "title": "圭委边境交火造成圭亚那士兵受伤", "summary": "事件发生在长期领土争端背景下。", "sources": ["south-ap-guyana-venezuela-2026-05-30"]},
                {"date": "2026-05-28", "title": "美国宣布指定巴西两大犯罪集团", "summary": "PCC 和 CV 将被列为外国恐怖组织。", "sources": ["south-ap-brazil-gangs-2026-05-28"]},
                {"date": "2026-05-25", "title": "哥伦比亚投票前安全担忧升温", "summary": "无人机袭击使部分地区选民对投票安全保持警惕。", "sources": ["south-ap-colombia-election-2026-05-25"]},
                {"date": "2026-05-24", "title": "厄瓜多尔总统强调反犯罪和引渡行动", "summary": "政府继续把有组织犯罪作为国家安全核心议题。", "sources": ["south-ap-ecuador-security-2026-05-24"]},
            ],
            "sources": ["south-ap-guyana-venezuela-2026-05-30", "south-ap-brazil-gangs-2026-05-28", "south-ap-brazil-operation-2026-05-28", "south-ap-colombia-election-2026-05-25", "south-ap-ecuador-security-2026-05-24"],
        },
    }

    for region_id, update in region_updates.items():
        regions[region_id].update(update)

    data["timeline_events"] = [
        {"date": "2026-05-30", "region_id": "north-america", "title": "美国高级外交官访问海地和多米尼加共和国", "summary": "访问期间安全、经济和区域优先事项成为核心议题。", "sources": ["north-ap-haiti-landau-2026-05-30"]},
        {"date": "2026-05-30", "region_id": "middle-east", "title": "加沙黄线停火争议持续", "summary": "AP 记录黄线周边执法、伤亡和双方互指违反停火。", "sources": ["middle-ap-gaza-yellow-line-2026-05-30"]},
        {"date": "2026-05-30", "region_id": "east-asia", "title": "菲律宾防长称南海威胁仍严重", "summary": "菲律宾在香格里拉对话期间强调同盟韧性和防务基础设施升级。", "sources": ["east-reuters-ph-threat-2026-05-30"]},
        {"date": "2026-05-30", "region_id": "south-america", "title": "圭委边境交火造成圭亚那士兵受伤", "summary": "埃塞奎博争端背景下的边境安全风险显性化。", "sources": ["south-ap-guyana-venezuela-2026-05-30"]},
        {"date": "2026-05-29", "region_id": "europe", "title": "乌克兰称俄罗斯准备大规模打击", "summary": "乌方称防空和天空防御力量将持续应对。", "sources": ["europe-reuters-attack-2026-05-29"]},
        {"date": "2026-05-28", "region_id": "south-america", "title": "美国指定巴西 PCC 和 CV 为外国恐怖组织", "summary": "指定将于 6 月 5 日生效，巴西国内政治反应强烈。", "sources": ["south-ap-brazil-gangs-2026-05-28"]},
        {"date": "2026-05-27", "region_id": "east-asia", "title": "朝鲜公布多系统武器测试", "summary": "测试涉及新型弹头、核能力巡航导弹和精确导航火箭炮。", "sources": ["east-ap-dprk-weapons-2026-05-27"]},
        {"date": "2026-05-25", "region_id": "middle-east", "title": "美军称在南伊朗实施自卫打击", "summary": "打击对象包括导弹发射点和布雷船只。", "sources": ["middle-ap-iran-strikes-2026-05-25"]},
        {"date": "2026-05-21", "region_id": "central-asia", "title": "UNAMA 关注阿富汗第 18 号法令", "summary": "UNAMA 称该法令进一步限制女性和儿童权利。", "sources": ["central-unama-decree-2026-05-21"]},
    ]

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
    print(f"Updated {DATA_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
