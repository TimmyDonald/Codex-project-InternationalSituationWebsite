const payload = window.__INTL_SITUATION__;

const locale = "zh-CN";
const REGION_ORDER = [
  "north-america",
  "south-america",
  "europe",
  "middle-east",
  "central-asia",
  "east-asia"
];

const REGION_THEMES = {
  "north-america": { accent: "#2f6fed", soft: "rgba(47, 111, 237, 0.12)" },
  "south-america": { accent: "#2d8a57", soft: "rgba(45, 138, 87, 0.12)" },
  europe: { accent: "#a34e2f", soft: "rgba(163, 78, 47, 0.12)" },
  "middle-east": { accent: "#b06b1f", soft: "rgba(176, 107, 31, 0.12)" },
  "central-asia": { accent: "#7a5cc2", soft: "rgba(122, 92, 194, 0.12)" },
  "east-asia": { accent: "#9a2f59", soft: "rgba(154, 47, 89, 0.12)" }
};

const REGION_MAP_LAYOUT = {
  "north-america": {
    path: "M72 70 L188 44 L264 70 L258 118 L220 138 L176 128 L136 154 L80 134 Z",
    labelX: 170,
    labelY: 110,
    numberX: 122,
    numberY: 92
  },
  "south-america": {
    path: "M196 184 L236 208 L252 264 L234 332 L210 390 L184 366 L174 308 L178 244 Z",
    labelX: 216,
    labelY: 284,
    numberX: 176,
    numberY: 238
  },
  europe: {
    path: "M424 74 L478 60 L526 82 L522 122 L488 134 L440 122 L420 96 Z",
    labelX: 480,
    labelY: 102,
    numberX: 432,
    numberY: 82
  },
  "middle-east": {
    path: "M514 144 L580 144 L626 176 L612 220 L556 232 L508 198 Z",
    labelX: 574,
    labelY: 188,
    numberX: 520,
    numberY: 158
  },
  "central-asia": {
    path: "M596 90 L684 78 L756 104 L754 150 L696 170 L620 154 L586 118 Z",
    labelX: 684,
    labelY: 126,
    numberX: 608,
    numberY: 98
  },
  "east-asia": {
    path: "M780 90 L862 110 L916 164 L900 218 L832 224 L772 188 L748 136 Z",
    labelX: 844,
    labelY: 160,
    numberX: 774,
    numberY: 112
  }
};

function formatDate(value) {
  if (!value) {
    return "日期未知";
  }

  return new Intl.DateTimeFormat(locale, {
    year: "numeric",
    month: "long",
    day: "numeric"
  }).format(new Date(value));
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (match) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  }[match]));
}

function getBasePath() {
  const customPath = document.body.dataset.basePath;
  return customPath ? `${customPath}/` : "./";
}

function getSourceMap() {
  const map = new Map();
  if (!payload || !Array.isArray(payload.sources)) {
    return map;
  }

  payload.sources.forEach((source) => {
    map.set(source.id, source);
  });
  return map;
}

const sourceMap = getSourceMap();

function resolveSources(sourceIds = []) {
  return sourceIds.map((sourceId) => sourceMap.get(sourceId)).filter(Boolean);
}

function sortRegions(regions) {
  return [...regions].sort((left, right) => REGION_ORDER.indexOf(left.id) - REGION_ORDER.indexOf(right.id));
}

function getRegionTheme(regionId) {
  return REGION_THEMES[regionId] || { accent: "#8b3c34", soft: "rgba(139, 60, 52, 0.12)" };
}

function getRegionById(regionId) {
  return payload.regions.find((region) => region.id === regionId);
}

function themeStyle(regionId) {
  const theme = getRegionTheme(regionId);
  return `--region-accent:${theme.accent};--region-soft:${theme.soft};`;
}

function riskLabel(level) {
  const labels = { high: "高风险", medium: "中风险", low: "低风险" };
  return labels[level] || "未评级";
}

function renderTopNav() {
  const topnav = document.querySelector("#topnav");
  if (!topnav || !payload) {
    return;
  }

  const basePath = getBasePath();
  const regionLinks = sortRegions(payload.regions)
    .map((region) => {
      const theme = getRegionTheme(region.id);
      return `
        <a href="${basePath}regions/${region.slug}.html" data-region-id="${region.id}" style="--region-accent:${theme.accent};--region-soft:${theme.soft};">
          ${escapeHtml(region.label)}
        </a>
      `;
    })
    .join("");

  topnav.innerHTML = `
    <a href="${basePath}index.html">全球总览</a>
    ${regionLinks}
  `;
}

function renderSourceLinks(sourceIds, className = "source-link") {
  return resolveSources(sourceIds)
    .map((source) => `
      <a class="${className}" href="${source.url}" target="_blank" rel="noreferrer">
        <span class="source-publisher">${escapeHtml(source.publisher)}</span>
        <span>${escapeHtml(source.title)}</span>
      </a>
    `)
    .join("");
}

function renderSourceRegister(sourceIds) {
  const seen = new Set();
  const sources = sourceIds
    .flatMap((id) => resolveSources([id]))
    .filter((source) => {
      if (seen.has(source.id)) {
        return false;
      }
      seen.add(source.id);
      return true;
    });

  return sources
    .map((source) => `
      <article class="source-record">
        <div>
          <p class="source-publisher">${escapeHtml(source.publisher)}</p>
          <h3>${escapeHtml(source.title)}</h3>
          <p class="source-note">${escapeHtml(source.note)}</p>
        </div>
        <dl class="meta-list">
          <div>
            <dt>发布日期</dt>
            <dd>${escapeHtml(source.published_at)}</dd>
          </div>
          <div>
            <dt>访问日期</dt>
            <dd>${escapeHtml(source.accessed_at)}</dd>
          </div>
        </dl>
        <a class="source-link" href="${source.url}" target="_blank" rel="noreferrer">打开来源</a>
      </article>
    `)
    .join("");
}

function createHotspotCard(hotspot, regionLabel = "", regionId = "") {
  const resolvedRegionId = regionId || hotspot.region_id || "";
  return `
    <article class="card hotspot-card" data-risk="${escapeHtml(hotspot.risk_level)}" data-region-id="${escapeHtml(resolvedRegionId)}" style="${themeStyle(resolvedRegionId)}">
      <div class="card-topline">
        <span class="status-pill">${escapeHtml(hotspot.status)}</span>
        <span class="risk-pill">${riskLabel(hotspot.risk_level)}</span>
      </div>
      <h3>${escapeHtml(hotspot.name)}</h3>
      <p>${escapeHtml(hotspot.summary)}</p>
      ${regionLabel ? `<p class="mini-label">${escapeHtml(regionLabel)}</p>` : ""}
      <div class="source-chip-row">
        ${renderSourceLinks(hotspot.sources, "source-chip")}
      </div>
    </article>
  `;
}

function createRegionCard(region, index) {
  const basePath = getBasePath();
  return `
    <article class="card region-card" data-region-id="${region.id}" style="${themeStyle(region.id)}">
      <div class="card-topline">
        <p class="section-kicker">${escapeHtml(region.nav_label || region.label)}</p>
        <span class="region-order">0${index + 1}</span>
      </div>
      <h3>${escapeHtml(region.label)}</h3>
      <p>${escapeHtml(region.summary)}</p>
      <div class="card-metrics">
        <span>${region.hotspots.length} 个热点</span>
        <span>${region.latest_developments.length} 条近期动态</span>
      </div>
      <a class="inline-link" href="${basePath}regions/${region.slug}.html">进入地区页</a>
    </article>
  `;
}

function createDevelopmentCard(item, regionLabel = "", regionId = "") {
  return `
    <article class="development-card" data-region-id="${escapeHtml(regionId)}" style="${themeStyle(regionId)}">
      <div class="card-topline">
        <span class="date-label">${formatDate(item.date)}</span>
        ${regionLabel ? `<span class="mini-label">${escapeHtml(regionLabel)}</span>` : ""}
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.summary)}</p>
      <div class="tag-row">
        ${(item.tags || []).map((tag) => `<span class="topic-chip">${escapeHtml(tag)}</span>`).join("")}
      </div>
      <div class="source-chip-row">
        ${renderSourceLinks(item.sources, "source-chip")}
      </div>
    </article>
  `;
}

function createTimelineItem(item, regionLabel = "", regionId = "") {
  return `
    <li class="timeline-item" data-region-id="${escapeHtml(regionId)}" style="${themeStyle(regionId)}">
      <div class="timeline-head">
        <span class="date-label">${formatDate(item.date)}</span>
        ${regionLabel ? `<span class="mini-label">${escapeHtml(regionLabel)}</span>` : ""}
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.summary)}</p>
      <div class="source-chip-row">
        ${renderSourceLinks(item.sources, "source-chip")}
      </div>
    </li>
  `;
}

function createMapSvg(regions) {
  const basePath = getBasePath();
  const regionShapes = regions
    .map((region, index) => {
      const theme = getRegionTheme(region.id);
      const layout = REGION_MAP_LAYOUT[region.id];
      return `
        <a href="${basePath}regions/${region.slug}.html" class="map-region-link" aria-label="${escapeHtml(region.label)}">
          <path class="map-region-shape" d="${layout.path}" fill="${theme.soft}" stroke="${theme.accent}" stroke-width="3"></path>
          <circle cx="${layout.numberX}" cy="${layout.numberY}" r="24" fill="white" stroke="${theme.accent}" stroke-width="2"></circle>
          <text x="${layout.numberX}" y="${layout.numberY + 7}" text-anchor="middle" class="map-region-number" fill="${theme.accent}">0${index + 1}</text>
          <text x="${layout.labelX}" y="${layout.labelY}" text-anchor="middle" class="map-region-label" fill="${theme.accent}">${escapeHtml(region.nav_label || region.label)}</text>
        </a>
      `;
    })
    .join("");

  return `
    <svg class="world-map-svg" viewBox="0 0 1000 520" role="img" aria-label="分区世界地图导航">
      <defs>
        <linearGradient id="mapBg" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="rgba(255,255,255,0.72)" />
          <stop offset="100%" stop-color="rgba(244,239,230,0.95)" />
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="1000" height="520" rx="32" fill="url(#mapBg)"></rect>
      <g class="map-grid">
        <path d="M40 90 H960 M40 160 H960 M40 230 H960 M40 300 H960 M40 370 H960 M40 440 H960" />
        <path d="M130 40 V480 M260 40 V480 M390 40 V480 M520 40 V480 M650 40 V480 M780 40 V480 M910 40 V480" />
      </g>
      <g class="map-outline">
        <path d="M58 58 L278 58 L278 172 L234 162 L214 150 L176 142 L118 164 L76 146 Z" />
        <path d="M184 174 L260 206 L272 268 L242 404 L192 398 L164 296 L172 214 Z" />
        <path d="M412 54 L548 54 L548 138 L498 146 L426 132 L402 94 Z" />
        <path d="M560 72 L934 72 L934 250 L842 246 L770 212 L720 192 L684 180 L610 160 L570 126 Z" />
      </g>
      ${regionShapes}
    </svg>
  `;
}

function createMapListItem(region, index) {
  const basePath = getBasePath();
  return `
    <a class="map-list-item" href="${basePath}regions/${region.slug}.html" data-region-id="${region.id}" style="${themeStyle(region.id)}">
      <span class="map-list-index">0${index + 1}</span>
      <span class="map-list-name">${escapeHtml(region.label)}</span>
      <span class="map-list-meta">${region.hotspots.length} 个热点 / ${region.latest_developments.length} 条更新</span>
    </a>
  `;
}

function renderMap(regions) {
  const mapBoard = document.querySelector("#map-board");
  const mapDirectory = document.querySelector("#map-directory");
  if (!mapBoard || !mapDirectory) {
    return;
  }

  mapBoard.innerHTML = `
    <div class="map-shell map-shell-world">
      <div class="map-headerline">
        <span>Region Order</span>
        <span>West to East</span>
      </div>
      ${createMapSvg(regions)}
    </div>
  `;

  mapDirectory.innerHTML = regions.map((region, index) => createMapListItem(region, index)).join("");
}

function renderHome() {
  const heroTitle = document.querySelector("#hero-title");
  const heroDek = document.querySelector("#hero-dek");
  const statGrid = document.querySelector("#stat-grid");
  const lastUpdatedLabel = document.querySelector("#last-updated-label");
  const overviewPoints = document.querySelector("#overview-points");
  const snapshotNote = document.querySelector("#snapshot-note");
  const hotspotGrid = document.querySelector("#hotspot-grid");
  const regionGrid = document.querySelector("#region-grid");
  const latestList = document.querySelector("#latest-list");
  const timelineList = document.querySelector("#timeline-list");
  const updateProcess = document.querySelector("#update-process");
  const sourceGroupList = document.querySelector("#source-group-list");

  const { global_overview: overview, timeline_events: timelineEvents, site } = payload;
  const regions = sortRegions(payload.regions);

  heroTitle.textContent = overview.headline;
  heroDek.textContent = overview.dek;
  lastUpdatedLabel.textContent = overview.last_updated_label;

  statGrid.innerHTML = `
    <li><span class="stat-label">覆盖地区</span><strong>${regions.length}</strong></li>
    <li><span class="stat-label">重点热点</span><strong>${overview.hotspots.length}</strong></li>
    <li><span class="stat-label">最新条目</span><strong>${overview.latest_developments.length}</strong></li>
    <li><span class="stat-label">已登记来源</span><strong>${payload.sources.length}</strong></li>
  `;

  overviewPoints.innerHTML = (overview.summary_points || []).map((point) => `<p>${escapeHtml(point)}</p>`).join("");
  snapshotNote.textContent = overview.snapshot_note;
  renderMap(regions);

  hotspotGrid.innerHTML = overview.hotspots
    .map((hotspot) => {
      const region = regions.find((item) => item.id === hotspot.region_id);
      return createHotspotCard(hotspot, region ? region.label : "", hotspot.region_id);
    })
    .join("");

  regionGrid.innerHTML = regions.map((region, index) => createRegionCard(region, index)).join("");

  latestList.innerHTML = overview.latest_developments
    .map((item) => {
      const region = regions.find((entry) => entry.id === item.region_id);
      return createDevelopmentCard(item, region ? region.label : "", item.region_id);
    })
    .join("");

  timelineList.innerHTML = timelineEvents
    .map((item) => {
      const region = regions.find((entry) => entry.id === item.region_id);
      return createTimelineItem(item, region ? region.label : "", item.region_id);
    })
    .join("");

  updateProcess.textContent = site.update_process;
  sourceGroupList.innerHTML = overview.source_groups
    .map((group) => `
      <article class="source-group">
        <h4>${escapeHtml(group.label)}</h4>
        <p>${escapeHtml(group.description)}</p>
      </article>
    `)
    .join("");
}

function renderRegion() {
  const regionId = document.body.dataset.region;
  const region = payload.regions.find((entry) => entry.id === regionId);

  if (!region) {
    document.querySelector("#main-content").innerHTML = `
      <section class="section">
        <article class="panel">
          <h1>未找到地区数据</h1>
          <p>请检查 data/international-situation.json 中的地区 id 是否与页面一致。</p>
        </article>
      </section>
    `;
    return;
  }

  const theme = getRegionTheme(region.id);
  const hero = document.querySelector("#region-hero");
  const actorsList = document.querySelector("#actors-list");
  const snapshotNote = document.querySelector("#region-snapshot-note");
  const hotspots = document.querySelector("#region-hotspots");
  const developments = document.querySelector("#region-developments");
  const timeline = document.querySelector("#region-timeline");
  const sources = document.querySelector("#region-sources");

  hero.style.setProperty("--region-accent", theme.accent);
  hero.style.setProperty("--region-soft", theme.soft);
  hero.classList.add("region-themed");

  hero.innerHTML = `
    <div class="hero-copy">
      <p class="eyebrow">${escapeHtml(region.nav_label || region.label)}</p>
      <h1>${escapeHtml(region.label)}</h1>
      <p class="hero-summary">${escapeHtml(region.summary)}</p>
      <div class="hero-actions">
        <a class="button button-primary" href="#hotspot-title">查看热点</a>
        <a class="button button-secondary" href="#sources-title">查看来源</a>
      </div>
    </div>
    <aside class="hero-panel">
      <p class="eyebrow">Last Updated</p>
      <p class="region-stamp">${escapeHtml(payload.global_overview.last_updated_label)}</p>
      <p class="hero-note">${escapeHtml(region.snapshot_note)}</p>
    </aside>
  `;

  actorsList.innerHTML = region.key_actors.map((actor) => `<span class="actor-chip" style="${themeStyle(region.id)}">${escapeHtml(actor)}</span>`).join("");
  snapshotNote.textContent = region.snapshot_note;
  hotspots.innerHTML = region.hotspots.map((item) => createHotspotCard(item, "", region.id)).join("");
  developments.innerHTML = region.latest_developments.map((item) => createDevelopmentCard(item, "", region.id)).join("");
  timeline.innerHTML = region.timeline.map((item) => createTimelineItem(item, "", region.id)).join("");
  sources.innerHTML = renderSourceRegister(region.sources);
}

function boot() {
  if (!payload || !Array.isArray(payload.regions) || !Array.isArray(payload.sources)) {
    document.body.innerHTML = `
      <main class="page-shell">
        <section class="section">
          <article class="panel">
            <h1>数据未加载</h1>
            <p>请先运行构建脚本生成 <code>data/site.js</code>。</p>
          </article>
        </section>
      </main>
    `;
    return;
  }

  renderTopNav();

  if (document.body.dataset.page === "home") {
    renderHome();
    return;
  }

  if (document.body.dataset.page === "region") {
    renderRegion();
  }
}

boot();
