import json
import os
import sys

import numpy as np


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


file_path = resource_path("data/frame_data.json")

with open(file_path, 'r') as json_file:
    frame_data = json.load(json_file)

json_file_path = resource_path("data/infernoMask.json")
with open(json_file_path, 'r') as json_file:
    map_mask = json.load(json_file)

frags_path = resource_path("data/frag_data.json")
with open(frags_path, 'r') as json_file:
    frags_data = json.load(json_file)

map_mask = np.array(map_mask)
map_mask = np.where(map_mask == 255, 1, 0)

# round 1-15 34-35
# Faze -> T Navi -> CT
# round 16-30 31-33
# Faze -> CT Navi -> T
faze_T, faze_CT = [], []
navi_T, navi_CT = [], []

for roundNum in frame_data.keys():
    for second in frame_data[roundNum].keys():
        Navi_frame_data = frame_data[roundNum][second][0]['Natus Vincere']
        Faze_frame_data = frame_data[roundNum][second][1]['FaZe Clan']
        if 1 <= int(roundNum) + 1 <= 15 or 34 <= int(roundNum) + 1 <= 35:
            faze_T.append(Faze_frame_data)
            navi_CT.append(Navi_frame_data)
        elif 16 <= int(roundNum) + 1 <= 30 or 31 <= int(roundNum) + 1 <= 33:
            faze_CT.append(Faze_frame_data)
            navi_T.append(Navi_frame_data)

map_scale_parameter = {"pos_x": -2087.0, "pos_y": 3870.0, "scale": 4.9}
