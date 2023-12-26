import tkinter as tk
from tkinter.ttk import Label, Combobox

from PIL import Image, ImageTk

from config import Config, MatchInfo, faze_players, navi_players, metrics
from util import center_window, create_circle_image
from util import create_map, create_overview
from function import show_player_stats, show_T_heatmap, show_CT_heatmap, show_T_frags, show_CT_frags

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas_widget = None
map_fig = None
player_chosen = []
faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}


def clean_widget():
    global canvas_widget
    if canvas_widget is not None:
        canvas_widget.destroy()
        canvas_widget = None


def check_conditions(player, metric, frame):
    global canvas_widget, faze_player_clicked, navi_player_clicked, player_chosen

    clean_widget()
    if player not in player_chosen:
        player_chosen.append(player)
    else:
        player_chosen.remove(player)
    result_label.config(text=f"{metric.get()}: {player_chosen}")

    if player in faze_player_clicked.keys():
        faze_player_clicked[player] = False if faze_player_clicked[player] else True

    elif player in navi_player_clicked.keys():
        navi_player_clicked[player] = False if navi_player_clicked[player] else True
    else:
        ValueError(f"Player {player} is not in both teams")

    #    ["Player_Stats", "Heatmap", "Frags", "Weapon_Stats", "Others"]
    if metric.get() == metrics[0]:
        stats_figure = show_player_stats(faze_player_clicked, navi_player_clicked)
        canvas = FigureCanvasTkAgg(stats_figure, master=frame)
        canvas_widget = canvas.get_tk_widget()
        center_window(frame, Config.window_height, Config.window_width)
        canvas_widget.pack(pady=80)

    elif metric.get() == metrics[1]:
        T_heatmap = show_T_heatmap(faze_player_clicked, navi_player_clicked)
        canvas = FigureCanvasTkAgg(T_heatmap, master=frame)
        canvas_widget = canvas.get_tk_widget()
        center_window(frame, Config.window_height, Config.window_width)
        canvas_widget.place(x=Config.window_height // 2 - Config.inferno_size // 2,
                            y=Config.window_width // 2 - Config.inferno_size // 2 + 100)

    elif metric.get() == metrics[2]:
        CT_heatmap = show_CT_heatmap(faze_player_clicked, navi_player_clicked)
        canvas = FigureCanvasTkAgg(CT_heatmap, master=frame)
        canvas_widget = canvas.get_tk_widget()
        center_window(frame, Config.window_height, Config.window_width)
        canvas_widget.place(x=Config.window_height // 2 - Config.inferno_size // 2,
                            y=Config.window_width // 2 - Config.inferno_size // 2 + 100)

    elif metric.get() == metrics[3]:
        T_frags = show_T_frags(faze_player_clicked, navi_player_clicked)
        canvas = FigureCanvasTkAgg(T_frags, master=frame)
        canvas_widget = canvas.get_tk_widget()
        center_window(frame, Config.window_height, Config.window_width)
        canvas_widget.place(x=Config.window_height // 2 - Config.inferno_size // 2,
                            y=Config.window_width // 2 - Config.inferno_size // 2 + 100)

    elif metric.get() == metrics[4]:
        CT_frags = show_CT_frags(faze_player_clicked, navi_player_clicked)
        canvas = FigureCanvasTkAgg(CT_frags, master=frame)
        canvas_widget = canvas.get_tk_widget()
        center_window(frame, Config.window_height, Config.window_width)
        canvas_widget.place(x=Config.window_height // 2 - Config.inferno_size // 2,
                            y=Config.window_width // 2 - Config.inferno_size // 2 + 100)

    elif metric.get() == metrics[5]:
        _ = create_overview(frame, MatchInfo.overview_path)

    else:
        ValueError("Invalid metric!")


def on_metric_change(event, frame):
    global canvas_widget, map_fig, faze_player_clicked, navi_player_clicked, player_chosen
    selected_metric = event.widget.get()
    print('the selected metric is ' + selected_metric)
    # ["Player_Stats", "Heatmap", "Frags", "Weapon_Stats", "Others"]
    if selected_metric == metrics[0]:
        if map_fig is not None:
            map_fig.destroy()
            map_fig = None
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []

    elif selected_metric == metrics[1]:
        if map_fig is None:
            map_fig = create_map(frame, MatchInfo.map_path, map_size=Config.inferno_size)
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []

    elif selected_metric == metrics[2]:
        if map_fig is None:
            map_fig = create_map(frame, MatchInfo.map_path, map_size=Config.inferno_size)
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []

    elif selected_metric == metrics[3]:
        if map_fig is None:
            map_fig = create_map(frame, MatchInfo.map_path, map_size=Config.inferno_size)
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []

    elif selected_metric == metrics[4]:
        if map_fig is None:
            map_fig = create_map(frame, MatchInfo.map_path, map_size=Config.inferno_size)
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []

    elif selected_metric == metrics[5]:
        if map_fig is None:
            map_fig = create_map(frame, MatchInfo.map_path, map_size=Config.inferno_size)
        faze_player_clicked = {faze_players[i]: False for i in range(len(faze_players))}
        navi_player_clicked = {navi_players[i]: False for i in range(len(navi_players))}
        player_chosen = []


    else:
        ValueError("Invalid metric!")
    clean_widget()


def team_button(team_name):
    result_label.config(text=f"You clicked on {team_name}!")


def major_button(major_name):
    result_label.config(text=f"You clicked on {major_name}!")


def player_button(player_name, metric_combobox, frame):
    check_conditions(player_name, metric_combobox, frame)


def create_team_buttons(frame, team_name, logo_path, size, x, y):
    team_logo = Image.open(logo_path)
    team_logo = team_logo.resize((size, size), Image.LANCZOS)
    team_logo = ImageTk.PhotoImage(team_logo)

    team_compound = tk.TOP if team_name == 'FaZe' else tk.TOP
    team_label = tk.Label(frame, text=team_name + ' Players', image=team_logo, compound=team_compound,
                          bg=Config.bg_color, fg=Config.fg_color, font=Config.team_font,
                          padx=0, pady=0)
    team_label.image = team_logo

    team_label.place(x=x, y=y)
    team_label.bind("<Button-1>",
                    lambda event, team=team_label.cget("text"): team_button(team))

    return team_label


def create_major_buttons(frame, image_path, size):
    major_icon = Image.open(image_path)
    major_icon = major_icon.resize((size[0], size[1]), Image.LANCZOS)
    major_icon = ImageTk.PhotoImage(major_icon)

    major_name = "Antwerp 2022 Final"
    major_label = tk.Label(frame, image=major_icon, bg=Config.bg_color, text=major_name, fg=Config.fg_color,
                           font=Config.team_font)
    major_label.image = major_icon
    major_label.pack(side=tk.TOP)
    major_label.bind("<Button-1>", lambda event, name=major_label.cget("text"): major_button(name))

    return major_label


def create_player_buttons(frame, image_paths, size, x, y, metric_combobox, player_list):
    player_buttons = []
    for i, path in enumerate(image_paths):
        player_id = player_list[i]
        icon = create_circle_image(path, size)
        player_button_frame = tk.Label(frame, relief="solid", image=icon, text=player_id, compound=tk.TOP,
                                       padx=0, pady=0,
                                       bg=Config.bg_color,
                                       fg=Config.fg_color, font=Config.player_font)
        player_button_frame.image = icon
        player_button_frame.place(x=x, y=y + i * 135)
        player_button_frame.bind("<Button-1>",
                                 lambda event, player=player_button_frame.cget("text"):
                                 player_button(player, metric_combobox, frame))
        player_buttons.append(player_button_frame)
    return player_buttons


def create_slider(frame, metrics_category):
    slider_label = Label(frame, text="Select one metirc to visualize: ",
                         font=Config.team_font, foreground=Config.fg_color, background=Config.bg_color)
    slider_label.place(x=Config.window_height // 2 - 250, y=Config.window_width // 6 + 20)
    selected_metric = tk.StringVar()
    metric_combobox = Combobox(frame, textvariable=selected_metric, values=metrics_category, state='readonly')
    metric_combobox.place(x=Config.window_height // 2 + 100, y=Config.window_width // 6 + 25)

    metric_combobox.bind("<<ComboboxSelected>>",
                         lambda event: on_metric_change(event, frame))
    return metric_combobox


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Anterwep Major 2020 The Final Visualization")
    center_window(window, Config.window_height, Config.window_width)
    window.configure(bg=Config.bg_color)

    map_fig = create_overview(window, MatchInfo.overview_path)
    major_image_label = create_major_buttons(window, MatchInfo.major_path, size=[500, 140])

    result_label = tk.Label(window, text="", font=Config.player_font, fg=Config.fg_color, bg=Config.bg_color)
    result_label.pack(pady=0)

    metric_slider = create_slider(window, metrics)

    faze_team_label = create_team_buttons(window, "FaZe", MatchInfo.faze_logo_path, Config.team_icon_size, 50, 0)
    navi_team_label = create_team_buttons(window, "Na'Vi", MatchInfo.navi_logo_path, Config.team_icon_size, 1020, 0)

    faze_player_labels = create_player_buttons(window, MatchInfo.faze_paths, Config.player_icon_size,
                                               100, 230, metric_slider, faze_players)
    navi_player_labels = create_player_buttons(window, MatchInfo.navi_paths, Config.player_icon_size,
                                               1070, 230, metric_slider, navi_players)

    window.mainloop()
