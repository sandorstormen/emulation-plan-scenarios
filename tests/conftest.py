from malsim import MalSimulatorSettings
from malsim.config import TTCMode
from malsim.config.sim_settings import AttackSurfaceSettings

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

sim_settings = MalSimulatorSettings(
    ttc_mode=TTCMode.DISABLED,
    run_defense_step_bernoullis=False,
    run_attack_step_bernoullis=False,
    attack_surface=AttackSurfaceSettings(
        skip_unnecessary=False,
    ),
    compromise_entrypoints_at_start=True,
)
