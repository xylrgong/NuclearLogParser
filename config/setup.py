from config.pattern import *
# line_num_content_dict = {}
line_num_content_addr = '/home/host/log_parse/config/line_content_dict.json'

log_parsed_name = ['SW1', 'cron', 'messages', 'secure', 'maillog', 'dmesg']
# log_parsed_name = ['messages']
log_parsed_regex = '(SW1)|^(cron|messages|cron|secure|dmesg)'

# log_parsed_regex = '(SW1)|^(messages)-(\d)*'

# device_name = [
#     'SW1' , 'CCT', 'DGS-SVR', 'SAR1STR1', 'SAS'
# ]

device_name = ['DGS-SVR', 'CCT1', 'SAS1', 'SAR1STR1', 'SW1']

log_dir = {
    'SW1': '/var/log/switch_log/SW1/',
    'CCT1': '/var/log/terminal_log/CCT1/sys/',
    'DGS-SVR': '/var/log/terminal_log/DGS-SVR/sys/',
    'SAR1STR1': '/var/log/terminal_log/SAR1STR1/sys/',
    'SAS1': '/var/log/terminal_log/SAS1/sys/'
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
    'dmesg': dmesg,
}

time_dict = {
    'SW1': 1,
    'cron': 2,
    'maillog': 2,
    'secure': 2,
    'messages': 2,
    'dmesg': 0,
}

# trash_dir = '../../LOG/trash'
