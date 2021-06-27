import pandas as pd
import re

filename = '../../LOG/TERMINAL/CCT/APPLOG/cct1exe_loglist.csv'
log = pd.read_csv(filename, engine='python', names=['logname', 'line_num', 'line_done'])
print(log['logname'][2])
print(log)