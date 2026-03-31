# APT Emulation Plan Scenarios

These scenarios are designed for the [`mal-simulator`](https://github.com/mal-lang/mal-simulator) [v2.3.0](https://pypi.org/project/mal-simulator/2.3.0/) and are based on CTID emulation plans. The [MITRE Center for Threat-Informed Defense (Center)](https://ctid.mitre.org/) has developed these [emulation plans](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master) to represent specific [*Advanced Persistent Threats* (*APTs*)](https://en.wikipedia.org/wiki/Advanced_persistent_threat). Each plan includes a system description and step-by-step instructions for simulating how a particular APT would compromise that system.

The emulation plans are modeled in [minCoreLang](https://github.com/sandorstormen/minCoreLang), a minimized version of [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) based on the [*Meta Attack Language* (*MAL*)](https://www.sciencedirect.com/science/article/pii/S0167404823001943) specification. minCoreLang removes certain asset types (e.g., Groups and Permissions) as well as supply chain and IDPS attack vector modeling. The scenarios remain fully compatible with coreLang and can be executed using either language.

# Modeling Approach

The scenarios were modeled to be representative of the attacks describe in the emulation plans. Therefore, only system components mentioned in each emulation plan are included in the corresponding instance models. Any part of the attack that is an aspect not represented in [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) was not included in the scenarios.

# Attacks

The attacks are given as `.txt` files that list sequences of attack steps. These sequences represent the actions performed by different APTs during the simulated attacks.