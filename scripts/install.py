#!/usr/bin/env python3
"""Copy selected self-contained skills without overwriting existing folders."""

import argparse
import shutil
from pathlib import Path


SKILLS = ("pnas-writing", "pnas-figure", "pnas-polishing")
SOURCE = Path(__file__).resolve().parents[1] / "skills"


def install(destination, names, dry_run=False):
    destination = Path(destination).expanduser().resolve()
    selected = tuple(dict.fromkeys(names))
    if not selected or any(name not in SKILLS for name in selected):
        raise ValueError("Select one or more known skills.")
    # Check the whole request before copying any skill.
    for name in selected:
        source = SOURCE / name
        target = destination / name
        if not (source / "SKILL.md").is_file():
            raise FileNotFoundError(f"Missing skill entry point: {source}")
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Already exists: {target}. Back it up outside the skill scan paths first.")
        if source.resolve() == target.resolve() or source.resolve() in target.resolve().parents:
            raise ValueError(f"Destination cannot be inside the source skill: {target}")
    for name in selected:
        target = destination / name
        print(f"{'Would install' if dry_run else 'Installing'} {name} -> {target}")
        if not dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(SOURCE / name, target)
    return [destination / name for name in selected]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Destination skills directory (default: ~/.agents/skills)")
    parser.add_argument("--skill", action="append", choices=SKILLS,
                        help="Install a single skill; repeat to select several (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only; create no files")
    args = parser.parse_args()
    try:
        install(args.dest, args.skill or SKILLS, args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Installation stopped: {exc}\n")


if __name__ == "__main__":
    main()
