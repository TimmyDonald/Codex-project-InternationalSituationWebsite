#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "generated_at",
    "site",
    "global_overview",
    "regions",
    "timeline_events",
    "sources",
}

REQUIRED_REGION_KEYS = {
    "id",
    "label",
    "slug",
    "summary",
    "key_actors",
    "hotspots",
    "latest_developments",
    "timeline",
    "sources",
}


def ensure_no_mojibake_strings(payload: object) -> None:
    suspicious: list[str] = []

    def visit(value: object, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                visit(child, f"{path}.{key}" if path else str(key))
            return
        if isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, f"{path}[{index}]")
            return
        if isinstance(value, str) and ("\ufffd" in value or "???" in value):
            suspicious.append(path)

    visit(payload, "")
    if suspicious:
        raise ValueError(
            "possible mojibake detected in strings: " + ", ".join(suspicious[:12])
        )


def validate_site_data(payload: dict) -> None:
    missing = REQUIRED_TOP_LEVEL_KEYS - payload.keys()
    if missing:
        raise ValueError(f"missing top-level keys: {', '.join(sorted(missing))}")

    ensure_no_mojibake_strings(payload)

    source_ids = set()
    for source in payload["sources"]:
        source_id = source.get("id")
        if not source_id:
            raise ValueError("every source must include an 'id'")
        if source_id in source_ids:
            raise ValueError(f"duplicate source id: {source_id}")
        source_ids.add(source_id)

    region_ids = set()
    for region in payload["regions"]:
        missing_region_keys = REQUIRED_REGION_KEYS - region.keys()
        if missing_region_keys:
            raise ValueError(
                f"region {region.get('id', '<unknown>')} is missing keys: "
                f"{', '.join(sorted(missing_region_keys))}"
            )
        if region["id"] in region_ids:
            raise ValueError(f"duplicate region id: {region['id']}")
        region_ids.add(region["id"])

    def ensure_sources_exist(container: dict, label: str) -> None:
        for source_id in container.get("sources", []):
            if source_id not in source_ids:
                raise ValueError(f"{label} references unknown source id: {source_id}")

    for hotspot in payload["global_overview"].get("hotspots", []):
        ensure_sources_exist(hotspot, f"global hotspot '{hotspot.get('name', '')}'")

    for item in payload["global_overview"].get("latest_developments", []):
        ensure_sources_exist(item, f"global development '{item.get('title', '')}'")
        if item.get("region_id") not in region_ids:
            raise ValueError(f"unknown region_id in global development '{item.get('title', '')}'")

    for region in payload["regions"]:
        for hotspot in region.get("hotspots", []):
            ensure_sources_exist(hotspot, f"hotspot '{hotspot.get('name', '')}'")
        for item in region.get("latest_developments", []):
            ensure_sources_exist(item, f"development '{item.get('title', '')}'")
        for item in region.get("timeline", []):
            ensure_sources_exist(item, f"timeline item '{item.get('title', '')}'")
        for source_id in region.get("sources", []):
            if source_id not in source_ids:
                raise ValueError(f"region '{region['id']}' references unknown source id: {source_id}")

    for event in payload["timeline_events"]:
        ensure_sources_exist(event, f"timeline event '{event.get('title', '')}'")
        if event.get("region_id") not in region_ids:
            raise ValueError(f"unknown region_id in timeline event '{event.get('title', '')}'")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate international situation JSON and build a browser-ready JS file."
    )
    parser.add_argument("--input", required=True, help="Path to site JSON")
    parser.add_argument("--output", required=True, help="Path to generated JS file")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    validate_site_data(payload)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "window.__INTL_SITUATION__ = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Built {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
