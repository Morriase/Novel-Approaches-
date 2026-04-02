# Decision Log

## Purpose
Track dated project decisions for candidate prioritization, controls, and workflow changes.

## Decision Records

| Date | Decision | Rationale | Status |
|---|---|---|---|
| 2026-04-02 | Prioritize quercetin vs MMP-9 as primary lead line | Strongest current docking signal in repo (best affinity -9.7 kcal/mol) and supportive interaction-map plausibility | Active |
| 2026-04-02 | Retain curcumin vs MMP-8 as comparator line | Useful biological comparator scaffold with stable score spread and existing prepared artifacts | Active |
| 2026-04-02 | Keep propranolol vs beta1-AR as workflow control only | Used to validate end-to-end docking pipeline; excluded from wound-healing lead interpretation | Control |
| 2026-04-02 | Exclude custom ML from current phase | Dataset size and label quality are not sufficient for justified ML modeling; non-ML path improves interpretability and reproducibility | Active policy |
| 2026-04-02 | Start copy-first repository migration to canonical research layout | Reduce structure drift while preserving legacy compatibility and traceability | In progress |
| 2026-04-02 | Adopt parser precedence: canonical pose paths first, legacy fallback second | Enables transition to stable directory model without breaking existing outputs | Active |

## Candidate Ranking Rule
Current ranking policy:
1. Most negative best affinity first.
2. Then score consistency across poses (spread).
3. Then interaction plausibility from contact maps.

## Promotion / Hold Criteria (Current)
- Promote: strong affinity signal with plausible active-site interactions and no immediate ADME/Tox red flags.
- Hold: acceptable docking score but insufficient controls, selectivity, or developability evidence.
- Control-only: used for pipeline validation, not therapeutic inference.

## Pending Decisions (Next)
1. Select and approve one positive MMP inhibitor control compound.
2. Select 3-5 negative/decoy compounds for score discrimination checks.
3. Finalize off-target mini-panel for selectivity screening.
4. Confirm ADME/Tox gate thresholds for promote vs hold decisions.