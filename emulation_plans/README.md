# Emulation Plans

Emulation plans from here: [https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master)

| Scenario | Initial Compromise | Strategy | Goal | Target System Hosts | Target Org. |
|---|---|---|---|---|---|
| **APT29 Scenario 1** | Widespread Phishing | Rapid collection then stealthy | Data exfiltration, Persistence | 2 Domain-joined Windows Workstations, 1 Domain Controller | - |
| **APT29 Scenario 2** | Spear Phishing | Stealthy, Slow and Methodical | Data exfiltration, Persistence | 2 Domain-joined Windows Workstations, 1 Domain Controller | - |
| **Blind Eagle** | Spear Phishing | Opportunistic, single-host |  Credential Theft & Persistence | 1 Windows Workstation, 1 Linux Web Server, 1 Domain Controller, 1 Echange Server, Hosts are domain-joined | Bank Network |
| **Carbanak** | Spear Phishing | Patient | Financial theft, Persistence | 1 Domain Controller, 2 Domain-joined Windows Workstations (HR Manager, CFO), 1 Linux Bank File Server | Bank / Financial Institution |
| **FIN6** | Assumed breach with C2 (no speficic tactic) | "Seek-and-Deploy": compromise system then establish intended impact | Phase 1: Discovery data and NTDS.dit exfiltration. Phase 2: Credential theft then ransomware | 1 Domain Controller, 1 Domain-joined Windows Workstation, 1 Windows POS system, 1 E-commerce web server, 1 Windows servers | Retail / Hospitality / E-commerce |
| **FIN7** | Spear Phishing | Evasive, targeted | Data exfiltration, Persistence | 1 Domain Controller, 3 Domain-joined Windows 10 Workstations (Hotel Manager, IT Admin, Accounting) | Hotel Manager Network |
| **menuPass Scenario 1** | Trusted relationship abuse (MSP to subscriber network) | Stealthy, blends in with routine admin activity | Data exfiltration, Persistence | (Inferred) 1 Initially accessed Windows Host, 1 Windows System of Interest, 1 Domain Controller, Hosts are domain-joined, MSP network and hosts | MSP Subscriber Network |
| **OceanLotus** | Phishing (delivery not emulated) | - | Data exfiltration, Persistence | 1 macOS Workstation (Hope Potter), 1 Linux File Server | - |
| **OilRig** | Spear Phishing (delivery not emulated) | - | Data exfiltration, Persistence | 1 Domain Controller, 1 Domain-joined Windows 10 Exchange Admin Workstation (Gosta), 1 Domain-joined Windows Exchange Server (EWS), 1 Domain-joined SQL Server | - |
| **Sandworm** | Credential Access | - | Credential theft, Persistence, Destructive impact | 1 Linux Server (CentOS 7, Caladan), 1 Domain Controller (Arrakis), 2 Domain-joined Windows 10 Workstations (Gammu - Frank Herbert, Quadra) | - |
| **Turla Carbon** | Spear Phishing | Multi-phase, Evasive | Credential theft, Persistence, Staging for Other Victims | 1 Domain Controller (Bannik), 2 Domain-joined Windows 10 Workstations (Hobgoblin - Gunter, Khabibulin - Adalwolfa), 1 Linux Apache Web Server (Kagarov) | - |
| **Turla Snake** | Drive-by Compromise (watering hole) | Multi-phase | Data exfiltration (email collection), Persistence | 1 Domain Controller, 1 IIS Server, 1 Exchange Server, 2 Windows Admin Workstations (IIS Admin - Eglė, Exchange Admin - Žilvinas) | News Organisation |
| **Wizard Spider** | Phishing (delivery not emulated) | Fast, Domain Controller-first | Credential theft, Data exfiltration, Ransomware | 1 Domain Controller (wizard), 2 Domain-joined Windows 10 Workstations (Dorothy, Toto) | - |

## License and credits

These emulation plans come from the [Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master) of the MITRE Center for Threat-Informed Defense. They are © The MITRE Corporation and used here under the [Apache License 2.0](LICENSE). Full credit goes to the original authors. Only the written descriptions are included here. Payloads, source code and other technical files from the original library are omitted, and the descriptions are otherwise unchanged. The `LICENSE` and `NOTICE` files in each plan's folder are kept as in the original and list the specific credits for that plan. Inclusion here is not an endorsement by MITRE.
