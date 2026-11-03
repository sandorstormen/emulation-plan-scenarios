# menuPass Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/menu_pass/Emulation_Plan/Scenario1.md`.

ATT&CK version used for names: v8.1 (`attack_version` in the plan yaml).


## Step 1 - menuPass Initial Access

30 distinct techniques.

1. T1199 - Trusted Relationship
2. T1078.002 - Valid Accounts: Domain Accounts
3. T1078 - Valid Accounts

## Step 2 - menuPass Command and Control

4. T1105 - Ingress Tool Transfer

## Step 3 - menuPass Discovery

5. T1049 - System Network Connections Discovery
6. T1018 - Remote System Discovery
7. T1046 - Network Service Scanning
8. T1016 - System Network Configuration Discovery

## Step 4 - menuPass Credential Access

9. T1003.001 - OS Credential Dumping: LSASS Memory
10. T1003 - OS Credential Dumping
11. T1003.002 - OS Credential Dumping: Security Account Manager
12. T1003.004 - OS Credential Dumping: LSA Secrets

## Step 5 - menuPass Lateral Movement

13. T1569.002 - System Services: Service Execution
14. T1569 - System Services
15. T1021.001 - Remote Services: Remote Desktop Protocol
16. T1021 - Remote Services
17. T1021.002 - Remote Services: SMB/Windows Admin Shares
18. T1570 - Lateral Tool Transfer
19. T1053.005 - Scheduled Task/Job: Scheduled Task
20. T1053 - Scheduled Task/Job

## Step 6 - menuPass Collection

21. T1560.001 - Archive Collected Data: Archive via Utility
22. T1560 - Archive Collected Data
23. T1074.001 - Data Staged: Local Data Staging
24. T1074 - Data Staged

## Step 7 - menuPass Exfiltration

25. T1537 - Transfer Data to Cloud Account

## Step 8 - menuPass Execution (Optional)

26. T1047 - Windows Management Instrumentation
27. T1053.005 - Scheduled Task/Job: Scheduled Task (repeat)
28. T1053 - Scheduled Task/Job (repeat)

## Step 9 - menuPass Persistence (Optional)

29. T1053.005 - Scheduled Task/Job: Scheduled Task (repeat)
30. T1053 - Scheduled Task/Job (repeat)
31. T1543.003 - Create or Modify System Process: Windows Service
32. T1543 - Create or Modify System Process
33. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
34. T1547 - Boot or Logon Autostart Execution
