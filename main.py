import requests
import re
import pandas as pd
import time

# 写入cookie信息
cookies = {
    'qgqp_b_id': '02d480cce140d4a420a0df6b307a945c',
    'cowCookie': 'true',
    'em_hq_fls': 'js',
    'intellpositionL': '1168.61px',
    'HAList': 'a-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-000001-%u5E73%u5B89%u94F6%u884C',
    'st_si': '07441051579204',
    'st_asi': 'delete',
    'st_pvi': '34234318767565',
    'st_sp': '2021-09-28%2010%3A43%3A13',
    'st_inirUrl': 'http%3A%2F%2Fdata.eastmoney.com%2F',
    'st_sn': '31',
    'st_psi': '20211020210419860-113300300813-5631892871',
    'intellpositionT': '1007.88px',
}

# 配置头文件
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
    'DNT': '1',
    'Accept': '*/*',
    'Referer': 'http://quote.eastmoney.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# 保存所有信息的列表
all_message = []

# 遍历页数
for page in range(1, 5):
    print(f"正在抓取第 {page} 页数据...")
    params = {
        'cb': 'jQuery1124031167968836399784_1615878909521',
        'pn': str(page),
        'pz': '20',
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'fid': 'f3',
        'fs': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
    }

    response = requests.get(
        'http://67.push2.eastmoney.com/api/qt/clist/get',
        headers=headers, params=params, cookies=cookies, verify=False
    )

    if response.status_code != 200:
        print(f"第 {page} 页请求失败，状态码：{response.status_code}")
        continue

    text = response.text

    # 使用正则提取数据
    daimas = re.findall('"f12":(.*?),', text)
    names = re.findall('"f14":"(.*?)"', text)
    zuixinjias = re.findall('"f2":(.*?),', text)
    zhangdiefus = re.findall('"f3":(.*?),', text)
    zhangdiees = re.findall('"f4":(.*?),', text)
    chengjiaoliangs = re.findall('"f5":(.*?),', text)
    chengjiaoes = re.findall('"f6":(.*?),', text)
    zhenfus = re.findall('"f7":(.*?),', text)
    zuigaos = re.findall('"f15":(.*?),', text)
    zuidis = re.findall('"f16":(.*?),', text)
    jinkais = re.findall('"f17":(.*?),', text)
    zuoshous = re.findall('"f18":(.*?),', text)
    liangbis = re.findall('"f10":(.*?),', text)
    huanshoulvs = re.findall('"f8":(.*?),', text)
    shiyinglvs = re.findall('"f9":(.*?),', text)
    shijinglvs = re.findall('"f23":(.*?),', text)

    # 保存为字典
    for i in range(len(daimas)):
        stock_dict = {
            "代码": daimas[i],
            "名称": names[i],
            "最新价": zuixinjias[i],
            "涨跌幅": zhangdiefus[i],
            "涨跌额": zhangdiees[i],
            "成交量": chengjiaoliangs[i],
            "成交额": chengjiaoes[i],
            "振幅": zhenfus[i],
            "最高": zuigaos[i],
            "最低": zuidis[i],
            "今开": jinkais[i],
            "昨收": zuoshous[i],
            "量比": liangbis[i],
            "换手率": huanshoulvs[i],
            "市盈率(动态)": shiyinglvs[i],
            "市净率": shijinglvs[i]
        }
        all_message.append(stock_dict)

    # 限速防封
    time.sleep(1)

# 转为DataFrame并保存
df = pd.DataFrame(all_message)
save_path = "C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_data.csv"
df.to_csv(save_path, index=False, encoding='utf-8-sig')

print(f"\n✅ 数据抓取完毕，共 {len(df)} 条记录，已保存至：{save_path}")
