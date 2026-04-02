# Repository Migration Plan (Research-Grade Structure)

## Goal
Move from mixed working folders (mainly under `tests/`) to a stable, research-first structure that is easier for supervisors, reviewers, and collaborators to navigate.

This plan is intentionally non-destructive:
- Phase 1 creates the target structure and copies key files.
- Phase 2 updates references and scripts.
- Phase 3 archives legacy folders after verification.

## Target structure

```text
.
├── docs/
│   ├── REPOSITORY_MIGRATION_PLAN.md
│   ├── METHODS.md
│   └── DECISION_LOG.md
├── data/
│   ├── ligands/
│   │   ├── raw/
│   │   └── optimized/
│   ├── receptors/
│   │   ├── raw/
│   │   └── prepared/
│   └── docking_inputs/
│       ├── conf/
│       ├── ligand_pdbqt/
│       └── receptor_pdbqt/
├── results/
│   ├── docking/
│   │   ├── poses/
│   │   └── scores/
│   ├── interactions/
│   │   ├── 2d_maps/
│   │   └── 3d_complexes/
│   └── summaries/
│       ├── vina_score_summary.csv
│       └── vina_pose_scores.csv
├── scripts/
├── archive/
│   └── legacy_tests_snapshot/
└── README.md
```

## Mapping from current folders

| Current path | Target path | Notes |
|---|---|---|
| `tests/hits/` | `data/ligands/raw/` | Keep original downloads and SDF sources unchanged |
| `tests/hits opt/` | `data/ligands/optimized/` | Optimized MOL2 and related files |
| `tests/receptors/` | `data/receptors/raw/` | Raw and optimized receptor structure files |
| `tests/Receptor binding analysis/*.conf` | `data/docking_inputs/conf/` | Vina grid and run settings |
| `tests/Receptor binding analysis/*.ligand.pdbqt` | `data/docking_inputs/ligand_pdbqt/` | Prepared ligands for docking |
| `tests/Receptor binding analysis/*.receptor.pdbqt` | `data/docking_inputs/receptor_pdbqt/` | Prepared receptors for docking |
| `tests/Docking scores/*.pdbqt` | `results/docking/poses/` | Primary pose output artifacts |
| `tests/docking complex/*-visual.png` | `results/interactions/2d_maps/` | 2D interaction maps and composite visuals |
| `tests/docking complex/*.pdb` | `results/interactions/3d_complexes/` | Docked complex geometry references |
| `results/vina_*.csv` | `results/summaries/` | Parser-generated quantitative summaries |

## Phase-by-phase execution

## Phase 1: Create new layout and copy files
1. Create all target directories.
2. Copy (not move) files from `tests/` into mapped target locations.
3. Keep existing files intact to avoid breaking current workflows.

Success criteria:
- New structure exists.
- Key artifacts (ligands, receptors, conf, docking outputs, visuals) are duplicated in target paths.

## Phase 2: Update workflows to use new paths
1. Update `scripts/parse_vina_scores.py` defaults to read from `results/docking/poses/`.
2. Keep backward-compatible fallback support for legacy paths during transition.
3. Update README references to point to new canonical paths.

Success criteria:
- Parser and documentation use canonical folders.
- Legacy paths still work during transition window.

## Phase 3: Freeze and archive legacy tree
1. Create `archive/legacy_tests_snapshot/` and move old `tests/` contents there.
2. Leave a minimal pointer in `tests/README.md` indicating where canonical data lives.
3. Tag the migration commit (for example `layout-migration-v1`).

Success criteria:
- Single canonical structure is active.
- Legacy snapshot remains available for traceability.

## Suggested metadata files

Add these lightweight documents in `docs/`:
- `METHODS.md`: exact docking protocol, software versions, and parameter standards.
- `DECISION_LOG.md`: dated candidate promotion decisions (promote/hold/control-only).

This makes the repository read like an evolving computational study rather than an ad-hoc file collection.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Broken path references in README/scripts | Run migration in copy-first mode; update paths in small commits |
| Duplicate files create confusion | Label canonical paths clearly in README immediately |
| Legacy workflow interruption | Keep fallback parser support for one transition cycle |

## Recommended commit sequence
1. `chore(layout): add canonical directory scaffold`
2. `chore(layout): copy current assets into canonical research folders`
3. `docs(readme): switch references to canonical paths`
4. `refactor(parser): default to canonical docking output folders`
5. `chore(archive): move legacy tests tree into archive snapshot`
