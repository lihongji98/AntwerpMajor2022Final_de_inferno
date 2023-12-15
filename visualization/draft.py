import json

import numpy as np

# 指定你的 JSON 文件路径
json_file_path = 'D:\pycharm_projects\CSGO_Analytics\Maps\mapMetaData\infernoMask.json'

# 打开并读取 JSON 文件
with open(json_file_path, 'r') as json_file:
    # 使用 json.load() 方法加载 JSON 数据
    data = json.load(json_file)

data = np.array(data)
# 现在，变量 data 包含了从 JSON 文件中读取的数据
print(data.shape)
