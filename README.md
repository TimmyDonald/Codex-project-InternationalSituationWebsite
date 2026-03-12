# README.md

# 国际局势观察（Situation Monitor）

一个 **基于结构化数据的全球国际局势快照网站**。
网站以 **静态页面 + 数据文件驱动** 的方式构建，展示全球热点、安全态势、时间线与地区局势。

该项目的设计目标是：

* 用 **结构化 JSON 数据** 管理国际局势
* 用 **静态网站** 展示分析结果
* 通过简单脚本 **生成与更新网站内容**

---

# 项目截图（示意）

首页包含以下主要模块：

* 全球局势快照
* 世界地图入口
* 热点地区
* 各地区局势入口
* 最新发展
* 全球时间线
* 数据来源与方法论

网站首页标题：

> 国际局势观察 — Situation Monitor 

---

# 网站特点

### 1 静态架构

网站完全由静态文件构成：

* HTML
* CSS
* JavaScript
* JSON 数据

因此可以直接部署到：

* GitHub Pages
* Cloudflare Pages
* Netlify
* Vercel
* 任意静态服务器

无需后端服务。

---

### 2 数据驱动

网站数据来自：

```
data/international-situation.json
```

包含：

* 全球概览
* 各地区局势
* 热点事件
* 时间线
* 数据来源

示例结构：

```json
{
  "schema_version": "1.1",
  "generated_at": "2026-03-11",
  "site": {...},
  "global_overview": {...},
  "regions": [...],
  "sources": [...]
}
```

该文件是 **唯一需要人工维护的核心数据文件**。 

---

### 3 自动渲染页面

`app.js` 会在浏览器中读取数据：

```javascript
const payload = window.__INTL_SITUATION__;
```

然后动态生成：

* 导航
* 地图
* 热点卡片
* 时间线
* 地区页面内容 

---

### 4 世界地图导航

首页包含一个 **SVG 世界地图导航**：

* 北美
* 南美
* 欧洲
* 中东
* 中亚
* 东亚

地图由 JS 动态生成，每个地区对应一个入口。

地区顺序：

```
north-america
south-america
europe
middle-east
central-asia
east-asia
```

按 **西半球 → 东半球排序**。 

---

# 项目结构

```
project/
│
├── index.html
├── styles.css
├── app.js
│
├── data/
│   ├── site.js
│   └── international-situation.json
│
├── regions/
│   ├── east-asia.html
│   ├── europe.html
│   ├── middle-east.html
│   └── ...
│
└── scripts/
    ├── build_site_data.py
    └── validate_site_data.py
```

---

# 页面结构

首页由以下模块组成：

```
Global Snapshot
│
├─ 当前总览
├─ 世界地图入口
├─ 重点热点
├─ 地区入口
├─ 最新发展
├─ 全球时间线
└─ 方法论与来源
```

HTML 页面加载：

```
styles.css
data/site.js
app.js
```

然后由 `app.js` 渲染页面。 

---

# 数据更新流程

项目采用 **数据驱动更新方式**：

1️⃣ 修改数据文件：

```
data/international-situation.json
```

2️⃣ 运行构建脚本：

```
python scripts/build_site_data.py \
  --input data/international-situation.json \
  --output data/site.js
```

3️⃣ 校验数据：

```
python scripts/validate_site_data.py \
  data/international-situation.json
```

4️⃣ 重新部署网站。

该流程保证：

* 网站仍然是静态站
* 更新只需要修改一个数据文件

说明来自数据文件中的 `update_process` 字段。 

---

# 支持地区

当前版本覆盖六个地区：

| 地区 | 说明         |
| -- | ---------- |
| 东亚 | 台海、南海、朝鲜半岛 |
| 中亚 | 阿富汗外溢与边境冲突 |
| 中东 | 加沙、黎巴嫩、伊朗  |
| 欧洲 | 俄乌战争       |
| 北美 | 贸易与安全      |
| 南美 | 边界争议与安全合作  |

每个地区包含：

* 关键行为体
* 热点事件
* 最新动态
* 历史时间线
* 数据来源

---

# 数据来源

网站优先使用以下来源：

### 一手来源

* 联合国
* 欧盟
* 各国政府

### 权威媒体

* Associated Press (AP)

### 研究机构

* AMTI
* UNRCCA

来源信息会在页面中提供链接与说明。 

---

# 本地运行

由于是静态网站，可以直接打开：

```
index.html
```

或者使用本地服务器：

```
python -m http.server
```

然后访问：

```
http://localhost:8000
```

---

# 部署

推荐部署方式：

### GitHub Pages

1 创建仓库
2 上传项目
3 打开：

```
Settings → Pages
```

4 选择：

```
Branch: main
Folder: /(root)
```

网站即可上线。

---

# 技术栈

```
HTML5
CSS3
Vanilla JavaScript
JSON
Python (构建脚本)
```

UI 特点：

* 报告式设计
* 卡片布局
* 世界地图导航
* 响应式布局 

---

# 未来扩展

可能的扩展方向：

* 自动抓取新闻
* GitHub Actions 自动更新
* 数据可视化
* 历史趋势图
* 多语言支持

---

# License

MIT License

---
