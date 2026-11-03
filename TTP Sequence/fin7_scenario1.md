# FIN7 Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/fin7/Emulation_Plan/Scenario_1/README.md`.

ATT&CK version used for names: v8.1 (`attack_version` in the plan yaml).


## Step 1 - Initial Breach (Evaluations Step 11)

52 distinct techniques.

1. T1204 - User Execution
2. T1027 - Obfuscated Files or Information
3. T1170 - Mshta *(revoked in v8.1; replaced by T1218.005 Signed Binary Proxy Execution: Mshta)*
4. T1218 - Signed Binary Proxy Execution
5. T1059 - Command and Scripting Interpreter
6. T1036 - Masquerading
7. T1175 - Component Object Model and Distributed COM *(deprecated in v8.1)*
8. T1053 - Scheduled Task/Job
9. T1204.002 - User Execution: Malicious File

## Step 2 - Delayed Malware Execution (Evaluations Step 12)

10. T1053.005 - Scheduled Task/Job: Scheduled Task
11. T1053 - Scheduled Task/Job (repeat)
12. T1059 - Command and Scripting Interpreter (repeat)
13. T1071 - Application Layer Protocol
14. T1016 - System Network Configuration Discovery
15. T1082 - System Information Discovery

## Step 3 - Target Assessment (Evaluations Step 13)

16. T1057 - Process Discovery
17. T1135 - Network Share Discovery
18. T1497 - Virtualization/Sandbox Evasion
19. T1033 - System Owner/User Discovery
20. T1082 - System Information Discovery (repeat)
21. T1016 - System Network Configuration Discovery (repeat)
22. T1059 - Command and Scripting Interpreter (repeat)
23. T1086 - PowerShell *(revoked in v8.1; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)*
24. T1113 - Screen Capture
25. T1041 - Exfiltration Over C2 Channel
26. T1105 - Ingress Tool Transfer
27. T1059.003 - Command and Scripting Interpreter: Windows Command Shell
28. T1059.001 - Command and Scripting Interpreter: PowerShell

## Step 4 - Staging Interactive Toolkit (Evaluations Step 14)

29. T1059 - Command and Scripting Interpreter (repeat)
30. T1086 - PowerShell *(revoked in v8.1; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)* (repeat)
31. T1140 - Deobfuscate/Decode Files or Information
32. T1071 - Application Layer Protocol (repeat)
33. T1032 - Standard Cryptographic Protocol *(revoked in v8.1; replaced by T1573 Encrypted Channel)*

## Step 5 - Escalate Privileges (Evaluations Step 15)

34. T1057 - Process Discovery (repeat)
35. T1507 - *(not in ATT&CK v8.1)*
36. T1086 - PowerShell *(revoked in v8.1; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)* (repeat)
37. T1088 - Bypass User Account Control *(revoked in v8.1; replaced by T1548.002 Abuse Elevation Control Mechanism: Bypass User Account Control)*
38. T1003.001 - OS Credential Dumping: LSASS Memory
39. T1003 - OS Credential Dumping
40. T1016 - System Network Configuration Discovery (repeat)
41. T1018 - Remote System Discovery
42. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
43. T1059 - Command and Scripting Interpreter (repeat)
44. T1140 - Deobfuscate/Decode Files or Information (repeat)
45. T1071.001 - Application Layer Protocol: Web Protocols
46. T1071 - Application Layer Protocol (repeat)
47. T1573.002 - Encrypted Channel: Asymmetric Cryptography
48. T1573 - Encrypted Channel

## Step 6 - Expand Access (Evaluations Step 16)

49. T1105 - Ingress Tool Transfer (repeat)
50. T1059.003 - Command and Scripting Interpreter: Windows Command Shell (repeat)
51. T1059 - Command and Scripting Interpreter (repeat)
52. T1021.002 - Remote Services: SMB/Windows Admin Shares
53. T1021 - Remote Services
54. T1035 - Service Execution *(revoked in v8.1; replaced by T1569.002 System Services: Service Execution)*
55. T1569 - System Services
56. T1055.012 - Process Injection: Process Hollowing
57. T1055 - Process Injection
58. T1071.001 - Application Layer Protocol: Web Protocols (repeat)
59. T1071 - Application Layer Protocol (repeat)
60. T1573.002 - Encrypted Channel: Asymmetric Cryptography (repeat)
61. T1573 - Encrypted Channel (repeat)
62. T1078.002 - Valid Accounts: Domain Accounts
63. T1078 - Valid Accounts
64. T1569.002 - System Services: Service Execution

## Step 7 - Setup User Monitoring (Evaluations Step 17)

65. T1105 - Ingress Tool Transfer (repeat)
66. T1036.005 - Masquerading: Match Legitimate Name or Location
67. T1036 - Masquerading (repeat)
68. T1059.003 - Command and Scripting Interpreter: Windows Command Shell (repeat)
69. T1059 - Command and Scripting Interpreter (repeat)
70. T1574 - Hijack Execution Flow
71. T1071 - Application Layer Protocol (repeat)
72. T1573 - Encrypted Channel (repeat)
73. T1574.001 - Hijack Execution Flow: DLL Search Order Hijacking
74. T1071.001 - Application Layer Protocol: Web Protocols (repeat)
75. T1573.002 - Encrypted Channel: Asymmetric Cryptography (repeat)

## Step 8 - User Monitoring (Evaluations Step 18)

76. T1055 - Process Injection (repeat)
77. T1113 - Screen Capture (repeat)
78. T1056.001 - Input Capture: Keylogging
79. T1056 - Input Capture

## Step 9 - Setup Shim Persistence (Evaluations Step 19)

80. T1021 - Remote Services (repeat)
81. T1090 - Proxy
82. T1059 - Command and Scripting Interpreter (repeat)
83. T1027 - Obfuscated Files or Information (repeat)
84. T1105 - Ingress Tool Transfer (repeat)
85. T1546.011 - Event Triggered Execution: Application Shimming
86. T1546 - Event Triggered Execution
87. T1078.003 - Valid Accounts: Local Accounts
88. T1078 - Valid Accounts (repeat)
89. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)

## Step 10 - Steal Payment Data (Evaluations Step 20)

90. T1546.011 - Event Triggered Execution: Application Shimming (repeat)
91. T1546 - Event Triggered Execution (repeat)
92. T1071 - Application Layer Protocol (repeat)
93. T1071.001 - Application Layer Protocol: Web Protocols (repeat)
94. T1573 - Encrypted Channel (repeat)
95. T1105 - Ingress Tool Transfer (repeat)
96. T1057 - Process Discovery (repeat)
97. T1138 - Application Shimming *(revoked in v8.1; replaced by T1546.011 Event Triggered Execution: Application Shimming)*
98. T1055 - Process Injection (repeat)
