# FIN6 (Phase 1 and 2) - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/fin6/Emulation_Plan/Phase1.md`, `emulation_plans/fin6/Emulation_Plan/Phase2.md`.

ATT&CK version used for names: v7.2 (`attack_version` in the plan yaml).


## Step 2 - FIN6 Discovery

35 distinct techniques.

1. T1087.002 - Account Discovery: Domain Account
2. T1087 - Account Discovery
3. T1018 - Remote System Discovery
4. T1482 - Domain Trust Discovery
5. T1016 - System Network Configuration Discovery
6. T1069.002 - Permission Groups Discovery: Domain Groups
7. T1069 - Permission Groups Discovery

## Step 3 - FIN6 Privilege Escalation

8. T1134 - Access Token Manipulation
9. T1003.001 - OS Credential Dumping: LSASS Memory
10. T1003 - OS Credential Dumping
11. T1003.003 - OS Credential Dumping: NTDS

## Step 4 - FIN6 Collection and Exfiltration

12. T1560.001 - Archive Collected Data: Archive via Utility
13. T1560 - Archive Collected Data
14. T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage
15. T1567 - Exfiltration Over Web Service

## Scenario 1 - Attacking Point of Sale (POS) Systems

16. T1036.005 - Masquerading: Match Legitimate Name or Location
17. T1036 - Masquerading
18. T1036.004 - Masquerading: Masquerade Task or Service
19. T1059.001 - Command and Scripting Interpreter: PowerShell
20. T1059 - Command and Scripting Interpreter
21. T1569.002 - System Services: Service Execution
22. T1569 - System Services
23. T1047 - Windows Management Instrumentation
24. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
25. T1547 - Boot or Logon Autostart Execution
26. T1053.005 - Scheduled Task/Job: Scheduled Task
27. T1053 - Scheduled Task/Job
28. T1543.003 - Create or Modify System Process: Windows Service
29. T1543 - Create or Modify System Process
30. T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
31. T1048 - Exfiltration Over Alternative Protocol

## Scenario 2 - Attacking E-Commerce Platforms

32. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
33. T1059 - Command and Scripting Interpreter (repeat)
34. T1569.002 - System Services: Service Execution (repeat)
35. T1569 - System Services (repeat)
36. T1047 - Windows Management Instrumentation (repeat)

## Scenario 3 - Deploying Ransomware

37. T1047 - Windows Management Instrumentation (repeat)
38. T1059.003 - Command and Scripting Interpreter: Windows Command Shell
39. T1059 - Command and Scripting Interpreter (repeat)
40. T1562.001 - Impair Defenses: Disable or Modify Tools
41. T1562 - Impair Defenses
42. T1562.004 - Impair Defenses: Disable or Modify System Firewall
43. T1569.002 - System Services: Service Execution (repeat)
44. T1569 - System Services (repeat)
