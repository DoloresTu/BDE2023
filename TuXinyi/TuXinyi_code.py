import pandas as pd
import glob

# 替换成你的特定路径
path = 'FilterFullText/*.csv'  
files = glob.glob(path)

total_count = 0  # 用于累加所有满足条件的微博数量

for file in files:
    # 读取CSV文件
    df = pd.read_csv(file)
    
    # 筛选转发数、评论数、点赞数不全为0的微博
    filtered_df = df[(df['转发数'] != 0) | (df['评论数'] != 0) | (df['点赞数'] != 0)]
    
    # 计算当前文件中满足条件的微博数量
    count = len(filtered_df)
    print(f"{file}: {count}个满足条件的微博")
    
    # 更新总数量
    total_count += count

print(f"所有CSV文件中共有{total_count}个满足条件的微博")
