import re
import json




def log_passer(addr, pattr):   # receive an addr(str) and log pattern(list); return key info of log
    with open(addr, 'r', encoding='utf-8') as f:
        keys = list(pattr.keys())
        values = list(pattr.values())
        match = []
        print(keys)
        print(values)
        all_data = f.readlines()
        line_num = len(all_data)
        for i in range(0, line_num):
            match_n = []
            for j in range(0, len(values)):
                res = re.search(values[j], all_data[i])
                if(res!=None):
                    match.append(res.group(2).replace(':','').replace('\n',''))
                    match_n.append(res.group(2).replace(':','').replace('\n',''))
            dic = dict(zip(keys, match_n))
            js = json.dumps(dic)
            print(js)
        print(match)
    return


def passer_handler():   # do the find job
    return


def get_regex(path):
    with open(path, 'r', encoding='utf-8') as pattr_file:
        pattr_json = pattr_file.read()
        regex_pattr = json.loads(pattr_json)
    return regex_pattr

if __name__ == '__main__':
    filename = '../TERMINAL/SAR1STR1/syslog/messages-20210523'
    pattr = get_regex('../conf/message.json')
    log_passer(filename, pattr)
