# APT Emulation Plan Scenarios

These are scenarios made for the [`mal-simulator`](https://github.com/mal-lang/mal-simulator) [v2.3.0](https://pypi.org/project/mal-simulator/2.3.0/) based on CTID emulation plans. The [MITRE Center for Threat-Informed Defense (Center)](https://ctid.mitre.org/) has created the [emulation plans](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master) to represent particular [*Advanced Persistent Threats* (*APTs*)](https://en.wikipedia.org/wiki/Advanced_persistent_threat), which a description of a system and instructions on how to hack it in a manner that a particular *APT* would. The emulation plans are modelled in [minCoreLang](https://github.com/sandorstormen/minCoreLang), a minimized version of [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) following the [*Meta Attack Language* (*MAL*)](https://www.sciencedirect.com/science/article/pii/S0167404823001943) specification. [minCoreLang](https://github.com/sandorstormen/minCoreLang) is a minimized version of [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) that cuts out Groups/Permissions asset types as well as supply chain/IDPS attack vector modelling. The scenarios are still fully compatible with [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) and can use it instead of [minCoreLang](https://github.com/sandorstormen/minCoreLang).

# Modelling Modus

The scenarios were modeled to be representative of the attacks describe in the emulation plans. Therefore, only system components mentioned in the emulation plan was included in the instance models of the sencarios. Any part of the attack that is an aspect not represented in [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) was not included in the scenarios.

# Attacks

The attacks are `txt`-files wich lists attack steps. These sequences of attack steps are supposed to represent the actions taken by different *APTs* to perform the attack.


# APT Emulation Plan Scenarios

These scenarios are designed for the [`mal-simulator`](https://github.com/mal-lang/mal-simulator) [v2.3.0](https://pypi.org/project/mal-simulator/2.3.0/) and are based on CTID emulation plans. The [MITRE Center for Threat-Informed Defense (Center)](https://ctid.mitre.org/) has developed these [emulation plans](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master) to represent specific [*Advanced Persistent Threats* (*APTs*)](https://en.wikipedia.org/wiki/Advanced_persistent_threat). Each plan includes a system description and step-by-step instructions for simulating how a particular APT would compromise that system.

The emulation plans are modeled in [minCoreLang](https://github.com/sandorstormen/minCoreLang), a minimized version of [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) based on the [*Meta Attack Language* (*MAL*)](https://www.sciencedirect.com/science/article/pii/S0167404823001943) specification. minCoreLang removes certain asset types (e.g., Groups and Permissions) as well as supply chain and IDPS attack vector modeling. The scenarios remain fully compatible with coreLang and can be executed using either language.

# Modeling Approach

The scenarios were modeled to be representative of the attacks describe in the emulation plans. Therefore, only system components mentioned in each emulation plan are included in the corresponding instance models. Any part of the attack that is an aspect not represented in [coreLang](https://www.sciencedirect.com/science/article/pii/S0167404824003626) was not included in the scenarios.

# Attacks

The attacks are given as `.txt` files that list sequences of attack steps. These sequences represent the actions performed by different APTs during the simulated attacks.