import re
import json
import os


left_file = 'leftbehind.txt'

class BaseLog:
    def __init__(self, pattr, filepath, pos=2):
        '''
        :param pattr: the parse pattern of log
        :param filepath: the directory where log locate
        :param pos: the position of bracket of regular expression, default is 2
        '''
        self.pos = pos
        self.pattr = pattr
        self.filepath = filepath
        self.keys = list(self.pattr.keys())
        self.values = list(self.pattr.values())

    def print2terminal(self):
        print('self.subdir:', self.subdir)

    def find_log_suffix(self):
    # TODO: ADD IF STATEMENT not to include empty log file
        for dir in self.log_subdir:
            filelist = os.listdir(dir)
            # print('filelist in class:', filelist)
            tmp_list = []
            pos = 0
            for list in filelist:
                # TODO: add right logic to include syslog items: maillog, spooler, secure, cron
                logfile_name = re.findall('maillog', list)  # .log[/d]*$
                # if logfile_name:
                if '.log' in list or logfile_name:
                    size = os.path.getsize(dir + '/' + list)
                    if size != 0:
                        tmp_list.append(filelist[pos])
                pos += 1
            self.filelist = tmp_list
            print('logfile name is:', self.filelist)

    def find_sub_dir(self):
        # for root, dirs, files in os.walk(self.filepath):
        # self.subdir = os.walk(self.filepath)
        # print(self.subdir)
        log_subdir = []
        for root, dirs, files in os.walk(self.filepath):
            for file in files:
                if '.log' in file:
                    log_subdir.append(root)
                    # print('FILES:', files)
                    break
        self.log_subdir = log_subdir
        print('log_subdir is: ', self.log_subdir)


    def get_pattr(self):
        pass

    def log_parse_handler(self):
        pass



if __name__ == '__main__':
    filepath = '../../LOG/TERMINAL/CCT/'
    pattr = {'time': '()(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}.\d{2})', \
             # 'time2': '()(\d{2}:\d{2}:\d{2}.\d{2})', \
             'type': '(<)((\S)*)(>)', \
             'Media': '(Media )((\d)*T)', \
             'action' : '()((remove)|(insert)|(Toggling AdminState)|(link UP)|(link down)|(shutdown)|(re-enable))', \
             'port' : '(Port )([(]?(\d)*)[)]?', \
             # 'power_state' : '(portLinkState[\S\s]*)((down)|(up))' , \
             'login/out_state' : '()(passed|failed|message repeated 2 additional times|logout)', \
             'pif' : '(pif )(0x[\dabcdef]*)', \
             'speed' : '(speed )(\d Gbps)', \
             'mode' : '()(full-duplex)', \
             }
    f = '../LOG/TERMINAL/CCT/APPLOG\cct1exe'

    log_obj = BaseLog(pattr=pattr, filepath=filepath, pos=2)
    log_obj.find_sub_dir()
    log_obj.find_log_suffix()
    #log_obj.print2terminal()

'''
def find_log_suffix(filepath):
    filelist = os.listdir(filepath)
    # print('filelist in class:', filelist)
    tmp_list = []
    for list in filelist:
        logfile_name = re.findall('\S*.log', list)
        if logfile_name:
            tmp_list.append(logfile_name)
    filelist = tmp_list
    print(filelist)

find_log_suffix(f)
'''