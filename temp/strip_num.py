import re
str1 = 'maillog-20210523'
str2 = 'secure-20210509'
pattr = 'maillog|spooler|secure|message'
res = re.search(pattr,str2)
print(res)
print(bool(res))