# Things to consider before starting Atomic Red Team tests
**Resources**: The repository that I am using is my forked repo at https://github.com/sudoheader/art-auto-testing. Check the `ART-win/scripts` folder to learn more about running the scripts. 
1. If you're using scripts, make sure to set the device sleep to "Never" or set to a few hours of your choosing.
2. If not, just make sure Docker is running so that `winlogbeat.exe` can pass the logs stored in Event Viewer to the ELK stack. Once this is done, you can start testing.
3. If you haven't done it already, it is a good idea to install any prerequisites that are necessary to run the atomic tests on the test machine. For example, Microsoft Word and Excel should be installed to run a couple tests successfully. 
4. Make sure to disable Windows Defender and Windows Defender Firewall.
5. Make sure your Active Directory server is running in the background in the other tab (if using VMware).
6. It is a good idea to save a snapshot of your vm instance either in VirtualBox or VMware in case of failure.

## Troubleshooting

If you run into problems with the ELK stack within Docker (nested virtualization) after running the tests, such as the UI in Elasticsearch starts to lags, try restarting the VM or closing a few apps. Sometimes, it looks like Windows just freezes and you get no response (Not responding) so try and see if this fixes it for you. Otherwise, reset it by restoring to a previous snapshot.

For **Sysmon**:
⚠️ALERT⚠️: While troubleshooting why there were no logs in Elasticsearch after running TID `T1562.001` with test number `10` "Unload Sysmon Filter Driver" and TID `T1562.001` with test number `11` "Uninstall Sysmon", **Sysmon** will cease sending logs to **winlogbeat.exe** and as a result, logs will not be collected by the ELK stack. Try to run these separately from the scripts. They have been commented out for a reason.

This will unload **Sysmon** so run the cleanup after executing this command:
```bash
Invoke-AtomicTest T1562.001 -TestNumbers 10
```
This will uninstall **Sysmon** so make sure to save a copy on your file system. The **config.xml** file should not be affected:
```bash
Invoke-AtomicTest T1562.001 -TestNumbers 11
```

### Note: You can skip these next steps if you have no problems running any of these tests
##### For Wizard Spider tests:
Referring back to the repository that I have linked, these are some other notes that I have gathered while observing the scripts run.

While running the `Wizard_Spider_test.ps1` test, I noticed that a few of them were not logging to the ELK stack correctly. The `process.parent.command_line` was showing as the `PowerShell_ISE.exe` executable instead of the typical `Invoke-Atomic $wizard_spider[$c][0] -TestNumbers $wizard_spider[$c][1]`. For example, Atomic Test #7 and #23 for TID `T1112`, and Atomic Test # 11 for TID `T1087.002` were not logging correctly.

You can re-run these test as shown below:
```bash
Invoke-AtomicTest T1112 -TestNumbers 7,23
Invoke-AtomicTest T1087.002 -TestNumbers 11
```

You can also re-run these tests if they are also missing:
```bash
Invoke-AtomicTest T1135 -TestNumbers 3,4,5,6,7,8
Invoke-AtomicTest T1018 -TestNumbers 18
```

##### For Sandworm Team tests:
Tests that have no parent process of the form  `Invoke-Atomic $sandworm_team[$c][0] -TestNumbers $sandworm_team[$c][1]`.
```bash
Invoke-AtomicTest T1204.002 -TestNumbers 1,3
```

⚠️WARNING⚠️: In case `Sandworm_Team_test.ps1` stops all logging, you'll need to perform `Sandworm_Team_test_part2.ps1`, due to the fact that TID `T1562.002` Atomic Test number #2 kills the Event Log service and stops logging to **Sysmon**. You should perform this test separately from the others as shown below or stop running the part 1 test and restart the machine (after it has finished logging this test):
```bash
Invoke-AtomicTest T1562.002 -TestNumbers 2
```

##### Part 2 script:
TID `T1070` Atomic Test number #1 Indicator Removal using FSUtil causes problems with logging for all other tests in the part 1 script, so run this one last, if possible.
```bash
Invoke-AtomicTest T1070 -TestNumbers 1
```

Re-run or recheck these tests that have the same problem as in Wizard Spider tests, where the parent process shows as `PowerShell_ISE.exe`or its variant. Disable the `event.code` filter, if it has already been set, to obtain relevant logs:
```bash
Invoke-AtomicTest T1218.011 -TestNumbers 5
Invoke-AtomicTest T1087.002 -TestNumbers 11
Invoke-AtomicTest T1018 -TestNumbers 18
Invoke-AtomicTest T1082 -TestNumbers 9
Invoke-AtomicTest T1033 -TestNumbers 3
Invoke-AtomicTest T1105 -TestNumbers 7,8,15
```