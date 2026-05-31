# 国际局势观察

一个静态国际形势快照网站，覆盖全球总览、东亚、中亚、中东、欧洲、北美和南美。内容集中维护在 `data/international-situation.json`，构建脚本会生成浏览器直接加载的 `data/site.js`。

## 本地预览

```powershell
python -m http.server 4173
```

然后打开 `http://localhost:4173/`。

## 更新数据

```powershell
python scripts/update_snapshot_20260531.py
python scripts/build_site_data.py --input data/international-situation.json --output data/site.js
python scripts/validate_site_data.py data/international-situation.json
```

## 当前快照

- 快照日期：2026-05-31
- 来源策略：优先使用联合国、OCHA、美国国务院等一手来源，再用 AP、Reuters 等补充近期动态。
- 发布形态：纯静态文件，可直接托管在 GitHub Pages 或任意静态托管服务。
