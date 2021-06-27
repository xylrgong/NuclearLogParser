import re
import json
import pymysql



'''
with open('一层交换机日志.txt', 'r', encoding='utf-8') as f:
    all_data = f.readlines()
    line_num = len(all_data)
    for i in range(0, line_num):
        match_time = re.search(r"(\d{2}/\d{2}/\d{4})",all_data[i])
        match_info = re.search(r"(\d{2}:\d{2}:\d{2}\.\d{2})", all_data[i])
        print(match_time)
        print(match_info)
        
pattr = {'time': '()(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}.\d{2})', \
                  # 'time2': '()(\d{2}:\d{2}:\d{2}.\d{2})', \
                  'type': '(<)((\S)*)(>)', \
                  'Media': '(Media )((\d)*T)', \
                  'action' : '()((remove)|(insert)|(Toggling AdminState)|(link UP)|(link down)|(shutdown)|(re-enable))',\
                  'port' : '(Port )([(]?(\d)*)[)]?',\
                  # 'power_state' : '(portLinkState[\S\s]*)((down)|(up))' , \
                  'login/out_state' : '()(passed|failed|message repeated 2 additional times|logout)', \
                  'pif' : '(pif )(0x[\dabcdef]*)', \
                  'speed' : '(speed )(\d Gbps)', \
                  'mode' : '()(full-duplex)', \
                  }
'''


def getPattr():
    pass



def log_passer(addr, pattr):   # receive an addr(str) and log pattern(list); return key info of log
    with open(addr, 'r', encoding='utf-8') as f:
        with open('parse_result.txt', 'w', encoding='utf-8') as wf:
            keys = list(pattr.keys())
            values = list(pattr.values())
            match = []
            print('keys:', keys)
            print('values:', values)
            all_data = f.readlines()
            line_num = len(all_data)
            for i in range(0, line_num):
                tmp_keys = []
                match_n = []
                for j in range(0, len(values)):
                    res = re.search(values[j], all_data[i])
                    # print('res.match', res.group(1))    # type of res.group() is str
                    if(res!=None):
                        tmp_keys.append(keys[j])
                        match.append(res)
                        # print(res.group())
                        match_n.append(res.group(2).replace('(',''))
                dic = dict(zip(tmp_keys, match_n))
                js = json.dumps(dic)
                print(js)
                wf.writelines(js)
                wf.writelines('\n')
            print(match)
        return



if __name__ == '__main__':

    filename = '../SWITCH/layer_1_log.txt'
    pattr = {'time': '()(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}.\d{2})', \
                  # 'time2': '()(\d{2}:\d{2}:\d{2}.\d{2})', \
                  'type': '(<)((\S)*)(>)', \
                  'Media': '(Media )((\d)*T)', \
                  'action' : '()((remove)|(insert)|(Toggling AdminState)|(link UP)|(link down)|(shutdown)|(re-enable))',\
                  'port' : '(Port )([(]?(\d)*)[)]?',\
                  # 'power_state' : '(portLinkState[\S\s]*)((down)|(up))' , \
                  'login/out_state' : '()(passed|failed|message repeated 2 additional times|logout)', \
                  'pif' : '(pif )(0x[\dabcdef]*)', \
                  'speed' : '(speed )(\d Gbps)', \
                  'mode' : '()(full-duplex)', \
                  }
    log_passer(filename, pattr)
