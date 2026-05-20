from malsim.config import TTCMode
from malsim.config.sim_settings import AttackSurfaceSettings
import pytest
from malsim import MalSimulatorSettings, Scenario, MalSimulator

attack_mapping = {
            "scenarios/apt29_scenario1.yml": "attacks/apt29_scenario1.txt",
            "scenarios/apt29_scenario2.yml": "attacks/apt29_scenario2.txt",
            "scenarios/blind_eagle.yml": "attacks/blind_eagle.txt",
            "scenarios/carbank_scenario1.yml": "attacks/carbank_scenario1.txt",
            "scenarios/fin6_phase1_and_2.yml": "attacks/fin6_phase1_and_2.txt",
            "scenarios/fin7_scenario1.yml": "attacks/fin7_scenario1.txt",
            "scenarios/menuPass_scenario1.yml": "attacks/menuPass_scenario1.txt",
            "scenarios/ocean_lotus.yml": "attacks/ocean_lotus.txt",
            "scenarios/oilrig.yml": "attacks/oilrig.txt",
            "scenarios/sandworm_scenario1.yml": "attacks/sandworm_scenario1.txt",
            "scenarios/turla_scenario_carbon.yml": "attacks/turla_scenario_carbon.txt",
            "scenarios/turla_scenario_snake.yml": "attacks/turla_scenario_snake.txt",
            "scenarios/wizard_spider_scenario1.yml": "attacks/wizard_spider_scenario1.txt",
        }

SIM_SETTINGS = MalSimulatorSettings(
            ttc_mode=TTCMode.DISABLED,
            run_defense_step_bernoullis=False,
            run_attack_step_bernoullis=False,
            attack_surface=AttackSurfaceSettings(
                skip_unnecessary=False,
            ),
            compromise_entrypoints_at_start=True,
        )


@pytest.mark.parametrize("scenario_file, attack_file", attack_mapping.items())
def test_verify_attack(scenario_file: str, attack_file: str) -> bool:
    scenario = Scenario.load_from_file(scenario_file)
    attacker_name = list(scenario.attacker_settings.keys())[0]

    attack_node_names = open(attack_file).read().splitlines()
    attack_node_names = [node_name.strip() for node_name in attack_node_names if not node_name.startswith("#") and not node_name.startswith("-")]
    attack_node_names = [node_name for node_name in attack_node_names if len(node_name) > 0]

    
    sim = MalSimulator.from_scenario(scenario, sim_settings=SIM_SETTINGS)
    state = sim.reset()[attacker_name]

    for node_name in attack_node_names:
        action = sim.get_node(node_name)
        state = sim.step({attacker_name: [action]})[attacker_name]
        assert any(action.id == node.id for node in state.performed_nodes), f"Action {action.id} not found in performed nodes"

    assert sim.agent_is_terminated(attacker_name), f"Attacker {attacker_name} not terminated"
        