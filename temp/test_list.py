import os
import re
f = '../LOG/TERMINAL/CCT/APPLOG\cct1exe'


def find_log_suffix(filepath):
    filelist = os.listdir(filepath)
    # print('filelist in class:', filelist)
    tmp_list = []
    pos = 0
    for list in filelist:
        logfile_name = re.findall('.log', list)
        if logfile_name:
            tmp_list.append(filelist[pos])
        pos += 1
    filelist = tmp_list
    print(filelist)

find_log_suffix(f)