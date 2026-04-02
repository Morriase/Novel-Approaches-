#!/usr/bin/env python3
"""Parse AutoDock Vina scores from PDBQT files and export CSV summaries.

This script scans for lines like:
REMARK VINA RESULT:      -7.7      0.000      0.000
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from statistics import mean, median


VINA_RESULT_RE = re.compile(
    r"^REMARK\s+VINA\s+RESULT:\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)"
)


def parse_vina_results(pdbqt_path: Path) -> list[tuple[float, float, float]]:
    """Return parsed Vina rows as tuples: (affinity, rmsd_lb, rmsd_ub)."""
    rows: list[tuple[float, float, float]] = []
    with pdbqt_path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = VINA_RESULT_RE.match(line.strip())
            if not match:
                continue
            affinity, rmsd_lb, rmsd_ub = match.groups()
            rows.append((float(affinity), float(rmsd_lb), float(rmsd_ub)))
    return rows


def write_summary_csv(summary_path: Path, records: list[dict[str, object]]) -> None:
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(
            out,
            fieldnames=[
                "file_path",
                "modes",
                "best_affinity_kcal_mol",
                "worst_affinity_kcal_mol",
                "mean_affinity_kcal_mol",
                "median_affinity_kcal_mol",
                "score_spread_kcal_mol",
            ],
        )
        writer.writeheader()
        writer.writerows(records)


def write_pose_csv(poses_path: Path, records: list[dict[str, object]]) -> None:
    poses_path.parent.mkdir(parents=True, exist_ok=True)
    with poses_path.open("w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(
            out,
            fieldnames=[
                "file_path",
                "mode_index",
                "affinity_kcal_mol",
                "rmsd_lb",
                "rmsd_ub",
            ],
        )
        writer.writeheader()
        writer.writerows(records)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parse Vina results from PDBQT files")
    parser.add_argument(
        "--input-glob",
        default="results/docking/poses/**/*.pdbqt",
        help="Primary glob pattern for PDBQT files (default: results/docking/poses/**/*.pdbqt)",
    )
    parser.add_argument(
        "--legacy-input-glob",
        default="tests/**/*.pdbqt",
        help="Fallback glob pattern used only when primary glob finds no files",
    )
    parser.add_argument(
        "--summary-out",
        default="results/vina_score_summary.csv",
        help="Output CSV with per-file summary",
    )
    parser.add_argument(
        "--poses-out",
        default="results/vina_pose_scores.csv",
        help="Output CSV with one row per pose",
    )
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Base directory used for search and relative output paths",
    )
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    input_files = sorted(base_dir.glob(args.input_glob))
    selected_glob = args.input_glob
    if not input_files:
        input_files = sorted(base_dir.glob(args.legacy_input_glob))
        selected_glob = args.legacy_input_glob

    summary_rows: list[dict[str, object]] = []
    pose_rows: list[dict[str, object]] = []

    for pdbqt_path in input_files:
        vina_rows = parse_vina_results(pdbqt_path)
        if not vina_rows:
            continue

        affinities = [row[0] for row in vina_rows]
        rel_path = str(pdbqt_path.resolve().relative_to(base_dir)).replace("\\", "/")

        summary_rows.append(
            {
                "file_path": rel_path,
                "modes": len(affinities),
                "best_affinity_kcal_mol": min(affinities),
                "worst_affinity_kcal_mol": max(affinities),
                "mean_affinity_kcal_mol": round(mean(affinities), 3),
                "median_affinity_kcal_mol": median(affinities),
                "score_spread_kcal_mol": round(max(affinities) - min(affinities), 3),
            }
        )

        for idx, (affinity, rmsd_lb, rmsd_ub) in enumerate(vina_rows, start=1):
            pose_rows.append(
                {
                    "file_path": rel_path,
                    "mode_index": idx,
                    "affinity_kcal_mol": affinity,
                    "rmsd_lb": rmsd_lb,
                    "rmsd_ub": rmsd_ub,
                }
            )

    summary_out = (base_dir / args.summary_out).resolve()
    poses_out = (base_dir / args.poses_out).resolve()

    write_summary_csv(summary_out, summary_rows)
    write_pose_csv(poses_out, pose_rows)

    print(f"Input glob used: {selected_glob}")
    print(f"Parsed files with Vina results: {len(summary_rows)}")
    print(f"Summary CSV: {summary_out}")
    print(f"Pose CSV: {poses_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
