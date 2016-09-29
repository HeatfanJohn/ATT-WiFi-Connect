# ATT-WiFi-Connect
Python script to automatically connect to AT&amp;T WiFi - automatically accepts AT&amp;T T's and C's

Requires:
* Curl
* Python Mechanize

Add the following line to CRON using `crontab -e`:
*/5 * * * * /home/chip/ATT-WiFi-Connect/test-internet 2>&1 | /usr/bin/logger -t ATT_WiWi_Check

This will run the check script every 5 minutes logging the result to syslog
