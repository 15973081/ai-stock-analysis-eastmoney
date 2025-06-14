import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体，防止乱码
plt.rcParams['font.family'] = 'SimHei'  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_data.csv")

# 提取数据
names = df['名称']
change_percent = df['涨跌幅']

# 创建图形
plt.figure(figsize=(12, 6))
bars = plt.bar(names, change_percent, color=['red' if x >= 0 else 'green' for x in change_percent])

# 设置Y轴范围
plt.ylim(-25, 50)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    label_y = height + 1 if height >= 0 else height - 3  # 正数放上面，负数放下面
    plt.text(bar.get_x() + bar.get_width() / 2, label_y, f'{height:.2f}%', ha='center', va='bottom' if height >= 0 else 'top', fontsize=8)

# 设置标题和标签
plt.xlabel("股票名称")
plt.ylabel("涨跌幅（%）")
plt.title("股票涨跌幅柱状图（范围：-25% 到 +50%）")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
