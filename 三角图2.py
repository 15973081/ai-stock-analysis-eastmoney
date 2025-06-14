import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_photo.csv")

# 提取名称与涨跌幅
names = df['名称'].values
values = df['涨跌幅'].values

# 至少3个点才能形成三角图
if len(values) < 3:
    raise ValueError("三角图需要至少3个数据点")

# 智能调整图像大小
n = len(names)
figsize = (6 + n * 0.2, 6 + n * 0.2)

# 创建图形
fig, ax = plt.subplots(figsize=figsize)

# 定义三角形顶点
triangle_points = np.array([
    [0.5, np.sqrt(3)/2],  # 顶部
    [0, 0],               # 左下
    [1, 0]                # 右下
])

# 归一化涨跌幅数据
norm_values = (values - np.min(values)) / (np.max(values) - np.min(values))

# 将归一化值映射到三角形中点
points = []
for i, v in enumerate(norm_values):
    a = triangle_points[0] * (1 - v) + triangle_points[1] * (v / 2) + triangle_points[2] * (v / 2)
    points.append(a)
points = np.array(points)

# 绘制三角形
triangle = plt.Polygon(triangle_points, fill=None, edgecolor='black', linewidth=2)
ax.add_patch(triangle)

# 绘制数据点
ax.scatter(points[:, 0], points[:, 1], c=['red' if val >= 0 else 'green' for val in values], s=80)

# 添加股票名称和涨跌幅标签
for i, (x, y) in enumerate(points):
    ax.text(x, y, f"{names[i]}\n{values[i]:.2f}%", ha='center', va='center', fontsize=8)

# 去除坐标轴
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1)
ax.axis('off')

plt.title("股票涨跌幅三角图", fontsize=16)
plt.tight_layout()
plt.show()
