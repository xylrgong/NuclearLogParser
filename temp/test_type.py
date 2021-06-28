import re
str = 'Info:vlan.dbg.info'
res = re.search('info', str, re.IGNORECASE)
print(bool(res))