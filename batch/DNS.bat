@echo off

set connectionName="ethernet"

netsh interface ip set dns %connectionName% static 10.9.24.148
netsh interface ip add dns name=%connectionName% addr=10.10.25.34 index=2