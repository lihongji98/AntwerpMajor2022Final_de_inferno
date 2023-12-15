import json

import numpy as np

file_path = r"D:\pycharm_projects\CSGO_Analytics\visualization\data\frame_data.json"

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

json_file_path = r'D:\pycharm_projects\CSGO_Analytics\Maps\mapMetaData\infernoMask.json'

with open(json_file_path, 'r') as json_file:
    # 使用 json.load() 方法加载 JSON 数据
    map_mask = json.load(json_file)

map_mask = np.array(map_mask)
map_mask = np.where(map_mask == 255, 1, 0)

# round 1-15 34-35
# Faze -> T Navi -> CT
# round 16-30 31-33
# Faze -> CT Navi -> T
faze_T, faze_CT = [], []
navi_T, navi_CT = [], []

for roundNum in data.keys():
    for second in data[roundNum].keys():
        Navi_frame_data = data[roundNum][second][0]['Natus Vincere']
        Faze_frame_data = data[roundNum][second][1]['FaZe Clan']
        if 1 <= int(roundNum) + 1 <= 15 or 34 <= int(roundNum) + 1 <= 35:
            faze_T.append(Faze_frame_data)
            navi_CT.append(Navi_frame_data)
        elif 16 <= int(roundNum) + 1 <= 30 or 31 <= int(roundNum) + 1 <= 33:
            faze_CT.append(Faze_frame_data)
            navi_T.append(Navi_frame_data)

map_scale_parameter = {"pos_x": -2087.0, "pos_y": 3870.0, "scale": 4.9}
