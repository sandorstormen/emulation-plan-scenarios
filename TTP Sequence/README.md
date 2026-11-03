# TTP Sequence

Ordered MITRE ATT&CK technique IDs used in each scenario of the emulation plans in `emulation_plans/`, grouped by the plan's steps. Technique names and statuses come from the ATT&CK Enterprise version each plan declares (`attack_version` in its CALDERA yaml), noted at the top of each file: FIN6 v7.2; Sandworm and Wizard Spider v8.0; Carbanak, FIN7 and menuPass v8.1; APT29 v7.0 (the plan mixes v6 IDs with sub-technique IDs; v7.0 is the earliest version where all cited IDs exist, and no TTP is omitted); OilRig v11.3; Turla v13.1. Blind Eagle and OceanLotus state no version, so v13.1 is assumed. IDs that are revoked or deprecated in that version are marked, with the replacement where ATT&CK names one.

| File | Plan source | Notes |
|---|---|---|
| `apt29_scenario1.md`, `apt29_scenario2.md` | Scenario 1 and 2 READMEs | IDs from the step text |
| `blind_eagle.md` | `Blind_Eagle_Scenario.md` | Plan cites `T1024.002`, a typo for `T1204.002` |
| `carbanak_scenario1.md` | Scenario 1 README | Scenario 1 used (plan has two) |
| `fin6.md` | `Phase1.md` + `Phase2.md` | Both phases |
| `fin7_scenario1.md` | Scenario 1 README | Scenario 1 used (plan has two) |
| `menupass_scenario1.md` | `Scenario1.md` | |
| `ocean_lotus.md` | `OceanLotus_Scenario.md` | |
| `oilrig.md`, `sandworm_scenario1.md`, `turla_carbon.md`, `turla_snake.md`, `wizard_spider_scenario1.md` | CALDERA `yaml` abilities | The plan text cites no IDs, so IDs come from `attack_id` in the yaml, restricted to the steps in the scenario README. Steps with no yaml ability, or an ability without an ID (`x`), are omitted. Turla uses the Detections variant. |

"(repeat)" marks a technique already listed in an earlier step. Numbering counts every listed occurrence.
