import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_data.csv")

# 提取名称与涨跌幅
names = df['名称']
change_percent = df['涨跌幅']
n = len(names)

# 智能调整图形大小
base_size = 6
figsize = (base_size + n * 0.2, base_size + n * 0.2)

# 设置三角坐标（每360°中取120°）
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
angles = (angles % (2 * np.pi / 3)) * 3  # 三角分布效果

# 创建图形
plt.figure(figsize=figsize)
ax = plt.subplot(111, polar=True)

# 柱状图（玫瑰花瓣）
bars = ax.bar(angles, change_percent, width=2 * np.pi / n * 0.8,
               color=['red' if x >= 0 else 'green' for x in change_percent])

# 标签位置调整
label_radius = max(change_percent.max(), abs(change_percent.min())) * 1.1
for angle, label, value in zip(angles, names, change_percent):
    ha = 'left' if 0 <= angle <= np.pi else 'right'
    ax.text(angle, label_radius, f"{label}\n{value:.2f}%",
            ha=ha, va='center', fontsize=9, rotation=np.degrees(angle), rotation_mode='anchor')

# 样式设置
ax.set_title("股票三角玫瑰图（三角极坐标）", fontsize=16)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
