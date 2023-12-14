import json

import numpy as np

file_path = r"D:\pycharm_projects\CSGO_Analytics\visualization\data\frame_data.json"

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

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

print(faze_T[0])
print(faze_T[1])

map_scale_parameter = {"pos_x": -2087.0, "pos_y": 3870.0, "scale": 4.9}


def _position_scaling(x, y):
    scaled_x = (x - map_scale_parameter["pos_x"]) / map_scale_parameter["scale"]
    scaled_y = (map_scale_parameter["pos_y"] - y) / map_scale_parameter["scale"]
    return round(scaled_x), round(scaled_y)


faze_heat_map_T = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
faze_heat_map_CT = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
navi_heat_map_T = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
navi_heat_map_CT = [np.zeros(shape=(1024, 1024)) for _ in range(5)]

for player_pos_dict in faze_T:
    for i, player in enumerate(player_pos_dict.keys()):
        player_name = player
        player_x, player_y = _position_scaling(player_pos_dict[player][0], player_pos_dict[player][1])
        player_hp = player_pos_dict[player][-1]
        print(player_name, player_x, player_y, player_hp)
        if player_hp != 0:
            faze_heat_map_T[i][player_x][player_y] += 100
