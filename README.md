# Novel Approaches for Chronic Wound Healing: Computational Phytochemical Discovery

## Research-First Repository Layout

This repository is organized as a computational research dossier, not a software product. The structure is designed to make scientific logic, evidence quality, and decision flow easy to audit.

### 1) Project frame
- Clinical problem: persistent inflammatory and proteolytic imbalance in chronic wounds.
- Discovery focus: phytochemical modulation of matrix metalloproteinase targets, currently emphasizing MMP-9 and MMP-8.
- Evidence type in this phase: in silico docking and interaction mapping.

### 2) Evidence hierarchy used here
1. Target selection rationale and receptor provenance.
2. Ligand source and optimization records.
3. Docking parameter transparency (.conf files).
4. Pose-level affinity outputs (PDBQT + CSV).
5. Interaction-map plausibility checks (2D/3D visuals).
6. Candidate ranking with explicit decision rule.

### 3) Repository architecture model

| Layer | Purpose | Current location in this repo |
|---|---|---|
| Scientific strategy | Literature-backed rationale and long-form framing | Resources/ and Research materials/ |
| Input chemistry | Raw and optimized ligand structures | tests/hits/ and tests/hits opt/ |
| Target structures | Receptor structures and optimized variants | tests/receptors/ |
| Docking setup | Grid center, box size, and run controls | tests/Receptor binding analysis/*.conf |
| Raw docking outputs | Pose-ranked Vina outputs | tests/Docking scores/ and tests/Receptor binding analysis/ |
| Visual validation | Complex render + interaction map panels | tests/docking complex/ |
| Quant summaries | Reproducible score tables from parser | results/ |

### 4) Reporting standard for each new experiment
For each new ligand-target run, record the same five blocks:
1. Biological intent: why this target in wound context.
2. Technical setup: receptor ID, ligand file, docking box, Vina parameters.
3. Quantitative result: best, mean, spread, and pose count.
4. Structural plausibility: key interaction classes from visualization.
5. Decision outcome: promote, hold, or control-only.

### 5) Why this layout fits this project
- It prioritizes scientific traceability over software engineering complexity.
- It preserves reproducibility while remaining readable for non-programmer reviewers.
- It supports portfolio review by supervisors, labs, and translational collaborators.

### 6) Physical structure migration plan
A concrete folder migration blueprint is available at `docs/REPOSITORY_MIGRATION_PLAN.md`.
It defines target directories, source-to-target mapping, phased execution, and risk controls so this repository can transition into a publication-style research layout without losing legacy traceability.

## Today Snapshot (April 2026)

### Quick update
- Added a new primary docking experiment: `quercetin` against human `MMP-9`.
- Best Vina score observed for this run: `-9.7 kcal/mol` (9 reported poses, range `-9.7` to `-8.6`).
- Added new structure and visualization assets for the quercetin-MMP9 system.
- Re-ran the parser script and refreshed CSV outputs.
- `Propranolol` remains in this repository as a pipeline-control/reference run and is not used as a lead candidate in the current biological interpretation.

### Prioritized candidates (quick view)

| Rank | Candidate | Target | Best Vina score (kcal/mol) | Mean score (kcal/mol) | Current role |
|---|---|---|---:|---:|---|
| 1 | Quercetin | MMP-9 (1GKC) | -9.7 | -9.122 | Primary lead from current in silico screen |
| 2 | Curcumin | MMP-8 (1A85) | -7.7 | -7.522 | Comparator lead and scaffold reference |
| Control | Propranolol | beta1-AR (7BVQ) | -7.6 | -6.967 | Pipeline validation reference (non-priority for wound targeting) |

Decision rule used for ranking: prioritize lower (more negative) best affinity first, then consistency across poses (tighter spread), then interaction plausibility in 2D/3D contact maps.

### Scientific breakdown (detailed)
Chronic wound pathology is strongly associated with protease imbalance, especially excessive matrix degradation by MMP family members. In this update, we expanded from MMP-8 testing to MMP-9-focused docking by introducing quercetin against an MMP-9 catalytic-domain structure (`PDB: 1GKC`, X-ray 2.30 A).

The quercetin docking profile is substantially more favorable than the prior curcumin-MMP8 baseline in terms of predicted binding free energy from Vina:
- Quercetin-MMP9 best pose: `-9.7 kcal/mol`
- Curcumin-MMP8 best pose: `-7.7 kcal/mol`

The score delta is approximately `2.0 kcal/mol`, which in docking terms suggests stronger predicted interaction potential for quercetin in this modeled MMP-9 pocket. The quercetin pose distribution also spans multiple geometries (`RMSD upper bound` values up to ~35 A in alternate modes), indicating several plausible conformational placements while retaining strong top-ranked affinity.

From the interaction map image, quercetin is supported by a mixed interaction network, including:
- Conventional hydrogen bonding
- Aromatic interactions (pi-pi and pi-alkyl classes)
- Additional electrostatic support (pi-anion contact reported in the legend)

This profile is mechanistically aligned with a polyphenol scaffold engaging a catalytic cleft through both polar and aromatic contacts. While docking cannot prove inhibition, the combined affinity and interaction-pattern evidence makes quercetin-MMP9 the strongest in silico signal in the current dataset.

### Non-technical breakdown (plain language)
We tested a new natural compound, quercetin, against a wound-related enzyme target (MMP-9). In the computer simulation, quercetin attached to the target more strongly than our earlier curcumin test. That means quercetin currently looks like the better candidate to keep investigating.

The propranolol run was kept only to confirm the pipeline still works end-to-end. It is not the compound we are prioritizing for wound-healing discovery.

## Current Project Status (April 2026)
This repository now reflects a practical docking-focused workflow completed in the `tests/` workspace.

Active receptor-ligand systems in scope:
- `Curcumin` docked against human `MMP-8` (receptor source: `1A85`)
- `Quercetin` docked against human `MMP-9` (receptor source: `1GKC`)

Pipeline-control/reference system retained in repo:
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
│   │   ├── quercetin-mmp9.pdbqt
│   │   └── propranolol.pdbqt
│   ├── hits/
│   │   ├── curcumin.sdf
│   │   ├── propranolol.sdf
│   │   └── tannic-acid-2D.sdf
│   ├── hits opt/
│   │   ├── curcumin-opt.acesin
│   │   ├── curcumin-opt.mol2
│   │   ├── quercetin.mol2
│   │   └── propranolol.mol2
│   ├── Receptor binding analysis/
│   │   ├── curcumin.conf
│   │   ├── curcumin.ligand.pdbqt
│   │   ├── curcumin.pdbqt
│   │   ├── curcumin.receptor.pdbqt
│   │   ├── propranolol.conf
│   │   ├── propranolol.ligand.pdbqt
│   │   ├── propranolol.pdbqt
│   │   ├── propranolol.receptor.pdbqt
│   │   ├── quercetin.conf
│   │   ├── quercetin.ligand.pdbqt
│   │   ├── quercetin.pdbqt
│   │   └── quercetin.receptor.pdbqt
│   └── receptors/
│       ├── beta1_adreno.ent
│       ├── MMP-9.ent
│       └── mmp-8.ent
└── Vina/
```

## Docking Score Analysis (from `tests/Docking scores`)

AutoDock Vina outputs were parsed from:
- `tests/Docking scores/curcumin-mmp8.pdbqt`
- `tests/Docking scores/quercetin-mmp9.pdbqt`
- `tests/Docking scores/propranolol.pdbqt` (pipeline control)

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

### 3) Quercetin vs MMP-9
Pose energies (kcal/mol):
- -9.7
- -9.6
- -9.5
- -9.2
- -9.1
- -9.0
- -8.7
- -8.7
- -8.6

Summary:
- Best affinity: `-9.7 kcal/mol`
- Worst reported pose: `-8.6 kcal/mol`
- Score spread: `1.1 kcal/mol`
- Mean affinity (CSV): `-9.122 kcal/mol`

### Quick comparison
- Quercetin-MMP9 currently has the strongest top-ranked score in this repository (`-9.7 kcal/mol`).
- Curcumin-MMP8 remains a useful comparator with tighter clustering (`0.4 kcal/mol spread`).
- Propranolol is retained as a pipeline-control/reference run, not a prioritized wound-healing lead.
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

### Quercetin run (`quercetin.conf`)
- center_x = 54.69
- center_y = 20.86
- center_z = 129.22
- size_x = 46.03
- size_y = 39.72
- size_z = 68.13
- energy_range = 3
- exhaustiveness = 8
- num_modes = 9

## Receptor Metadata Confirmed
- `tests/receptors/mmp-8.ent`: human MMP-8 structure (`PDB: 1A85`, X-ray, 2.00 A)
- `tests/receptors/MMP-9.ent`: human MMP-9 catalytic domain (`PDB: 1GKC`, X-ray, 2.30 A)
- `tests/receptors/beta1_adreno.ent`: human beta1-adrenergic receptor chimera (`PDB: 7BVQ`, X-ray, 2.50 A)

## Visual Interaction Outputs

Generated images in `tests/docking complex/`:
- `curcumin-mmp8-visual.png`
- `quarcetin-mmp9-visual.png`
- `prop-beta1-visual.png`

![Curcumin-MMP8 docking visualization](tests/docking%20complex/curcumin-mmp8-visual.png)
![Quercetin-MMP9 docking visualization](tests/docking%20complex/quarcetin-mmp9-visual.png)
![Propranolol-beta1 docking visualization](tests/docking%20complex/prop-beta1-visual.png)

From the provided 2D interaction diagrams:
- Curcumin-MMP8 shows hydrogen-bonding and aromatic contacts (including interactions around residues such as TYR A:227, ASN A:226, PHE A:192, and nearby van der Waals contacts).
- Quercetin-MMP9 shows a mixed contact network including conventional hydrogen bonding, pi-pi / pi-alkyl contacts, and a pi-anion interaction (for example around residues GLU B:402, HIS B:401, TYR B:423, PRO B:415, and neighboring pocket residues).
- Propranolol-beta1 shows hydrogen-bonding and aromatic/hydrophobic contacts (including residues such as ASP B:1138, TRP B:1337, PHE B:1218, PHE B:1340, and PHE B:1341).

These visuals support the docking score outputs by showing plausible binding-contact networks for all docked complexes.

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

Current run detected 6 files containing Vina score records (including mirrored result files in `tests/Docking scores/` and `tests/Receptor binding analysis/`).

## Next Technical Steps
1. Add optional deduplication/labeling in the parser so mirrored outputs can be grouped as primary vs backup result files.
2. Standardize result folders (for example: `results/scores`, `results/figures`, `results/interactions`) to align with manuscript-ready reporting.
3. Add ADMET and target selectivity filtering for prioritized hits (quercetin, curcumin, and tannic acid candidates).

## Disclaimer
This repository contains in silico docking outputs for research and learning purposes. Docking scores are hypothesis-generating and must be validated through wet-lab assays and pharmacological testing.
