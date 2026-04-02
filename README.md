# Novel Approaches for Chronic Wound Healing: Computational Phytochemical Discovery

## Current Project Status (April 2026)
This repository now reflects a practical docking-focused workflow completed in the `tests/` workspace.

Today we worked on two receptor-ligand systems:
- `Curcumin` docked against human `MMP-8` (receptor source: `1A85`)
- `Propranolol` docked against human `beta1 adrenergic receptor` (receptor source: `7BVQ`)

The project goal remains chronic-wound-targeted lead discovery, but the current data in this repo is centered on docking execution, pose collection, and interaction visualization.

## What Is In The Repository Right Now

```text
.
├── README.md
├── Research materials/
├── Resources/
│   ├── Computational Wound Healing Phytochemical Research Strategy.epub
│   └── Computational Wound Healing Phytochemical Research Strategy.md
├── tests/
│   ├── docking complex/
│   │   ├── curcumin-mmp8-visual.png
│   │   └── prop-beta1-visual.png
│   ├── Docking scores/
│   │   ├── curcumin-mmp8.pdbqt
│   │   └── propranolol.pdbqt
│   ├── hits/
│   │   ├── curcumin.sdf
│   │   ├── propranolol.sdf
│   │   └── tannic-acid-2D.sdf
│   ├── hits opt/
│   │   ├── curcumin-opt.acesin
│   │   ├── curcumin-opt.mol2
│   │   └── propranolol.mol2
│   ├── Receptor binding analysis/
│   │   ├── curcumin.conf
│   │   ├── curcumin.ligand.pdbqt
│   │   ├── curcumin.pdbqt
│   │   ├── curcumin.receptor.pdbqt
│   │   ├── propranolol.conf
│   │   ├── propranolol.ligand.pdbqt
│   │   ├── propranolol.pdbqt
│   │   └── propranolol.receptor.pdbqt
│   └── receptors/
│       ├── beta1_adreno.ent
│       └── mmp-8.ent
└── Vina/
```

## Docking Score Analysis (from `tests/Docking scores`)

AutoDock Vina outputs were parsed from:
- `tests/Docking scores/curcumin-mmp8.pdbqt`
- `tests/Docking scores/propranolol.pdbqt`

### 1) Curcumin vs MMP-8
Pose energies (kcal/mol):
- -7.7
- -7.7
- -7.7
- -7.5
- -7.5
- -7.5
- -7.4
- -7.4
- -7.3

Summary:
- Best affinity: `-7.7 kcal/mol`
- Worst reported pose: `-7.3 kcal/mol`
- Tight score spread (~0.4 kcal/mol across top 9 poses), suggesting consistent binding modes.

### 2) Propranolol vs beta1-adrenergic receptor
Pose energies (kcal/mol):
- -7.6
- -7.2
- -7.0
- -6.9
- -6.9
- -6.9
- -6.8
- -6.7
- -6.7

Summary:
- Best affinity: `-7.6 kcal/mol`
- Worst reported pose: `-6.7 kcal/mol`
- Wider spread (~0.9 kcal/mol), indicating more conformational variability than curcumin in this run.

### Quick comparison
- Curcumin shows the most favorable single score in this dataset (`-7.7` vs `-7.6 kcal/mol`).
- Curcumin also shows tighter clustering across modes.
- These are docking estimates only; they are not proof of biological efficacy.

## Docking Run Settings Used

From config files in `tests/Receptor binding analysis/`:

### Curcumin run (`curcumin.conf`)
- center_x = 17.60
- center_y = 58.36
- center_z = 51.86
- size_x = 30.38
- size_y = 35.22
- size_z = 33.92
- energy_range = 3
- exhaustiveness = 8
- num_modes = 9

### Propranolol run (`propranolol.conf`)
- center_x = 28.09
- center_y = -39.12
- center_z = 40.13
- size_x = 58.50
- size_y = 64.66
- size_z = 170.76
- energy_range = 3
- exhaustiveness = 8
- num_modes = 9

## Receptor Metadata Confirmed
- `tests/receptors/mmp-8.ent`: human MMP-8 structure (`PDB: 1A85`, X-ray, 2.00 A)
- `tests/receptors/beta1_adreno.ent`: human beta1-adrenergic receptor chimera (`PDB: 7BVQ`, X-ray, 2.50 A)

## Visual Interaction Outputs

Generated images in `tests/docking complex/`:
- `curcumin-mmp8-visual.png`
- `prop-beta1-visual.png`

![Curcumin-MMP8 docking visualization](tests/docking%20complex/curcumin-mmp8-visual.png)
![Propranolol-beta1 docking visualization](tests/docking%20complex/prop-beta1-visual.png)

From the provided 2D interaction diagrams:
- Curcumin-MMP8 shows hydrogen-bonding and aromatic contacts (including interactions around residues such as TYR A:227, ASN A:226, PHE A:192, and nearby van der Waals contacts).
- Propranolol-beta1 shows hydrogen-bonding and aromatic/hydrophobic contacts (including residues such as ASP B:1138, TRP B:1337, PHE B:1218, PHE B:1340, and PHE B:1341).

These visuals support the docking score outputs by showing plausible binding-contact networks for both complexes.

## Notes On Other Readable Content
- `Resources/Computational Wound Healing Phytochemical Research Strategy.md` contains the broader strategic framework and literature-style background.
- Current executable data assets are concentrated in `tests/` (ligands, optimized structures, receptors, Vina inputs, and docking outputs).

## Automated Score Extraction

A parser script has been added to make docking score reporting reproducible:
- Script: `scripts/parse_vina_scores.py`
- Run command: `python scripts/parse_vina_scores.py`

Generated outputs:
- `results/vina_score_summary.csv` (per-file summary stats)
- `results/vina_pose_scores.csv` (one row per docking pose)

Current run detected 4 files containing Vina score records (including mirrored result files in `tests/Docking scores/` and `tests/Receptor binding analysis/`).

## Next Technical Steps
1. Add optional deduplication/labeling in the parser so mirrored outputs can be grouped as primary vs backup result files.
2. Standardize result folders (for example: `results/scores`, `results/figures`, `results/interactions`) to align with manuscript-ready reporting.
3. Add ADMET and target selectivity filtering for current hits (curcumin, propranolol, tannic acid candidates).

## Disclaimer
This repository contains in silico docking outputs for research and learning purposes. Docking scores are hypothesis-generating and must be validated through wet-lab assays and pharmacological testing.
