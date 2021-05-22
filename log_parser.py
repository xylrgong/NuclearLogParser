import re

with open('一层交换机日志.txt', 'r', encoding='utf-8') as f:
    all_data = f.readlines()
    line_num = len(all_data)
    for i in range(0, line_num):
        raw_data = all_data[i]
        data = raw_data.split()
        match_time = re.search(r"(\d{2}/\d{2}/\d{4})",data[0])
        print(match_time)
