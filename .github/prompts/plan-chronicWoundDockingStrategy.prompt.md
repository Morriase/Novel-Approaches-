## Plan: Non-ML Chronic Wound Docking Roadmap

Use a research-first, non-ML workflow centered on reproducibility, controls, selectivity, and translational interpretation. Build confidence in current lead (quercetin-MMP9) before adding complexity.

**Steps**
1. Phase 1 (Week 1-2): Lock reproducibility package.
2. Write docs/METHODS.md with software versions, exact commands, parameter rationale, receptor prep choices, and pose-selection rule. *blocks all later claims*
3. Write docs/DECISION_LOG.md with dated promote/hold/control decisions and rationale. *parallel with step 2*
4. Execute Phase 1 layout migration in copy-first mode per docs/REPOSITORY_MIGRATION_PLAN.md. Keep legacy tests paths until parser fallback is validated. *depends on 2*
5. Update scripts/parse_vina_scores.py defaults to canonical folders with backward-compatible fallback. Regenerate results CSVs and verify row counts.
6. Phase 2 (Week 3-4): Add structural rigor.
7. Build interaction quantification table for each top pose (HBond distances, aromatic/hydrophobic contacts, key residues). Export CSV under results/summaries.
8. Add residue-contact check (<=5 A shell) to confirm active-site occupancy versus off-site docking. *depends on 7*
9. Perform pose clustering (RMSD-based) to confirm whether top modes are stable or divergent. *parallel with 8*
10. Phase 3 (Week 5-7): Add controls and selectivity.
11. Positive control docking: known MMP inhibitor (e.g., GM6001/Marimastat) against MMP9 receptor to benchmark expected affinity behavior.
12. Negative control docking: 3-5 weakly relevant molecules to ensure score discrimination.
13. Off-target panel docking (MMP1/MMP2 and one non-MMP protease) for quercetin and curcumin to estimate selectivity risk.
14. Phase 4 (Week 8-9): Add developability filters.
15. Run SwissADME and ProTox for prioritized compounds; summarize liabilities and topical-delivery implications.
16. Integrate ADME/Tox outcomes into candidate rank table and DECISION_LOG promote/hold status.
17. Phase 5 (Week 10-12): Prepare translational handoff.
18. Produce mechanism map linking observed residue contacts to wound-healing hypothesis (MMP-9 modulation -> ECM preservation -> improved re-epithelialization hypothesis).
19. Draft wet-lab handoff package: assay suggestions (MMP9 enzyme inhibition, zymography, keratinocyte migration context), expected readouts, go/no-go criteria.

**Relevant files**
- c:/Users/Morris/Desktop/Novel Approaches for chronic wound healing/README.md — public-facing study summary and decision snapshots.
- c:/Users/Morris/Desktop/Novel Approaches for chronic wound healing/docs/REPOSITORY_MIGRATION_PLAN.md — canonical folder transition protocol.
- c:/Users/Morris/Desktop/Novel Approaches for chronic wound healing/scripts/parse_vina_scores.py — score extraction and reproducibility anchor.
- c:/Users/Morris/Desktop/Novel Approaches for chronic wound healing/results/vina_score_summary.csv — per-run quantitative leaderboard.
- c:/Users/Morris/Desktop/Novel Approaches for chronic wound healing/tests/Receptor binding analysis/quercetin.conf — current lead docking settings.

**Verification**
1. Re-run parser and confirm expected runs are present in summary CSV (including quercetin and mirrored files).
2. Confirm every lead claim in README has a corresponding source artifact and one quantitative table.
3. Confirm controls (positive and negative) are present and scored before declaring candidate confidence.
4. Confirm ADME/Tox records exist for top-ranked compounds and are reflected in final rank status.

**Decisions**
- Include: non-ML experimental strategy, reproducibility, controls, selectivity, ADME/Tox, translational handoff.
- Exclude for now: custom ML models, generative ligand design, neural scoring.
- Propranolol is retained as workflow control only, not as therapeutic lead.

**Further Considerations**
1. Optional ML trigger: only if you accumulate >=20 ligands with measured IC50/Kd (not docking-only labels).
2. Priority recommendation: finish reproducibility + controls before expanding compound library.
3. Publication readiness threshold: methods locked, controls passed, selectivity profile documented.
