import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体，防止乱码
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_data.csv")

# 提取数据
names = df['名称']
change_percent = df['涨跌幅']

# 计算角度值
angles = np.linspace(0, 2 * np.pi, len(names), endpoint=False)

# 创建极坐标图
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection='polar')

# 创建玫瑰图（柱状图）
bars = ax.bar(angles, change_percent, width=0.3, color=['red' if x >= 0 else 'green' for x in change_percent])

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    label_angle = bar.get_x() + bar.get_width() / 2
    label_y = height + 1 if height >= 0 else height - 3  # 正数放上面，负数放下面
    ax.text(label_angle, label_y, f'{height:.2f}%', ha='center', va='bottom' if height >= 0 else 'top', fontsize=8)

# 设置图形标题
ax.set_title("股票涨跌幅玫瑰图", fontsize=16)

# 显示股票名称
ax.set_xticks(angles)
ax.set_xticklabels(names, rotation=45, ha='right', fontsize=10)

# 显示网格线
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
