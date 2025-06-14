from openai import OpenAI
import pandas as pd
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    filename='b.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

# 设置 DeepSeek API
API_KEY = "sk-aedc680dd9514aaaba75580f6dd96f50"
BASE_URL = "https://api.deepseek.com"

# 创建 OpenAI 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 预设 Prompt 模板
PROMPT_TEMPLATE = """
你是一个专业的AI助手，根据以下要求处理数据：
1. 分析用户上传的CSV文件内容
2. 提取关键信息并生成总结报告
3. 以表格形式展示核心数据
4. 输出结果需包含时间戳和数据来源
5. 推荐我选择哪些股票，来帮助用户合理选择，给出分析理由和原因，并发表无关声明
6. 请作为一名合格的韭菜避雷机，用户是散户。
7. 当个股涨幅异常、成交量剧烈波动时，在提示中加入“高风险”标签；
数据内容如下：
{data}
"""

def read_csv(file_path):
    """读取 CSV 文件并返回 DataFrame"""
    try:
        df = pd.read_csv(file_path)
        logging.info(f"成功读取文件: {file_path}")
        return df
    except Exception as e:
        logging.error(f"读取文件失败: {str(e)}")
        return None

def format_response(data):
    """格式化 API 响应数据"""
    formatted_text = f"""
数据分析报告 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
--------------------------------------------------
数据来源: 东方财富_data.csv

{data}
"""
    return formatted_text

def main():
    # 读取 CSV 数据
    df = read_csv('东方财富_data.csv')

    if df is not None:
        # 发送 API 请求
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个数据分析助手"},
                {"role": "user", "content": PROMPT_TEMPLATE.format(data=df.to_string())},
            ],
            stream=False
        )

        # 解析 API 响应
        if response.choices:
            formatted_output = format_response(response.choices[0].message.content)
        else:
            formatted_output = "API 返回格式异常，未能解析数据。"

        # 输出到控制台
        print(formatted_output)

        # 记录到日志文件
        logging.info("API 调用成功")
        logging.info(formatted_output)
    else:
        logging.warning("未成功读取数据文件")
        print("未成功读取数据文件")

if __name__ == "__main__":
    main()
