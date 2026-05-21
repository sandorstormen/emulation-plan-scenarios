from pathlib import Path
from malsim.config import TTCMode
from malsim.config.sim_settings import AttackSurfaceSettings
from malsim.mal_simulator import RewardMode
from malsim.scenario import Scenario
from maltoolbox.attackgraph import AttackGraphNode
from maltoolbox.attackgraph.node import AttackGraphNode

from malsim import MalSimulator, MalSimulatorSettings, Scenario

scenario_file = "scenarios/apt29_scenario2.yml"
attack_file = "attacks/apt29_scenario2.txt"

scenario = Scenario.load_from_file(scenario_file)
scenario.attack_graph.save_to_file("logs/attack_graph.yml")
for agent_settings in scenario.agent_settings:
    agent_settings.reward_mode = RewardMode.EXPECTED_TTC
sim = MalSimulator.from_scenario(
    scenario,
    sim_settings=MalSimulatorSettings(
        ttc_mode=TTCMode.DISABLED,
        run_defense_step_bernoullis=False,
        run_attack_step_bernoullis=False,
        attack_surface=AttackSurfaceSettings(
            skip_unnecessary=False,
        ),
        compromise_entrypoints_at_start=True,
    ),
)
attacker_name = list(scenario.attacker_settings.keys())[0]


def print_names(action_surface: list[AttackGraphNode]):
    for i, node in enumerate(action_surface):
        print(f"{i}: {node.full_name}")


save_file = Path("logs") / "_".join(
    [scenario.attack_graph.model.name, attacker_name, "temp_record", ".txt"]
)


def print_node_attrs(node: AttackGraphNode):
    print(
        f"{node.full_name} - Type: {node.type}, Viability: {sim.node_is_viable(node)}, Necessity: {sim.node_is_necessary(node)}"
    )


def print_neccesity_of_parents(node: AttackGraphNode):
    for parent in node.parents:
        print(f"{parent.type} {parent.full_name}: {sim.node_is_necessary(parent)}")


# # AG DEBUGGING
# ag = sim.attack_graph
# pos_guess_creds = sim.attack_graph.get_node_by_full_name("POS System Admin Credentials:guessCredentials")
# print_node_attrs(pos_guess_creds)
# pos_not_guessable = sim.attack_graph.get_node_by_full_name("POS System Admin Credentials:notGuessable")
# print_node_attrs(pos_not_guessable)
# pos_weak_credentials = sim.attack_graph.get_node_by_full_name("POS System Admin Credentials:weakCredentials")
# print_node_attrs(pos_weak_credentials)
# pos_guess_creds_from_hash = sim.attack_graph.get_node_by_full_name("POS System Admin Credentials:guessCredentialsFromHash")
# print_node_attrs(pos_guess_creds_from_hash)
# # AG DEBUGGING

state = sim.reset()[attacker_name]
action_surface = sorted(list(state.action_surface), key=lambda x: x.id)

prev_actions = open(attack_file, "r").readlines()
prev_actions = [action.strip() for action in prev_actions if action.strip()]
cum_reward = sim.agent_reward(state)
for action in prev_actions:
    if action.startswith("---") or action.startswith("#"):
        continue
    action_surface_names = [node.full_name for node in action_surface]
    try:
        action_idx = action_surface_names.index(action)
    except ValueError:
        try:
            print(
                f"Action {action} not found in action surface."
                f"Traversability={sim.node_is_traversable(state.performed_nodes, sim.get_node(action))}, "
                f"Necessity={sim.node_is_necessary(sim.get_node(action))}, "
                f"Actionability={sim.node_is_actionable(sim.get_node(action))}"
            )
        except LookupError:
            print(f"Action {action} not found in attack graph.")
        if action == "stop":
            print(f"Stopping replay")
            break
        continue
    action_node = action_surface[action_idx]
    state = sim.step({attacker_name: [action_node]})[attacker_name]
    action_surface = sorted(list(state.action_surface), key=lambda x: x.id)
    cum_reward += sim.agent_reward(state)

print(f"All goals met: {all(goal in state.performed_nodes for goal in state.goals)}")
print(f"No. goals met: {len(state.performed_nodes & state.goals)}/{len(state.goals)}")
print(f"Agent is terminated: {sim.agent_is_terminated(attacker_name)}")
print(f"Cumulative reward: {cum_reward}")
while True:
    print_names(action_surface)
    action = int(input("Enter the action number: "))
    with open(save_file, "a") as file_handle:
        file_handle.write(f"{action_surface[action].full_name}\n")
    action_node = action_surface[action]
    state = sim.step({attacker_name: [action_node]})[attacker_name]
    action_surface = sorted(
        list[AttackGraphNode](state.action_surface), key=lambda x: x.id
    )
