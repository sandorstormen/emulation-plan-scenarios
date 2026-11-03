# APT29 Scenario 2 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/apt29/Emulation_Plan/Scenario_2/README.md`.

ATT&CK version used for names: v7.0 (the plan links to v6 IDs but also cites sub-technique IDs, which exist only from v7; v7.0 is the earliest version where all cited IDs resolve, with the fewest revoked).


## Step 11 - Initial Breach

81 distinct techniques.

1. T1204 - User Execution
2. T1204.002 - User Execution: Malicious File
3. T1096 - NTFS File Attributes *(revoked in v7.0; replaced by T1564.004 Hide Artifacts: NTFS File Attributes)*
4. T1564.004 - Hide Artifacts: NTFS File Attributes
5. T1564 - Hide Artifacts
6. T1497 - Virtualization/Sandbox Evasion
7. T1497.001 - Virtualization/Sandbox Evasion: System Checks
8. T1082 - System Information Discovery
9. T1120 - Peripheral Device Discovery
10. T1033 - System Owner/User Discovery
11. T1016 - System Network Configuration Discovery
12. T1057 - Process Discovery
13. T1083 - File and Directory Discovery
14. T1060 - Registry Run Keys / Startup Folder *(revoked in v7.0; replaced by T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder)*
15. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
16. T1547 - Boot or Logon Autostart Execution
17. T1140 - Deobfuscate/Decode Files or Information
18. T1086 - PowerShell *(revoked in v7.0; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)*
19. T1059.001 - Command and Scripting Interpreter: PowerShell
20. T1059 - Command and Scripting Interpreter
21. T1043 - Commonly Used Port *(deprecated in v7.0)*
22. T1032 - Standard Cryptographic Protocol *(revoked in v7.0; replaced by T1573 Encrypted Channel)*
23. T1573.002 - Encrypted Channel: Asymmetric Cryptography
24. T1573 - Encrypted Channel
25. T1071 - Application Layer Protocol
26. T1071.001 - Application Layer Protocol: Web Protocols

## Step 12 - Fortify Access

27. T1099 - Timestomp *(revoked in v7.0; replaced by T1070.006 Indicator Removal on Host: Timestomp)*
28. T1070.006 - Indicator Removal on Host: Timestomp
29. T1070 - Indicator Removal on Host
30. T1083 - File and Directory Discovery (repeat)
31. T1063 - Security Software Discovery *(revoked in v7.0; replaced by T1518.001 Software Discovery: Security Software Discovery)*
32. T1518.001 - Software Discovery: Security Software Discovery
33. T1518 - Software Discovery
34. T1012 - Query Registry

## Step 13 - Local Enumeration

35. T1082 - System Information Discovery (repeat)
36. T1016 - System Network Configuration Discovery (repeat)
37. T1033 - System Owner/User Discovery (repeat)
38. T1057 - Process Discovery (repeat)

## Step 14 - Elevation

39. T1122 - Component Object Model Hijacking *(revoked in v7.0; replaced by T1546.015 Event Triggered Execution: Component Object Model Hijacking)*
40. T1546.015 - Event Triggered Execution: Component Object Model Hijacking
41. T1546 - Event Triggered Execution
42. T1088 - Bypass User Account Control *(revoked in v7.0; replaced by T1548.002 Abuse Elevation Control Mechanism: Bypass User Access Control)*
43. T1548.002 - Abuse Elevation Control Mechanism: Bypass User Access Control
44. T1548 - Abuse Elevation Control Mechanism
45. T1047 - Windows Management Instrumentation
46. T1105 - Ingress Tool Transfer
47. T1003 - OS Credential Dumping
48. T1003.001 - OS Credential Dumping: LSASS Memory
49. T1027 - Obfuscated Files or Information
50. T1057 - Process Discovery (repeat)
51. T1140 - Deobfuscate/Decode Files or Information (repeat)

## Step 15 - Establish Persistence

52. T1084 - Windows Management Instrumentation Event Subscription *(revoked in v7.0; replaced by T1546.003 Event Triggered Execution: Windows Management Instrumentation Event Subscription)*
53. T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription
54. T1546 - Event Triggered Execution (repeat)
55. T1033 - System Owner/User Discovery (repeat)

## Step 16 - Lateral Movement

56. T1018 - Remote System Discovery
57. T1033 - System Owner/User Discovery (repeat)
58. T1106 - Native API
59. T1078 - Valid Accounts
60. T1078.002 - Valid Accounts: Domain Accounts
61. T1028 - Windows Remote Management *(revoked in v7.0; replaced by T1021.006 Remote Services: Windows Remote Management)*
62. T1021.006 - Remote Services: Windows Remote Management
63. T1021 - Remote Services
64. T1105 - Ingress Tool Transfer (repeat)
65. T1570 - Lateral Tool Transfer
66. T1003 - OS Credential Dumping (repeat)
67. T1003.001 - OS Credential Dumping: LSASS Memory (repeat)

## Step 17 - Collection

68. T1114 - Email Collection
69. T1114.001 - Email Collection: Local Email Collection
70. T1005 - Data from Local System
71. T1074 - Data Staged
72. T1074.001 - Data Staged: Local Data Staging
73. T1002 - Data Compressed *(revoked in v7.0; replaced by T1560 Archive Collected Data)*
74. T1560.001 - Archive Collected Data: Archive via Utility
75. T1560 - Archive Collected Data
76. T1027 - Obfuscated Files or Information (repeat)

## Step 18 - Exfiltration

77. T1102 - Web Service
78. T1048 - Exfiltration Over Alternative Protocol
79. T1567.002 - Exfiltration Over Web Service: Exfiltration to Cloud Storage

## Step 19 - Clean Up

80. T1107 - File Deletion *(revoked in v7.0; replaced by T1070.004 Indicator Removal on Host: File Deletion)*
81. T1070.004 - Indicator Removal on Host: File Deletion
82. T1070 - Indicator Removal on Host (repeat)
83. T1055 - Process Injection
84. T1055.002 - Process Injection: Portable Executable Injection

## Step 20 - Leverage Persistence

85. T1085 - Rundll32 *(revoked in v7.0; replaced by T1218.011 Signed Binary Proxy Execution: Rundll32)*
86. T1218.011 - Signed Binary Proxy Execution: Rundll32
87. T1218 - Signed Binary Proxy Execution
88. T1084 - Windows Management Instrumentation Event Subscription *(revoked in v7.0; replaced by T1546.003 Event Triggered Execution: Windows Management Instrumentation Event Subscription)* (repeat)
89. T1546.003 - Event Triggered Execution: Windows Management Instrumentation Event Subscription (repeat)
90. T1546 - Event Triggered Execution (repeat)
91. T1086 - PowerShell *(revoked in v7.0; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)* (repeat)
92. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
93. T1059 - Command and Scripting Interpreter (repeat)
94. T1097 - Pass the Ticket *(revoked in v7.0; replaced by T1550.003 Use Alternate Authentication Material: Pass the Ticket)*
95. T1558.001 - Steal or Forge Kerberos Tickets: Golden Ticket
96. T1558 - Steal or Forge Kerberos Tickets
97. T1558.003 - Steal or Forge Kerberos Tickets: Kerberoasting
98. T1028 - Windows Remote Management *(revoked in v7.0; replaced by T1021.006 Remote Services: Windows Remote Management)* (repeat)
99. T1021 - Remote Services (repeat)
100. T1021.006 - Remote Services: Windows Remote Management (repeat)
101. T1136 - Create Account
102. T1136.001 - Create Account: Local Account
103. T1550.001 - Use Alternate Authentication Material: Application Access Token
104. T1550 - Use Alternate Authentication Material
105. T1550.003 - Use Alternate Authentication Material: Pass the Ticket
