import re
regex_month = '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
raw_data = 'Apr 25 03:25:01 CCT1 run-parts(/etc/cron.daily)[14731]: finished logrotate'
pattr = '(CROND\[)(\d*)'
flag = re.search(pattr, raw_data)
print(flag)
print(pattr)
