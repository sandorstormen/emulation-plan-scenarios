# Sandworm Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/sandworm/Emulation_Plan/yaml/sandworm.yaml`.

ATT&CK version used for names: v8.0 (`attack_version` in the plan yaml).


## Step 11 - Initial Compromise

22 distinct techniques.

1. T1105 - Ingress Tool Transfer
2. T1505.003 - Server Software Component: Web Shell

## Step 12 - Initial Discovery

3. T1033 - System Owner/User Discovery
4. T1082 - System Information Discovery
5. T1083 - File and Directory Discovery
6. T1003.008 - OS Credential Dumping: /etc/passwd and /etc/shadow

## Step 13 - Upload and Execute Exaramel (Linux Variant)

7. T1105 - Ingress Tool Transfer (repeat)
8. T1548.001 - Abuse Elevation Control Mechanism: Setuid and Setgid

## Step 14 - Exaramel Linux Persistence

9. T1053.003 - Scheduled Task/Job: Cron
10. T1543.002 - Create or Modify System Process: Systemd Service
11. T1003.008 - OS Credential Dumping: /etc/passwd and /etc/shadow (repeat)
12. T1552.003 - Unsecured Credentials: Bash History
13. T1552.004 - Unsecured Credentials: Private Keys

## Step 15 - Move laterally to Windows host

14. T1021.002 - Remote Services: SMB/Windows Admin Shares
15. T1569.002 - System Services: Service Execution
16. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

## Step 16 - Windows Discovery

17. T1033 - System Owner/User Discovery (repeat)
18. T1082 - System Information Discovery (repeat)
19. T1083 - File and Directory Discovery (repeat)
20. T1049 - System Network Connections Discovery

## Step 17 - Credential Dumping

21. T1105 - Ingress Tool Transfer (repeat)
22. T1555.003 - Credentials from Password Stores: Credentials from Web Browsers
23. T1056.001 - Input Capture: Keylogging
24. T1041 - Exfiltration Over C2 Channel
25. T1018 - Remote System Discovery
26. T1070.004 - Indicator Removal on Host: File Deletion
27. T1021.001 - Remote Services: Remote Desktop Protocol

## Step 18 - Pivot to DC

28. T1105 - Ingress Tool Transfer (repeat)
29. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)

## Step 19 - Deploy NotPetya

30. T1486 - Data Encrypted for Impact
31. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)
