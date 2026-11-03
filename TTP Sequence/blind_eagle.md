# Blind Eagle - TTP Sequence

Techniques in order of first appearance per step, extracted from: `emulation_plans/blind_eagle/Emulation_Plan/Blind_Eagle_Scenario.md`.

ATT&CK version used for names: v13.1 (not stated in the plan; assumed, see README).


## Step 1 - Initial Compromise and Persistence

15 distinct techniques.

1. T1024.002 - User Execution: Malicious File *(plan typo for T1204.002)*
2. T1036.007 - Masquerading: Double File Extension
3. T1059 - Command and Scripting Interpreter
4. T1105 - Ingress Tool Transfer
5. T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
6. T1132.001 - Data Encoding: Standard Encoding
7. T1140 - Deobfuscate/Decode Files or Information
8. T1150 - Plist Modification *(revoked in v13.1; replaced by T1547.011 Boot or Logon Autostart Execution: Plist Modification)*
9. T1102 - Web Service
10. T1055.012 - Process Injection: Process Hollowing
11. T1218.009 - System Binary Proxy Execution: Regsvcs/Regasm

## Step 2 - Credential Theft

12. T1555.003 - Credentials from Password Stores: Credentials from Web Browsers
13. T1539 - Steal Web Session Cookie
14. T1555.004 - Credentials from Password Stores: Windows Credential Manager

## Step 3 - Keylogging

15. T1056 - Input Capture
