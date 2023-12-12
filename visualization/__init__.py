faze_players = ["karrigan", "rain", "broky", "twistzz", "ropz"]
navi_players = ["boombl4", "electronic", "simple", "bit", "perfecto"]


class Config(object):
    bg_color = "#000000"
    fg_color = "#F3F9F1"
    team_font = "casadia 20"
    player_font = "casadia 12"
    button_font = "casadia 10"
    window_height, window_width = 1280, 960
    button_height, button_width = 1, 12
    player_icon_size = 75
    team_icon_size = 200
    function_button_y = 150


class MatchInfo(object):
    faze_paths = ["icons/faze/" + player + ".png" for player in faze_players]
    navi_paths = ["icons/navi/" + player + ".png" for player in navi_players]
    faze_logo_path = "icons/faze_logo.png"
    navi_logo_path = "icons/navi_logo.png"
    major_path = "icons/Antwerp.png"
    map_path = "../Maps/mapMetaData/de_inferno.png"


# name : [KPR, DPR, KAST, Impact, ADR, Rating]
faze_player_stats = {"karrigan": [0.69, 0.74, 0.743, 1.05, 73.5, 1.04],
                     "rain": [0.63, 0.69, 0.714, 1.72, 89.9, 1.25],
                     "broky": [0.86, 0.63, 0.771, 1.36, 78.2, 1.29],
                     "twistzz": [0.66, 0.69, 0.714, 0.89, 67.9, 0.96],
                     "ropz": [0.63, 0.6, 0.771, 1.04, 70.2, 1.13]}

navi_player_stats = {"boombl4": [1.02, 0.63, 0.741, 0.88, 68.2, 0.6],
                     "eletronic": [0.54, 0.8, 0.629, 0.76, 70.7, 0.84],
                     "simple": [0.8, 0.86, 0.743, 1.2, 75.4, 1.04],
                     "bit": [0.74, 0.54, 0.771, 1.18, 83.5, 1.27],
                     "perfecto": [0.83, 0.6, 0.8, 1.14, 81.2, 1.26]}
