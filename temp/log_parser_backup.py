import re
from utils.time_handler import time_handler


def log_passer(addr, pattr, type=1):   # receive an addr(str) and log pattern(list); return key info of log
    with open(addr, 'r', encoding='utf-8') as f:
        with open('../SWITCH/parse_result.txt', 'w', encoding='utf-8') as wf:
            keys = list(pattr.keys())
            values = list(pattr.values())
            match = []
            print('keys:', keys)
            print('values:', values)
            all_data = f.readlines()
            line_num = len(all_data)
            for i in range(0, line_num):
                tmp_dict = {}
                tmp_keys = []
                match_n = []
                raw_data = all_data[i]
                for j in range(0, len(values)):
                    key_keyword = keys[j]
                    regex_keyword = values[j]    # keyword is each regex for our log
                    res = re.search(regex_keyword, raw_data)
                    # print('res.match', res.group(1))    # type of res.group() is str
                    if(key_keyword=='time' and res!=None):
                        time = res.group(2).replace('(','')
                        tmp_dict['time'] = time_handler(time, type)
                    if(key_keyword=='type' and res!=None):
                        tmp_dict['type'] = res.group(2).replace('(','')
                    if(res!=None):
                        tmp_keys.append(keys[j])
                        match.append(res)
                        # print(res.group())
                        match_n.append(res.group(2).replace('(',''))
                res_dic = dict(zip(tmp_keys, match_n))
                print(res_dic)
                # result = []
                # result.append(tmp_dict['time'])
                # result.append('SW1')
                # result.append(tmp_dict['type'])
                # result.append(raw_data.strip('\n'))
                # js = json.dumps(res_dic)
                # result.append(js)
                # title = ['time', 'device', 'type', 'logMessage', 'details']
                # df = pd.DataFrame(columns=title,data=[result])
                # df.to_csv('my_csv.csv', mode='a', header=False)
                # print(js)
                # print(result)
                # wf.writelines(js)
                # wf.writelines('\n')
        return



if __name__ == '__main__':

    filename = '../SWITCH/layer_1_log.txt'
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
    log_passer(filename, pattr)

