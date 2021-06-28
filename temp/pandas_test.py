import pandas as pd
title = ['time', 'device', 'type', 'logMessage', 'details']
res = ["02/25/2021 06:35:55.01", "sw1", "Info:vlan.dbg.info", "02/25/2021 06:35:55.01 <Info:vlan.dbg.info> Media 1000T is inserted into Port 25", '{"time": "02/25/2021 06:35:55.01", "type": "Info:vlan.dbg.info", "Media": "1000T", "action": "insert", "port": "25"}']
result = [res]
#result = ["02/25/2021 06:35:55.01", "sw1", "Info:vlan.dbg.info", "02/25/2021 06:35:55.01 <Info:vlan.dbg.info> Media 1000T is inserted into Port 25", '{"time": "02/25/2021 06:35:55.01", "type": "Info:vlan.dbg.info", "Media": "1000T", "action": "insert", "port": "25"}']
df = pd.DataFrame(columns=title,data=result)
df.to_csv('my_csv.csv', header=False)