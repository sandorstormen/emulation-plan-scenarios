# APT29 Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/apt29/Emulation_Plan/Scenario_1/README.md`.

ATT&CK version used for names: v7.0 (the plan links to v6 IDs but also cites sub-technique IDs, which exist only from v7; v7.0 is the earliest version where all cited IDs resolve, with the fewest revoked).


## Step 1 - Initial Breach

80 distinct techniques.

1. T1204 - User Execution
2. T1204.002 - User Execution: Malicious File
3. T1036 - Masquerading
4. T1036.002 - Masquerading: Right-to-Left Override
5. T1065 - Uncommonly Used Port *(revoked in v7.0; replaced by T1571 Non-Standard Port)*
6. T1059 - Command and Scripting Interpreter
7. T1059.003 - Command and Scripting Interpreter: Windows Command Shell
8. T1086 - PowerShell *(revoked in v7.0; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)*
9. T1059.001 - Command and Scripting Interpreter: PowerShell

## Step 2 - Rapid Collection and Exfiltration

10. T1083 - File and Directory Discovery
11. T1119 - Automated Collection
12. T1005 - Data from Local System
13. T1002 - Data Compressed *(revoked in v7.0; replaced by T1560 Archive Collected Data)*
14. T1560.001 - Archive Collected Data: Archive via Utility
15. T1560 - Archive Collected Data
16. T1041 - Exfiltration Over C2 Channel

## Step 3 - Deploy Stealth Toolkit

17. T1105 - Ingress Tool Transfer
18. T1027 - Obfuscated Files or Information
19. T1027.003 - Obfuscated Files or Information: Steganography
20. T1122 - Component Object Model Hijacking *(revoked in v7.0; replaced by T1546.015 Event Triggered Execution: Component Object Model Hijacking)*
21. T1546.015 - Event Triggered Execution: Component Object Model Hijacking
22. T1546 - Event Triggered Execution
23. T1088 - Bypass User Account Control *(revoked in v7.0; replaced by T1548.002 Abuse Elevation Control Mechanism: Bypass User Access Control)*
24. T1548.002 - Abuse Elevation Control Mechanism: Bypass User Access Control
25. T1548 - Abuse Elevation Control Mechanism
26. T1043 - Commonly Used Port *(deprecated in v7.0)*
27. T1071 - Application Layer Protocol
28. T1071.001 - Application Layer Protocol: Web Protocols
29. T1032 - Standard Cryptographic Protocol *(revoked in v7.0; replaced by T1573 Encrypted Channel)*
30. T1573 - Encrypted Channel
31. T1112 - Modify Registry

## Step 4 - Defense Evasion and Discovery

32. T1105 - Ingress Tool Transfer (repeat)
33. T1086 - PowerShell *(revoked in v7.0; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)* (repeat)
34. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
35. T1059 - Command and Scripting Interpreter (repeat)
36. T1140 - Deobfuscate/Decode Files or Information
37. T1057 - Process Discovery
38. T1107 - File Deletion *(revoked in v7.0; replaced by T1070.004 Indicator Removal on Host: File Deletion)*
39. T1070.004 - Indicator Removal on Host: File Deletion
40. T1070 - Indicator Removal on Host
41. T1016 - System Network Configuration Discovery
42. T1033 - System Owner/User Discovery
43. T1063 - Security Software Discovery *(revoked in v7.0; replaced by T1518.001 Software Discovery: Security Software Discovery)*
44. T1518.001 - Software Discovery: Security Software Discovery
45. T1518 - Software Discovery
46. T1069 - Permission Groups Discovery
47. T1082 - System Information Discovery
48. T1083 - File and Directory Discovery (repeat)
49. T1106 - Native API

## Step 5 - Persistence

50. T1031 - Modify Existing Service *(revoked in v7.0; replaced by T1543.003 Create or Modify System Process: Windows Service)*
51. T1543.003 - Create or Modify System Process: Windows Service
52. T1543 - Create or Modify System Process
53. T1060 - Registry Run Keys / Startup Folder *(revoked in v7.0; replaced by T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder)*
54. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
55. T1547 - Boot or Logon Autostart Execution

## Step 6 - Credential Access

56. T1081 - Credentials in Files *(revoked in v7.0; replaced by T1552.001 Unsecured Credentials: Credentials In Files)*
57. T1552.001 - Unsecured Credentials: Credentials In Files
58. T1552 - Unsecured Credentials
59. T1003 - OS Credential Dumping
60. T1555.003 - Credentials from Password Stores: Credentials from Web Browsers
61. T1555 - Credentials from Password Stores
62. T1036 - Masquerading (repeat)
63. T1036.005 - Masquerading: Match Legitimate Name or Location
64. T1145 - Private Keys *(revoked in v7.0; replaced by T1552.004 Unsecured Credentials: Private Keys)*
65. T1552.004 - Unsecured Credentials: Private Keys
66. T1003.002 - OS Credential Dumping: Security Account Manager

## Step 7 - Collection and Exfiltration

67. T1113 - Screen Capture
68. T1115 - Clipboard Data
69. T1056 - Input Capture
70. T1056.001 - Input Capture: Keylogging
71. T1005 - Data from Local System (repeat)
72. T1560 - Archive Collected Data (repeat)
73. T1560.001 - Archive Collected Data: Archive via Utility (repeat)
74. T1048 - Exfiltration Over Alternative Protocol
75. T1002 - Data Compressed *(revoked in v7.0; replaced by T1560 Archive Collected Data)* (repeat)
76. T1022 - Data Encrypted *(revoked in v7.0; replaced by T1560 Archive Collected Data)*

## Step 8 - Lateral Movement

77. T1018 - Remote System Discovery
78. T1021 - Remote Services
79. T1021.006 - Remote Services: Windows Remote Management
80. T1057 - Process Discovery (repeat)
81. T1105 - Ingress Tool Transfer (repeat)
82. T1027 - Obfuscated Files or Information (repeat)
83. T1027.002 - Obfuscated Files or Information: Software Packing
84. T1021.002 - Remote Services: SMB/Windows Admin Shares
85. T1035 - Service Execution *(revoked in v7.0; replaced by T1569.002 System Services: Service Execution)*
86. T1569.002 - System Services: Service Execution
87. T1569 - System Services
88. T1078 - Valid Accounts
89. T1078.002 - Valid Accounts: Domain Accounts

## Step 9 - Collection

90. T1105 - Ingress Tool Transfer (repeat)
91. T1059 - Command and Scripting Interpreter (repeat)
92. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
93. T1083 - File and Directory Discovery (repeat)
94. T1119 - Automated Collection (repeat)
95. T1005 - Data from Local System (repeat)
96. T1002 - Data Compressed *(revoked in v7.0; replaced by T1560 Archive Collected Data)* (repeat)
97. T1022 - Data Encrypted *(revoked in v7.0; replaced by T1560 Archive Collected Data)* (repeat)
98. T1560.001 - Archive Collected Data: Archive via Utility (repeat)
99. T1560 - Archive Collected Data (repeat)
100. T1074 - Data Staged
101. T1074.001 - Data Staged: Local Data Staging
102. T1041 - Exfiltration Over C2 Channel (repeat)
103. T1107 - File Deletion *(revoked in v7.0; replaced by T1070.004 Indicator Removal on Host: File Deletion)* (repeat)
104. T1070.004 - Indicator Removal on Host: File Deletion (repeat)
105. T1070 - Indicator Removal on Host (repeat)

## Step 10 - Persistence Execution

106. T1035 - Service Execution *(revoked in v7.0; replaced by T1569.002 System Services: Service Execution)* (repeat)
107. T1569.002 - System Services: Service Execution (repeat)
108. T1569 - System Services (repeat)
109. T1060 - Registry Run Keys / Startup Folder *(revoked in v7.0; replaced by T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder)* (repeat)
110. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (repeat)
111. T1547 - Boot or Logon Autostart Execution (repeat)
112. T1106 - Native API (repeat)
113. T1134 - Access Token Manipulation
114. T1134.002 - Access Token Manipulation: Create Process with Token
