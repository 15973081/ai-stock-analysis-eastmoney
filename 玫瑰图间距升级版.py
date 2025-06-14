import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv("C:\\Users\\MaYunnan\\PycharmProjects\\dongfangmoney\\东方财富_data.csv")

# 提取数据
names = df['名称']
change_percent = df['涨跌幅']
num_stocks = len(names)

# 动态调整玫瑰图图形尺寸
fig_size = max(8, min(40, num_stocks * 0.4))  # 最小8，最大40
plt.figure(figsize=(fig_size, fig_size))

# 极坐标角度
angles = np.linspace(0, 2 * np.pi, num_stocks, endpoint=False)

# 创建极坐标图
ax = plt.subplot(111, projection='polar')

# 设置每个柱子的宽度：总角度除以数量再乘缩放因子（避免重叠）
bar_width = (2 * np.pi / num_stocks) * 0.8

# 创建玫瑰图
bars = ax.bar(angles, change_percent, width=bar_width,
              color=['red' if x >= 0 else 'green' for x in change_percent])

# 标签：自动调整文字角度和位置
for i, bar in enumerate(bars):
    height = bar.get_height()
    label_angle = angles[i]
    label_y = height + 1 if height >= 0 else height - 3
    rotation = np.degrees(label_angle)

    # 文字角度与居中方式自适应
    alignment = 'left' if np.pi / 2 < label_angle < 3 * np.pi / 2 else 'right'
    rotation = (rotation + 180) % 360 if alignment == 'left' else rotation

    ax.text(label_angle, label_y, f'{height:.2f}%',
            ha='center', va='bottom' if height >= 0 else 'top',
            fontsize=8, rotation=rotation, rotation_mode='anchor')

# 设置股票名称在图外圆周排列
ax.set_xticks(angles)
ax.set_xticklabels(names, fontsize=10)

# 自动旋转角度防止名称堆叠
for label, angle in zip(ax.get_xticklabels(), angles):
    angle_deg = np.degrees(angle)
    label.set_rotation(angle_deg)
    label.set_rotation_mode('anchor')
    if np.pi / 2 < angle < 3 * np.pi / 2:
        label.set_horizontalalignment('right')
    else:
        label.set_horizontalalignment('left')

# 其它样式
ax.set_title("股票涨跌幅玫瑰图", fontsize=16, pad=20)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
