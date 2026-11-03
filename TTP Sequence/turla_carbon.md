# Turla Carbon (Detections) - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/turla/Emulation_Plan/yaml/turla_carbon.yaml`.

ATT&CK version used for names: v13.1 (`attack_version` in the plan yaml).


## Step 1 - Initial Compromise

18 distinct techniques.

1. T1566.002 - Phishing: Spearphishing Link
2. T1204.002 - User Execution: Malicious File

## Step 3 - Discovery and Privilege Escalation

3. T1069.002 - Permission Groups Discovery: Domain Groups
4. T1059.001 - Command and Scripting Interpreter: PowerShell
5. T1574.011 - Hijack Execution Flow: Services Registry Permissions Weakness

## Step 4 - Persistence

6. T1105 - Ingress Tool Transfer
7. T1112 - Modify Registry
8. T1033 - System Owner/User Discovery

## Step 5 - Lateral Movement to Domain Controller

9. T1110.003 - Brute Force: Password Spraying
10. T1070.004 - Indicator Removal: File Deletion
11. T1570 - Lateral Tool Transfer
12. T1053.005 - Scheduled Task/Job: Scheduled Task
13. T1069.002 - Permission Groups Discovery: Domain Groups (repeat)
14. T1018 - Remote System Discovery

## Step 6 - Preparation for Lateral Movement onto Second Host

15. T1003 - OS Credential Dumping

## Step 7 - Lateral Movement to Second Workstation

16. T1105 - Ingress Tool Transfer (repeat)
17. T1550.002 - Use Alternate Authentication Material: Pass the Hash

## Step 8 - Credential Access on Admin Host

18. T1070.004 - Indicator Removal: File Deletion (repeat)

## Step 9 - Lateral Movement to Linux Server

19. T1105 - Ingress Tool Transfer (repeat)
20. T1021.004 - Remote Services: SSH
21. T1070.004 - Indicator Removal: File Deletion (repeat)

## Step 10 - Installation of Watering Hole

22. T1205 - Traffic Signaling
23. T1189 - Drive-by Compromise
