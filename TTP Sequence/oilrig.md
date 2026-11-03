# OilRig - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/oilrig/Emulation_Plan/yaml/oilrig.yaml`.

ATT&CK version used for names: v11.3 (`attack_version` in the plan yaml).


## Step 1 - Initial Compromise

24 distinct techniques.

1. T1082 - System Information Discovery
2. T1033 - System Owner/User Discovery

## Step 2 - Workstation Discovery

3. T1033 - System Owner/User Discovery (repeat)
4. T1082 - System Information Discovery (repeat)
5. T1016 - System Network Configuration Discovery
6. T1087.002 - Account Discovery: Domain Account
7. T1069.002 - Permission Groups Discovery: Domain Groups
8. T1021 - Remote Services
9. T1087.001 - Account Discovery: Local Account
10. T1069.001 - Permission Groups Discovery: Local Groups
11. T1049 - System Network Connections Discovery
12. T1057 - Process Discovery
13. T1007 - System Service Discovery
14. T1012 - Query Registry
15. T1018 - Remote System Discovery

## Step 3 - Workstation Low Privilege Credential Dumping test

16. T1555.004 - Credentials from Password Stores: Windows Credential Manager
17. T1041 - Exfiltration Over C2 Channel

## Step 4 - Install Web Shell on EWS

18. T1105 - Ingress Tool Transfer
19. T1505.003 - Server Software Component: Web Shell
20. T1082 - System Information Discovery (repeat)

## Step 5 - EWS Discovery

21. T1033 - System Owner/User Discovery (repeat)
22. T1016 - System Network Configuration Discovery (repeat)
23. T1049 - System Network Connections Discovery (repeat)

## Step 6 - Privileged Credential Dumping

24. T1105 - Ingress Tool Transfer (repeat)
25. T1003.001 - OS Credential Dumping: LSASS Memory
26. T1041 - Exfiltration Over C2 Channel (repeat)
27. T1070.004 - Indicator Removal on Host: File Deletion

## Step 7 - Lateral Movement to EWS via RDP Tunnel

28. T1105 - Ingress Tool Transfer (repeat)
29. T1572 - Protocol Tunneling
30. T1021.001 - Remote Services: Remote Desktop Protocol
31. T1569.002 - System Services: Service Execution
32. T1083 - File and Directory Discovery
33. T1048.003 - Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol
34. T1070.004 - Indicator Removal on Host: File Deletion (repeat)
