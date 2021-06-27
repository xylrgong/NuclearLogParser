from config.pattern import *
# line_num_content_dict = {}
line_num_content_addr = './config/line_content_dict.json'

# log_parsed_name = ['SW1', 'cron', 'messages', 'secure', 'boot', 'maillog', 'dmesg']
log_parsed_name = ['messages']
log_parsed_regex = '(SW1)|^(cron|messages|maillog|secure|dmesg)'

# log_parsed_regex = '(SW1)|^(messages)-(\d)*'

# device_name = [
#     'SW1' , 'CCT', 'DGS-SVR', 'SAR1STR1', 'SAS'
# ]

device_name = ['DGS-SVR']

log_dir = {
    'SW1': 'SWITCH/',
    'CCT': '../LOG/TERMINAL/CCT/log/',
    'DGS-SVR': '../LOG/TERMINAL/DGS-SVR/SYSLOG/',
    'SAR1STR1': '../LOG/TERMINAL/SAR1STR1/log/',
    'SAS': '../LOG/TERMINAL/SAS/SYSLOG/log/'
}

this_year = '2021/'

month_dict = {
    'Jan': '1/',
    'Feb': '2/',
    'Mar': '3/',
    'Apr': '4/',
    'May': '5/',
    'Jun': '6/',
    'Jul': '7/',
    'Aug': '8/',
    'Sep': '9/',
    'Oct': '10/',
    'Nov': '11/',
    'Dec': '12/'
}

dict_pattr = {
    'SW1': SW1,
    'cron': cron,
    'maillog': maillog,
    'secure': secure,
    'messages': messages,
}

time_dict = {
    'SW1': 1,
    'cron': 2,
    'maillog': 2,
    'secure': 2,
    'messages': 2,
    'dmesg': 0,
}

trash_dir = '../../LOG/trash'