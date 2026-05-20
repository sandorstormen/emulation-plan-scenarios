import pytest
from malsim import MalSimulator, Scenario

from conftest import attack_mapping, sim_settings


@pytest.mark.parametrize("scenario_file, attack_file", attack_mapping.items())
def test_verify_attack(scenario_file: str, attack_file: str) -> bool:
    scenario = Scenario.load_from_file(scenario_file)
    attacker_name = list(scenario.attacker_settings.keys())[0]

    attack_node_names = open(attack_file).read().splitlines()
    attack_node_names = [node_name.strip() for node_name in attack_node_names if not node_name.startswith("#") and not node_name.startswith("-")]
    attack_node_names = [node_name for node_name in attack_node_names if len(node_name) > 0]

    
    sim = MalSimulator.from_scenario(scenario, sim_settings=sim_settings)
    state = sim.reset()[attacker_name]

    for node_name in attack_node_names:
        action = sim.get_node(node_name)
        state = sim.step({attacker_name: [action]})[attacker_name]
        assert any(action.id == node.id for node in state.performed_nodes), f"Action {action.id} not found in performed nodes"

    assert sim.agent_is_terminated(attacker_name), f"Attacker {attacker_name} not terminated"
        
