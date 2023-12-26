from numpy import array, max, min, concatenate
import os
import sys
from bson import ObjectId

faze_players = ["karrigan", "rain", "broky", "Twistzz", "ropz"]
navi_players = ["Boombl4", "electroNic", "s1mple", "b1t", "Perfecto"]

metrics = ["Player_Stats", "T_Heatmap", "CT_Heatmap", "T_Frags", "CT_Frags", "overview"]


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Config(object):
    bg_color, fg_color = "#000000", "#F3F9F1"
    team_font = "casadia 18"
    player_font = "casadia 12"
    button_font = "casadia 10"

    window_height, window_width = 1280, 960
    button_height, button_width = 1, 12

    inferno_size = 750
    player_icon_size = 75
    team_icon_size = 200

    function_button_y = 150


class MatchInfo(object):
    matchID = ObjectId("656c9a14a038bfba3be1021d")
    faze_paths = [resource_path("icons/faze/" + player + ".png") for player in faze_players]
    navi_paths = [resource_path("icons/navi/" + player + ".png") for player in navi_players]
    faze_logo_path = resource_path("icons/faze_logo.png")
    navi_logo_path = resource_path("icons/navi_logo.png")
    major_path = resource_path("icons/Antwerp.png")
    map_path = resource_path("icons/de_inferno.png")
    overview_path = resource_path("icons/overview.png")


# name : [KPR, DPR, KAST, Impact, ADR, Rating]
faze_player_stats = {"karrigan": [0.69, 0.74, 0.743, 1.05, 73.5 / 100, 1.04],
                     "rain": [0.63, 0.69, 0.714, 1.72, 89.9 / 100, 1.25],
                     "broky": [0.86, 0.63, 0.771, 1.36, 78.2 / 100, 1.29],
                     "Twistzz": [0.66, 0.69, 0.714, 0.89, 67.9 / 100, 0.96],
                     "ropz": [0.63, 0.6, 0.771, 1.04, 70.2 / 100, 1.13]}

navi_player_stats = {"Boombl4": [1.02, 0.63, 0.741, 0.88, 68.2 / 100, 0.6],
                     "electroNic": [0.54, 0.8, 0.629, 0.76, 70.7 / 100, 0.84],
                     "s1mple": [0.8, 0.86, 0.743, 1.2, 75.4 / 100, 1.04],
                     "b1t": [0.74, 0.54, 0.771, 1.18, 83.5 / 100, 1.27],
                     "Perfecto": [0.83, 0.6, 0.8, 1.14, 81.2 / 100, 1.26]}

faze_stats = array(list(faze_player_stats.values()))
navi_stats = array(list(navi_player_stats.values()))
total_stats = concatenate((faze_stats, navi_stats), axis=0).T
total_stats[1] = 1 - total_stats[1]
for i in range(len(total_stats)):
    max_stat, min_stat = max(total_stats[i]), min(total_stats[i]) - 0.2
    total_stats[i] = (total_stats[i] - min_stat) / (max_stat - min_stat)

faze_player_stat_value = total_stats.T[0:5]
navi_player_stat_value = total_stats.T[5:]

faze_player_stats = {player_name: list(faze_player_stat_value[i]) for i, player_name in
                     enumerate(faze_player_stats.keys())}
navi_player_stats = {player_name: list(navi_player_stat_value[i]) for i, player_name in
                     enumerate(navi_player_stats.keys())}
