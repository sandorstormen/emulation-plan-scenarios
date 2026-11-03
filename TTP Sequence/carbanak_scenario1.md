# Carbanak Scenario 1 - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/carbanak/Emulation_Plan/Scenario_1/README.md`.

ATT&CK version used for names: v8.1 (`attack_version` in the plan yaml).


## Step 1 - Initial Breach

57 distinct techniques.

1. T1204 - User Execution
2. T1204.002 - User Execution: Malicious File
3. T1027 - Obfuscated Files or Information
4. T1059.005 - Command and Scripting Interpreter: Visual Basic
5. T1059 - Command and Scripting Interpreter
6. T1140 - Deobfuscate/Decode Files or Information
7. T1059.007 - Command and Scripting Interpreter: JavaScript/JScript
8. T1563.002 - Remote Service Session Hijacking: RDP Hijacking
9. T1563 - Remote Service Session Hijacking
10. T1071.001 - Application Layer Protocol: Web Protocols
11. T1071 - Application Layer Protocol

## Step 2 - Target Assessment

12. T1033 - System Owner/User Discovery
13. T1082 - System Information Discovery
14. T1057 - Process Discovery
15. T1047 - Windows Management Instrumentation
16. T1105 - Ingress Tool Transfer
17. T1086 - PowerShell *(revoked in v8.1; replaced by T1059.001 Command and Scripting Interpreter: PowerShell)*
18. T1059 - Command and Scripting Interpreter (repeat)
19. T1113 - Screen Capture
20. T1041 - Exfiltration Over C2 Channel

## Step 3 - Deploy Toolkit

21. T1027 - Obfuscated Files or Information (repeat)
22. T1112 - Modify Registry
23. T1105 - Ingress Tool Transfer (repeat)
24. T1059.001 - Command and Scripting Interpreter: PowerShell
25. T1059 - Command and Scripting Interpreter (repeat)
26. T1012 - Query Registry
27. T1140 - Deobfuscate/Decode Files or Information (repeat)
28. T1055 - Process Injection
29. T1571 - Non-Standard Port

## Step 4 - Escalate Privileges

30. T1083 - File and Directory Discovery
31. T1018 - Remote System Discovery
32. T1069 - Permission Groups Discovery
33. T1105 - Ingress Tool Transfer (repeat)
34. T1059.001 - Command and Scripting Interpreter: PowerShell (repeat)
35. T1059 - Command and Scripting Interpreter (repeat)
36. T1549.002 - *(not in ATT&CK v8.1)*
37. T1548 - Abuse Elevation Control Mechanism
38. T1003.001 - OS Credential Dumping: LSASS Memory
39. T1003 - OS Credential Dumping

## Step 5 - Expand Access

40. T1105 - Ingress Tool Transfer (repeat)
41. T1570 - Lateral Tool Transfer
42. T1021.004 - Remote Services: SSH
43. T1021 - Remote Services
44. T1057 - Process Discovery (repeat)
45. T1083 - File and Directory Discovery (repeat)
46. T1018 - Remote System Discovery (repeat)
47. T1550 - Use Alternate Authentication Material
48. T1569.002 - System Services: Service Execution
49. T1569 - System Services
50. T1021.002 - Remote Services: SMB/Windows Admin Shares

## Step 6 - Discover Potential Targets

51. T1018 - Remote System Discovery (repeat)
52. T1087.002 - Account Discovery: Domain Account
53. T1087 - Account Discovery

## Step 7 - Setup Persistence

54. T1105 - Ingress Tool Transfer (repeat)
55. T1572 - Protocol Tunneling
56. T1021.004 - Remote Services: SSH (repeat)
57. T1021 - Remote Services (repeat)
58. T1021.001 - Remote Services: Remote Desktop Protocol
59. T1033 - System Owner/User Discovery (repeat)
60. T1078.002 - Valid Accounts: Domain Accounts
61. T1078 - Valid Accounts
62. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
63. T1547 - Boot or Logon Autostart Execution

## Step 8 - Gain Covert Access to Target

64. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (repeat)
65. T1547 - Boot or Logon Autostart Execution (repeat)
66. T1071 - Application Layer Protocol (repeat)

## Step 9 - Profile a Victim User

67. T1056.001 - Input Capture: Keylogging
68. T1056 - Input Capture
69. T1113 - Screen Capture (repeat)
70. T1555.003 - Credentials from Password Stores: Credentials from Web Browsers
71. T1555 - Credentials from Password Stores
72. T1070.004 - Indicator Removal on Host: File Deletion
73. T1070 - Indicator Removal on Host

## Step 10 - Impersonate Victim

74. T1105 - Ingress Tool Transfer (repeat)
75. T1562.004 - Impair Defenses: Disable or Modify System Firewall
76. T1562 - Impair Defenses
77. T1543.003 - Create or Modify System Process: Windows Service
78. T1543 - Create or Modify System Process
79. T1112 - Modify Registry (repeat)
80. T1078 - Valid Accounts (repeat)
81. T1021.005 - Remote Services: VNC
82. T1021 - Remote Services (repeat)
