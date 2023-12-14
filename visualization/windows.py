import tkinter as tk
import functools
from __init__ import Config, MatchInfo, faze_players, navi_players
from __init__ import faze_player_stats, navi_player_stats
from util import create_map, create_circle_image, center_window
from function import show_player_stats, show_heatmap, show_frags, show_weapon_stats, show_others
from PIL import Image, ImageTk, ImageDraw


def player_button(player_name, team_name):
    result_label.config(text=f"You clicked on {player_name} from {team_name}!")


def team_button(team_name):
    result_label.config(text=f"You clicked on {team_name}!")


def major_button(major_name):
    result_label.config(text=f"You clicked on {major_name}!")


def create_team_label(frame, team_name, logo_path, size, side):
    team_logo = Image.open(logo_path)
    team_logo = team_logo.resize((size, size), Image.LANCZOS)
    team_logo = ImageTk.PhotoImage(team_logo)

    # Create team label with logo and name
    team_label = tk.Label(frame, text=team_name, image=team_logo, compound=tk.TOP, bg=Config.bg_color,
                          fg=Config.fg_color,
                          font=Config.team_font)
    team_label.image = team_logo

    # Pack team label based on the specified side
    if side == "left":
        team_label.pack(side=tk.TOP)
    elif side == "right":
        team_label.pack(side=tk.TOP)
    team_label.bind("<Button-1>", lambda event, team=team_label.cget("text"): team_button(team))

    return team_label


def create_player_labels(frame, team_label, image_paths, size, team):
    labels = []
    for path in image_paths:
        player_id = path[11:-4]
        icon = create_circle_image(path, size)
        label = tk.Label(frame, relief="solid", image=icon, text=player_id, compound=tk.TOP, padx=10, pady=10, bg=Config.bg_color, fg=Config.fg_color, font=Config.player_font)
        label.image = icon
        label.pack(side=tk.TOP)
        label.bind("<Button-1>", lambda event, player=player_id: player_button(player, team))
        labels.append(label)
    return labels



def create_major_icon(frame, image_path, size):
    major_icon = Image.open(image_path)
    major_icon = major_icon.resize((size[0], size[1]), Image.LANCZOS)
    major_icon = ImageTk.PhotoImage(major_icon)
    major_name = "Antwerp 2022 Final"
    major_label = tk.Label(frame, image=major_icon, bg=Config.bg_color, text=major_name, fg=Config.fg_color, font=Config.team_font)
    major_label.image = major_icon
    major_label.pack(side=tk.TOP)
    major_label.bind("<Button-1>", lambda event, name=major_label.cget("text"): major_button(name))

    return major_label


def create_function_button(frame, text, x, y, command):
    button = tk.Button(frame, text=text, font=Config.button_font, width=Config.button_width, height=Config.button_height, command=command)
    button.place(x=x, y=y)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Circular Icon Window")
    center_window(window, Config.window_height, Config.window_width)
    window.configure(bg=Config.bg_color)

    left_frame = tk.Frame(window, bg=Config.bg_color)
    left_frame.pack(side=tk.LEFT)
    right_frame = tk.Frame(window, bg=Config.bg_color)
    right_frame.pack(side=tk.RIGHT)

    faze_team_label = create_team_label(left_frame, "FaZe", MatchInfo.faze_logo_path, Config.team_icon_size, "left")
    navi_team_label = create_team_label(right_frame, "Na'Vi", MatchInfo.navi_logo_path, Config.team_icon_size, "right")

    faze_player_labels = create_player_labels(window, faze_team_label, MatchInfo.faze_paths, Config.player_icon_size, "faze")
    navi_player_labels = create_player_labels(window, navi_team_label, MatchInfo.navi_paths, Config.player_icon_size, "navi")

    major_image_label = create_major_icon(window, MatchInfo.major_path, size=[500, 140])

    map_image_label = create_map(window, MatchInfo.map_path, map_size=800)

    result_label = tk.Label(window, text="", font=Config.player_font, fg=Config.fg_color, bg=Config.bg_color)
    result_label.pack(pady=45)

    create_function_button(window, "Player Stats", x=300, y=Config.function_button_y, command=show_player_stats)
    create_function_button(window, "Player Heatmap", x=450, y=Config.function_button_y, command=show_heatmap)
    create_function_button(window, "Frags", x=600, y=Config.function_button_y, command=show_frags)
    create_function_button(window, "Weapon Stats", x=750, y=Config.function_button_y, command=show_weapon_stats)
    create_function_button(window, "others", x=900, y=Config.function_button_y, command=show_others)

    window.mainloop()
