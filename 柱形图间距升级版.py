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
num_stocks = len(names)

# 根据数据数量动态设置图表宽度（每条股票给0.5~0.8英寸宽度）
fig_width = max(12, num_stocks * 0.6)

# 创建图形
plt.figure(figsize=(fig_width, 6))
bars = plt.bar(names, change_percent, color=['red' if x >= 0 else 'green' for x in change_percent])

# 设置Y轴范围
plt.ylim(-25, 50)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    label_y = height + 1 if height >= 0 else height - 3  # 正数放上面，负数放下面
    plt.text(bar.get_x() + bar.get_width() / 2, label_y, f'{height:.2f}%',
             ha='center', va='bottom' if height >= 0 else 'top', fontsize=8)

# 设置标题和标签
plt.xlabel("股票名称")
plt.ylabel("涨跌幅（%）")
plt.title("股票涨跌幅柱状图（范围：-25% 到 +50%）")

# 自动旋转标签防止重叠
rotation_angle = 45 if num_stocks <= 20 else 60
plt.xticks(rotation=rotation_angle, ha='right')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
