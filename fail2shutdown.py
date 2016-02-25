#!/usr/bin/python3
#
# This script turns the computer off after multiple failed attempts to
# login. Useful if you want to thwart an attacker who currently has access
# to attempt logins but is unaware of the FDE password required on reboot

from time import strftime,strptime,localtime
from datetime import datetime,timedelta
from socket import gethostname
from os import system

MAX_ATTEMPTS = 4    # maximum number of allowed logins per duration
DURATION     = 600  # in seconds

host     = gethostname()
auth_log = '/var/log/auth.log'
bad_auth = 'Authentication failure for '
today    = strftime('%b %e',localtime())
now      = datetime.today()
fails    = []

# To prevent a rebooting loop, exit if the computer was rebooted in the
# last DURATION + 1 minutes
with open('/proc/uptime','r') as f:
	uptime_seconds = float(f.readlines()[0].split()[0])

if uptime_seconds < (DURATION + 60):
	raise SystemExit(1)

# otherwise, open log
with open(auth_log, 'r') as f:
	log = f.readlines()

# create a list of all failed auths today
for line in log:
	if today in line and bad_auth in line:
		fails.append(line)

# but stop if there aren't any failed auths today
if len(fails) == 0:
	raise SystemExit(2)

# now create a list of all failed auths in the last 10 minutes
shutdown = 0
for line in fails:
	dt = datetime.strptime(line.split(host)[0], '%b %d %H:%M:%S ')  #v3
	dt = dt.replace(year=now.year)

	if dt > now - timedelta(seconds=DURATION):
		shutdown = shutdown + 1

# shutdown if greater than MAX_ATTEMPTS value. Need to run this as root.
if shutdown > MAX_ATTEMPTS:
	system('/sbin/shutdown -h now')
