import os

from config.setup import *
import json

# @atexit.register
def exit_save(line_num_content_dict):
 with open(line_num_content_addr, 'w') as f:
     json_str = json.dumps(line_num_content_dict, indent=4)
     f.write(json_str)
 print('Bye')


def read_line_num_content_from_json(addr=line_num_content_addr):
    if os.path.getsize(addr) == 0:
        return {}
    with open(addr, 'r') as f:
        raw = f.read()
        line_num_content_dict = json.loads(raw)
        print(line_num_content_dict)
    return line_num_content_dict





if __name__ == '__main__':
    line_num_content_dict = {}
    addr = 'SWITCH/'
    filename = 'SW1.txt'
    line_num_content_dict['SW1'] = [322, '02/25/2021 02:46:16.34 <Info:vlan.dbg.info> Toggling AdminState on Port 25 with pif 0x5df7f0\n']
    # linenum = file_line_num_content_comparison(addr, filename)
    # print(line_num_content_dict[filename])
    # print(linenum)
    # print('*****************')
    # read_line_num_content_from_json(addr+filename)
    # exit_save(line_num_content_dict)
    json_str = json.dumps(line_num_content_dict, indent=4)
    # print(json_str)
