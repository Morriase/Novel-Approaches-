# Methods

## Scope
This document captures the reproducible computational workflow used for the current chronic wound phytochemical docking phase.

## Software Environment
- OS: Windows 11 Pro 25H2 (build 26200.8039)
- Python: 3.11.9
- AutoDock Vina: 1.1.2 (May 11, 2011)
- UCSF Chimera: 1.19 (not ChimeraX)
- Avogadro2: 1.103.0
- BIOVIA: 2025 (used for visualization support)
- Auxiliary tools: none declared

## Receptors and Primary Structures
- MMP-8: PDB 1A85, source file in legacy path tests/receptors/mmp-8.ent
- MMP-9: PDB 1GKC, source file in legacy path tests/receptors/MMP-9.ent
- beta1-adrenergic receptor control: PDB 7BVQ, source file in legacy path tests/receptors/beta1_adreno.ent

## Ligands in Current Phase
- Quercetin (priority lead)
- Curcumin (comparator)
- Propranolol (pipeline control, non-priority for wound-healing interpretation)

## Docking Protocol (Current Baseline)
- Engine: AutoDock Vina 1.1.2
- energy_range: 3
- exhaustiveness: 8
- num_modes: 9

### Grid settings used
#### Curcumin (curcumin.conf)
- center_x = 17.60
- center_y = 58.36
- center_z = 51.86
- size_x = 30.38
- size_y = 35.22
- size_z = 33.92

#### Propranolol control (propranolol.conf)
- center_x = 28.09
- center_y = -39.12
- center_z = 40.13
- size_x = 58.50
- size_y = 64.66
- size_z = 170.76

#### Quercetin (quercetin.conf)
- center_x = 54.69
- center_y = 20.86
- center_z = 129.22
- size_x = 46.03
- size_y = 39.72
- size_z = 68.13

## File Locations
Canonical (Phase 1 copy-first) paths:
- Raw ligands: data/ligands/raw/
- Optimized ligands: data/ligands/optimized/
- Receptors raw: data/receptors/raw/
- Receptors prepared: data/receptors/prepared/
- Docking conf files: data/docking_inputs/conf/
- Ligand PDBQT inputs: data/docking_inputs/ligand_pdbqt/
- Receptor PDBQT inputs: data/docking_inputs/receptor_pdbqt/
- Pose outputs: results/docking/poses/
- Interaction maps: results/interactions/2d_maps/
- Complex geometries: results/interactions/3d_complexes/
- Summary tables: results/summaries/

Legacy paths remain valid during transition:
- tests/Docking scores/
- tests/Receptor binding analysis/
- tests/docking complex/

## Parsing and Quant Summary
Score extraction script:
- scripts/parse_vina_scores.py

Current default behavior (Phase 1):
- Parse from canonical pose outputs first.
- Fall back to legacy tests path if canonical pose files are unavailable.

Generated summary outputs:
- results/vina_score_summary.csv
- results/vina_pose_scores.csv
- results/summaries/vina_score_summary.csv
- results/summaries/vina_pose_scores.csv

## Pose Selection Rule (Current)
For ranking, use the most negative affinity (kcal/mol) from Vina output as the top pose score.
Tie-breakers and confidence context:
1. Tighter spread across reported modes is preferred.
2. Interaction plausibility from 2D/3D contact maps is used as qualitative support.

## Important Limitations
- Docking scores are hypothesis-generating only.
- No wet-lab validation is included in this phase.
- Control set is currently limited and will be expanded in the next phase (positive and negative controls).