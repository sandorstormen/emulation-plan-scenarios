# Wizard Spider Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/wizard_spider/Emulation_Plan/yaml/wizard_spider.yaml`.

ATT&CK version used for names: v8.0 (`attack_version` in the plan yaml).


## Step 1 - Initial Compromise

24 distinct techniques.

1. T1105 - Ingress Tool Transfer
2. T1078 - Valid Accounts
3. T1204.002 - User Execution: Malicious File

## Step 2 - Emotet Persistence

4. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

## Step 3 - Emotet Host Discovery and Credential Collection

5. T1082 - System Information Discovery
6. T1057 - Process Discovery
7. T1105 - Ingress Tool Transfer (repeat)
8. T1552 - Unsecured Credentials
9. T1114.001 - Email Collection: Local Email Collection
10. T1021.001 - Remote Services: Remote Desktop Protocol

## Step 4 - Move Laterally Deploy TrickBot

11. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)
12. T1105 - Ingress Tool Transfer (repeat)

## Step 5 - TrickBot Discovery

13. T1082 - System Information Discovery (repeat)
14. T1007 - System Service Discovery
15. T1087.001 - Account Discovery: Local Account
16. T1087.002 - Account Discovery: Domain Account
17. T1016 - System Network Configuration Discovery
18. T1049 - System Network Connections Discovery
19. T1482 - Domain Trust Discovery
20. T1069 - Permission Groups Discovery

## Step 6 - Kerberoast the DC

21. T1558.003 - Steal or Forge Kerberos Tickets: Kerberoasting
22. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)

## Step 7 - Lateral Movement to DC

23. T1105 - Ingress Tool Transfer (repeat)
24. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)
25. T1547.004 - Boot or Logon Autostart Execution: Winlogon Helper DLL
26. T1069.002 - Permission Groups Discovery: Domain Groups

## Step 8 - Dump Active Directory Database (ntds.dit)

27. T1003.003 - OS Credential Dumping: NTDS
28. T1003.002 - OS Credential Dumping: Security Account Manager

## Step 9 - Ryuk Inhibit System Recovery

29. T1105 - Ingress Tool Transfer (repeat)
30. T1489 - Service Stop
31. T1490 - Inhibit System Recovery

## Step 10 - Ryuk Encryption for Impact

32. T1105 - Ingress Tool Transfer (repeat)
33. T1486 - Data Encrypted for Impact
34. T1021.001 - Remote Services: Remote Desktop Protocol (repeat)
