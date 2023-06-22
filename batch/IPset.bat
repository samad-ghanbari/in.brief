@echo off
SET /P d= Do you want to use DHCP?
IF "%d%"=="y" (goto DHCP)
IF "%d%"=="YES" (goto DHCP)
IF "%d%"=="Y" (goto DHCP)
IF "%d%"=="yes" (goto DHCP)
goto SETIP

:DHCP
netsh interface ip set address Ethernet dhcp
netsh interface ip set dns Ethernet dhcp
goto DONE

:SETIP
set connectionName="Ethernet"
set staticIP=172.18.14.31
set subnetMask=255.255.255.0
set defaultGateway=172.18.14.1

:: Change Nothing Below This Line ::
netsh interface ip set address %connectionName% static %staticIP% %subnetMask% %defaultGateway% 1
netsh interface ip set dns %connectionName% static 10.9.24.148
netsh interface ip add dns name=%connectionName% addr=10.10.25.34 index=2

:DONE