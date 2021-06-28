import re

from config.setup import *

def time_handler(time, type):
    if type == 0:
        return time
    if type == 1: # time like 02/25/2021 06:32:31.29
        t_year = time[6:10]
        t_slash = time[5]
        t_month_day = time[0:5]
        t_others = time[10:]
        t_new = t_year + t_slash + t_month_day + t_others
        return t_new
    if type == 2: # time like May  9 03:30:01
        timelist = re.split(r'\s+', time)
        t_year = this_year
        month = timelist[0]
        t_month = month_dict[month]
        t_day = timelist[1]
        t_others = timelist[2]
        t_new = t_year + t_month + t_day + " " + t_others
        return t_new


if __name__ == '__main__':
    time1 = 'May  9 03:30:01'
    new = time_handler(time1, type=2)
    print(new)