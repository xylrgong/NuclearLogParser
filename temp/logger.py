import re
import json
import os
import pandas as pd

def find_log_suffix(filepath):
    # TODO: ADD IF STATEMENT not to include empty log file
    with open(filepath, 'r', encoding='utf-8') as f:
        subdir_list = f.read().splitlines()
        print('subdir_list:', subdir_list)
        for dir in subdir_list:
            loglist_from_dir = os.listdir(dir)
            tmp_list = []
            pos = 0
            fw = open(dir+'_loglist.txt', 'a', encoding='utf-8')
            fr = open(dir+'_loglist.txt', 'r', encoding='utf-8')
            size = os.path.getsize(dir+'_loglist.txt')
            if size != 0:
                loglist_from_fr = fr.read().splitlines()
                print('loglist_from_fr:', loglist_from_fr)

            for log_from_dir in loglist_from_dir:
                # TODO: add right logic to include syslog items: maillog, spooler, secure, cron
                syslog_res = re.search('(maillog|spooler|secure|message)', log_from_dir)  # .log[/d]*$
                # if logfile_name:
                if ('.log' in log_from_dir) or syslog_res:
                    #size = os.path.getsize(dir + '/' + list)
                    # if size != 0:
                    log_entry = loglist_from_dir[pos]
                    tmp_list.append(log_entry)
                    if size == 0:
                        fw.writelines(log_entry)
                        fw.writelines(' 0 0')
                        fw.writelines('\n')
                pos += 1
            loglist_from_dir = tmp_list
            print('logfile name of ' + dir + ' is:', loglist_from_dir)
            fw.close()
            fr.close()
    f.close()


def find_sub_dir(filepath):
    # for root, dirs, files in os.walk(self.filepath):
    # self.subdir = os.walk(self.filepath)
    # print(self.subdir)
    log_subdir = []
    with open('sub_dir.txt', 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(filepath):
            for file in files:
                if '.log' in file:
                    log_subdir.append(root)
                    f.writelines(root)
                    f.writelines('\n')
                    # print('FILES:', files)
                    break
    f.close()
    print('log_subdir is: ', log_subdir)

if __name__ == '__main__':
    filepath = '../../LOG/TERMINAL/CCT/APPLOG'
    find_sub_dir(filepath)
    find_log_suffix('sub_dir.txt')

