import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_photo.csv")

# 提取数据
names = df['名称']
change_percent = df['涨跌幅']

# 数据标准化到 [0, 1] 范围用于颜色映射
norm = plt.Normalize(change_percent.min(), change_percent.max())
colors = plt.cm.RdYlGn(norm(change_percent))  # 红-黄-绿渐变色（涨为绿色，跌为红色）

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(names), endpoint=False)

# 极坐标图
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# 每个股票用颜色编码，固定半径
radii = np.full(len(names), 10)  # 固定长度
bars = ax.bar(angles, radii, width=2*np.pi/len(names), color=colors, edgecolor='white')

# 添加标签
for i, (angle, label) in enumerate(zip(angles, names)):
    rotation = np.degrees(angle)
    alignment = 'left' if np.pi/2 <= angle <= 3*np.pi/2 else 'right'
    ax.text(angle, 12, label, rotation=rotation, ha=alignment, va='center', fontsize=9)

# 去掉极轴标签
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_title("股票涨跌幅热力循环图", fontsize=16, pad=20)

plt.tight_layout()
plt.show()


column_mapping = {
    '涨幅%': '涨跌幅',
    '换手率%': '换手率',
    '市盈率(动)': '市盈率',
    '行业名称': '行业'
}
df.rename(columns=column_mapping, inplace=True)

