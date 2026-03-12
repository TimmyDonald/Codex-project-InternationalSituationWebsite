#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_site_data import validate_site_data


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate international situation JSON.")
    parser.add_argument("path", help="Path to site JSON")
    args = parser.parse_args()

    path = Path(args.path).resolve()
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate_site_data(payload)
    print(f"Site data is valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
