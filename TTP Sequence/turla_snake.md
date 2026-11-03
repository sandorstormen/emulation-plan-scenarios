# Turla Snake (Detections) - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/turla/Emulation_Plan/yaml/turla_snake.yaml`.

ATT&CK version used for names: v13.1 (`attack_version` in the plan yaml).


## Step 11 - Initial Compromise and Establish Foothold

21 distinct techniques.

1. T1189 - Drive-by Compromise
2. T1204.002 - User Execution: Malicious File
3. T1082 - System Information Discovery

## Step 12 - Rootkit Installation

4. T1105 - Ingress Tool Transfer
5. T1014 - Rootkit

## Step 13 - First Workstation Discovery

6. T1057 - Process Discovery
7. T1087.002 - Account Discovery: Domain Account
8. T1049 - System Network Connections Discovery

## Step 14 - Lateral Movement to File Server

9. T1105 - Ingress Tool Transfer (repeat)
10. T1569.002 - System Services: Service Execution
11. T1070.004 - Indicator Removal: File Deletion

## Step 15 - Domain Discovery

12. T1059.001 - Command and Scripting Interpreter: PowerShell
13. T1069.001 - Permission Groups Discovery: Local Groups
14. T1087.002 - Account Discovery: Domain Account (repeat)
15. T1018 - Remote System Discovery

## Step 16 - Preparation for Lateral Movement to Admin Workstation

16. T1105 - Ingress Tool Transfer (repeat)
17. T1003.001 - OS Credential Dumping: LSASS Memory

## Step 17 - Lateral Movement to Admin Workstation and Persistence

18. T1550.002 - Use Alternate Authentication Material: Pass the Hash
19. T1070.004 - Indicator Removal: File Deletion (repeat)
20. T1057 - Process Discovery (repeat)
21. T1136.002 - Create Account: Domain Account

## Step 18 - Lateral Movement to Exchange Server

22. T1105 - Ingress Tool Transfer (repeat)
23. T1570 - Lateral Tool Transfer
24. T1505.002 - Server Software Component: Transport Agent
25. T1059.003 - Command and Scripting Interpreter: Windows Command Shell
26. T1070.004 - Indicator Removal: File Deletion (repeat)

## Step 19 - Discovery and Email Collection

27. T1016 - System Network Configuration Discovery
28. T1041 - Exfiltration Over C2 Channel
