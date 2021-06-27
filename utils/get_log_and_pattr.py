from config.setup import *
import os
import re

def get_log_pattr_dict(work_dir):
    tmp_dict = {}
    filelist = os.listdir(work_dir)
    pos = 0
    for logfile in filelist:
        size = os.path.getsize(work_dir+logfile)
        syslog_res = re.search(log_parsed_regex, logfile)  # .log[/d]*$
        if  syslog_res and size != 0:
            log_name = filelist[pos]
            for pattr_name in log_parsed_name:
                flag = bool(re.search(pattr_name, log_name))
                if flag:
                    tmp_dict[log_name] = pattr_name
                    break
        pos += 1
    # print('logfile name of ' + work_dir + ' is:', tmp_list)
    return tmp_dict

if __name__ == '__main__':
    for device in device_name:
        work_dir = log_dir[device]
        log_dict = get_log_pattr_dict(work_dir)
        print(log_dict)