#!/usr/bin/env python3
"""Check backward compatibility of simplified event JSON Schemas."""
import argparse
import json
from pathlib import Path


def check(before, after):
    old_props, new_props = before.get("properties", {}), after.get("properties", {})
    old_required, new_required = set(before.get("required", [])), set(after.get("required", []))
    issues = []
    for name, old in old_props.items():
        if name not in new_props: issues.append({"field": name, "kind": "field-removed"})
        elif old.get("type") != new_props[name].get("type"): issues.append({"field": name, "kind": "type-changed"})
    for name in new_required - old_required:
        issues.append({"field": name, "kind": "required-added"})
    return {"compatible": not issues, "issues": issues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before"); parser.add_argument("after")
    args = parser.parse_args()
    report = check(json.loads(Path(args.before).read_text()), json.loads(Path(args.after).read_text()))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["compatible"] else 1)


if __name__ == "__main__":
    main()
