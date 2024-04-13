!os.p
!2024.3.26 [xinhaitianze]
!This module implements some simple window system operations


cbl shutdown = "system('shutdown /s /t cbl['timas']');";
cbl reboot = "system('shutdown /r /t cbl['timas']');";
cbl cpu = "system('wmic cpu get /value');";
cbl blos = "system('wmic bios get /value');";