# OceanLotus - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/ocean_lotus/Emulation_Plan/OceanLotus_Scenario.md`.

ATT&CK version used for names: v13.1 (not stated in the plan; assumed, see README).


## Step 1 - Establish Foothold

27 distinct techniques.

1. T1204.002 - User Execution: Malicious File
2. T1204 - User Execution
3. T1036.008 - Masquerading: Masquerade File Type
4. T1059.004 - Command and Scripting Interpreter: Unix Shell
5. T1222.002 - File and Directory Permissions Modification: Linux and Mac File and Directory Permissions Modification
6. T1543.001 - Create or Modify System Process: Launch Agent
7. T1027.009 - Obfuscated Files or Information: Embedded Payloads
8. T1070.006 - Indicator Removal: Timestomp
9. T1070 - Indicator Removal
10. T1106 - Native API
11. T1082 - System Information Discovery
12. T1016 - System Network Configuration Discovery
13. T1124 - System Time Discovery
14. T1033 - System Owner/User Discovery
15. T1071.001 - Application Layer Protocol: Web Protocols

## Step 2 - macOS Discovery

16. T1059.004 - Command and Scripting Interpreter: Unix Shell (repeat)
17. T1071.001 - Application Layer Protocol: Web Protocols (repeat)
18. T1083 - File and Directory Discovery
19. T1041 - Exfiltration Over C2 Channel
20. T1552.003 - Unsecured Credentials: Bash History

## Step 3 - Lateral Movement

21. T1105 - Ingress Tool Transfer
22. T1059.004 - Command and Scripting Interpreter: Unix Shell (repeat)
23. T1083 - File and Directory Discovery (repeat)
24. T1071.001 - Application Layer Protocol: Web Protocols (repeat)
25. T1570 - Lateral Tool Transfer
26. T1021.004 - Remote Services: SSH
27. T1547.013 - Boot or Logon Autostart Execution: XDG Autostart Entries
28. T1106 - Native API (repeat)
29. T1559 - Inter-Process Communication

## Step 4 - Discovery on Linux Host

30. T1082 - System Information Discovery (repeat)
31. T1135 - Network Share Discovery

## Step 5 - Collection

32. T1074.001 - Data Staged: Local Data Staging
33. T1083 - File and Directory Discovery (repeat)
34. T1119 - Automated Collection
35. T1560.001 - Archive Collected Data: Archive via Utility

## Step 6 - Exfil from Linux Host

36. T1041 - Exfiltration Over C2 Channel (repeat)
