from qqwry import QQwry
import pandas as pd
import os

# 设置工作目录
os.chdir('G:/python/0-ip')

# 数据读取
df = pd.read_excel('1.xlsx', sheet_name = 0)
df_length = len(df)

# 读取'IP'列数据放入列表
ip_data = df.IP.tolist()

city_data = []
isp_data = []
q = QQwry()
q.load_file('G:/python/0-ip/qqwry_find_ip_belong/qqwry.dat')
for i in ip_data:

    result = q.lookup(i)
    print(result)
    city_data.append(result[0])

# 将数据整合为Dataframe类型
ipinfo = {"IP": ip_data, "城市": city_data}
result = pd.DataFrame(ipinfo)
# # Dataframe输出为excel
result.to_excel('5.xlsx')