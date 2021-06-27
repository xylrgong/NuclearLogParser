import json
from utils.time_handler import time_handler
from utils.get_log_and_pattr import get_log_pattr_dict
from db.db import *
from config.setup import *
from utils.move_file import *
from utils.line_num_select import exit_save, read_line_num_content_from_json
from datetime import datetime
global flag
flag = False

def log_passer(addr, pattr, devicename, timetype, startline=0):   # receive an addr(str) and log pattern(list); return key info of log
    with open(addr, 'r', encoding='utf-8') as f:
    # with open('SWITCH/parse_result.txt', 'w', encoding='utf-8') as wf:
        keys = list(pattr.keys())
        values = list(pattr.values())
        match = []
        # print('keys:', keys)
        # print('values:', values)
        all_data = f.readlines()[startline:]
        line_num = len(all_data)
        for i in range(0, line_num):
            tmp_dict = {}
            tmp_keys = []
            match_n = []
            raw_data = all_data[i].strip('\n')
            for j in range(0, len(values)):
                key_keyword = keys[j]
                regex_keyword = values[j]    # keyword is each regex for our log
                res = re.search(regex_keyword, raw_data)
                # print('res.match', res.group(1))    # type of res.group() is str
                if(key_keyword=='time'):
                    if res!=None:
                        time = res.group(2).replace('(','')
                        tmp_dict['time'] = time_handler(time, timetype)
                    else:
                        # TODO: 日志写入时time没法为空
                        tmp_dict['time'] = str(datetime.now())
                        # tmp_dict['time'] = 'None'
                if(key_keyword=='type'):
                    #print('################')
                    if res != None:
                        tmp_dict['type'] = res.group(2).replace('(','')
                        if bool(re.search('debug', tmp_dict['type'], re.IGNORECASE)):
                            tmp_dict['type'] = 'Debug'
                        elif bool(re.search('warn', tmp_dict['type'], re.IGNORECASE)):
                            tmp_dict['type'] = 'Warning'
                        elif bool(re.search('error', tmp_dict['type'], re.IGNORECASE)):
                            tmp_dict['type'] = 'Error'
                    else:
                        global flag
                        flag = True
                        tmp_dict['type'] = 'Info'
                if(res!=None):
                    tmp_keys.append(keys[j])
                    match.append(res)
                    # print(res.group())
                    match_n.append(res.group(2).replace('(',''))
                if flag:
                    tmp_keys.append(keys[j])
                    match_n.append(tmp_dict['type'])
                    flag = False
            res_dic = dict(zip(tmp_keys, match_n))
            result = []
            result.append(tmp_dict['time'])
            result.append(devicename)
            result.append(tmp_dict['type'])
            result.append(raw_data.strip('\n'))
            js = json.dumps(res_dic)
            result.append(js)
            insert_log(result)
            print(result)
        return


def parse_a_sentence(raw_data, devicename, keys, values, timetype):
    tmp_keys = []
    match_n = []
    tmp_dict = {}
    for j in range(0, len(values)):
        key_keyword = keys[j]
        regex_keyword = values[j]    # keyword is each regex for our log
        res = re.search(regex_keyword, raw_data)
        # print('res.match', res.group(1))    # type of res.group() is str
        if(key_keyword=='time'):
            if res!=None:
                time = res.group(2).replace('(','')
                tmp_dict['time'] = time_handler(time, timetype)
            else:
                # TODO: 日志写入时time没法为空
                tmp_dict['time'] = str(datetime.now())
                # tmp_dict['time'] = 'None'
        if(key_keyword=='type'):
            #print('################')
            if res != None:
                tmp_dict['type'] = res.group(2).replace('(','')
                if bool(re.search('debug', tmp_dict['type'], re.IGNORECASE)):
                    tmp_dict['type'] = 'Debug'
                elif bool(re.search('warn', tmp_dict['type'], re.IGNORECASE)):
                    tmp_dict['type'] = 'Warning'
                elif bool(re.search('error', tmp_dict['type'], re.IGNORECASE)):
                    tmp_dict['type'] = 'Error'
            else:
                global flag
                flag = True
                tmp_dict['type'] = 'Info'
        if(res!=None):
            tmp_keys.append(keys[j])
            # print(res.group())
            match_n.append(res.group(2).replace('(',''))
        if flag:
            tmp_keys.append(keys[j])
            match_n.append(tmp_dict['type'])
            flag = False
    res_dic = dict(zip(tmp_keys, match_n))
    result = []
    result.append(tmp_dict['time'])
    result.append(devicename)
    result.append(tmp_dict['type'])
    result.append(raw_data.strip('\n'))
    js = json.dumps(res_dic)
    result.append(js)
    return result


def file_line_num_content_comparison(addr, filename, device, line_num_content_dict):
    with open(addr + filename, 'r', encoding='utf-8') as f:
        key = filename + '_' + device
        raw_data = f.readlines()
        linenum = len(raw_data)
        content_last_line = raw_data[linenum-1]
        new_list = []
        new_list.append(linenum)
        new_list.append(content_last_line)
        if key not in line_num_content_dict.keys():
            print('In branch 1: new file:{} at {}'.format(filename, device))
            line_num_content_dict[key] = new_list
            return 0

        elif line_num_content_dict[key] == new_list:
            print('In branch 2: old file:{} at {}'.format(filename, device))
            return -1
        elif line_num_content_dict[key] != new_list:
            print('In branch 3: file changed')
            old_line_num = line_num_content_dict[key][0]
            if old_line_num < linenum:
                print('In branch 3-1: file added:{} at {}'.format(filename, device))
                line_num_content_dict[key] = new_list
                return old_line_num
            elif old_line_num > linenum:
                print('In branch 3-2: new file < old file')
                line_num_content_dict[key] = new_list
                return 0
            else:
                print('In branch 3-3: What a magic! New file is the same size as old one!')
                line_num_content_dict[key] = new_list
                return 0


def start_parse(line_num_content_dict):
    for device in device_name:
        work_dir = log_dir[device]
        log_dict_n = get_log_pattr_dict(work_dir)
        for filename in log_dict_n.keys():
            pattr_name = log_dict_n[filename]
            pattr = dict_pattr[pattr_name]
            timetype = time_dict[pattr_name]
            addr = work_dir + filename
            startline = file_line_num_content_comparison(addr=work_dir,
                                                         filename=filename,
                                                         device= device,
                                                         line_num_content_dict=line_num_content_dict)
            if startline != -1:
                log_passer(addr, pattr, devicename=device,timetype=timetype,startline=startline)
                # move_file(work_dir, trash_dir, filename)
    return


if __name__ == '__main__':
    line_num_content_dict = read_line_num_content_from_json()
    #start = datetime.now().replace( minute=3, second=0, microsecond=0 )
    #print(start)
    #tmr = MyTimer( start, 60*60*3, start_parse() )
    #tmr.start()
    start_parse(line_num_content_dict)
    exit_save(line_num_content_dict)