#!/usr/bin/python3

from subprocess import call, getoutput
from re import findall


def bash(cmd):
	call(cmd, shell=True)


port = 5555
devices = getoutput('adb devices')[25:]

if 'device' in devices:
	ip = getoutput('adb shell ifconfig')
	ip = findall(r'addr:(\S+)', ip)

	if len(ip) > 0 and ':' not in devices:
		ip = ip[0]
		bash(f'adb tcpip {port}')
		bash(f'adb connect {ip}:{port}')
	else:
		bash('adb disconnect')
else:
	exit('Not exists devices!!!')
