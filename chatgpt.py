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

# 设置 ChatGPT API
API_KEY = "sk-PMqQFrJdFfespfZtfkjkOlmW1KpryRTCgbYB8uAnbT6fG5eT"
BASE_URL = "https://api.chatanywhere.tech"

# 创建 OpenAI 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 预设 Prompt 模板
PROMPT_TEMPLATE = """
你是一个 专业的AI助手，负责处理和分析用户上传的 股票 CSV 数据，并根据以下要求生成报告：
分析数据：解析 CSV 文件内容，提取关键因子（基本面、技术面、情绪面）。
生成报告：总结市场趋势，筛选高价值信息，并提供清晰的结论。
表格展示：核心数据需以表格方式呈现
股票推荐：根据分析结果，提供 “值得关注” 和 “需避雷” 的股票清单。
无关声明：明确指出“本报告不构成投资建议，仅供参考”。
散户避雷机模式：针对散户投资者，特别标注高风险个股，避免踩雷。
数据内容如下：
要求精简输出
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
            model="gpt-4o-mini",
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

