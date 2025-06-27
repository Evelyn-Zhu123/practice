import pandas as pd
import requests
import math
#进度条
from tqdm import tqdm

#创建一个变量储存信息
All_data = []
#网址，其中{} 会被 .format() 替换成页码，size=20 意味着每页20条记录。
url = 'https://gs.amac.org.cn/amac-infodisc/api/pof/manager/query?&page={}&size=20'
#筛选条件
filter_data = {'fundScale': "scope03",'fundType': "smzqzzfx",'primaryInvestType': "smzqtzjjglr"}
#爬第一页,POST JSON:json是一个字典类型
res = requests.post(url = url.format(0),json = filter_data)
total_elements = res.json().get('totalElements')
total_page = math.ceil(total_elements/20)
for page in tqdm(range(0,total_page)):
    res1 = requests.post(url = url.format(page),json = filter_data)
    data = res1.json().get('content')
    All_data.extend(data)
#pd.DataFrame(All_data)：把列表中的每个字典自动转成一行，把所有字段都变成 DataFrame 的列。
df = pd.DataFrame(All_data)
print(df)

df.to_excel("company.xlsx", index=False)
#index=False：不把 DataFrame 的行号也写进去。 

