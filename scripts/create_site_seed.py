#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


SEED = {
    "schema_version": "1.1",
    "generated_at": "",
    "site": {
        "title": "国际局势观察",
        "description": "国际局势站点的数据骨架。",
        "language": "zh-CN",
        "snapshot_date": "",
        "update_process": ""
    },
    "global_overview": {
        "headline": "",
        "dek": "",
        "last_updated_label": "",
        "summary_points": [],
        "snapshot_note": "",
        "hotspots": [],
        "latest_developments": [],
        "source_groups": []
    },
    "regions": [],
    "timeline_events": [],
    "sources": []
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a starter site JSON file.")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--force", action="store_true", help="Overwrite existing file")
    args = parser.parse_args()

    output_path = Path(args.output).resolve()
    if output_path.exists() and not args.force:
        parser.error(f"{output_path} already exists. Use --force to overwrite it.")

    payload = dict(SEED)
    payload["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    payload["site"] = dict(SEED["site"])
    payload["site"]["snapshot_date"] = datetime.now(timezone.utc).date().isoformat()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
