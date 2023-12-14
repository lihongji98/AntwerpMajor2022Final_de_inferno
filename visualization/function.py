from config import faze_player_stats, navi_player_stats, faze_players, navi_players
import numpy as np
import matplotlib.pyplot as plt


def plot_radar_chart(categories, all_values, clicked_players):
    num_plots = len(all_values)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fill_color_list = ['cyan', 'red', 'blue', 'yellow', 'green', 'brown', 'pink',  'purple', 'orange',  'magenta', ]

    for i in range(num_plots):
        values = all_values[i]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
        values = np.concatenate((values, [values[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        ax.plot(angles, values, label=clicked_players[i], color=fill_color_list[i])
        ax.fill(angles, values, alpha=0.7)
        ax.set_xticks(angles[:-1])

    ax.set_ylim(0, 1)
    ax.grid(True, linestyle='--', alpha=0.5)
    if clicked_players:
        ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=10)
        ax.set_xticklabels(categories, fontsize=12, weight='bold')
    plt.close(fig)
    return fig


def show_player_stats(faze_player_clicked, navi_player_clicked):
    metrics_label = ['KPR', 'DPR', 'KAST', 'IMPACT', 'ADR', 'Rating']
    stats = []
    clicked_players = []

    for player in faze_player_clicked.keys():
        if faze_player_clicked[player]:
            player_data = faze_player_stats[player]
            stats.append(player_data)
            clicked_players.append(player)
    for player in navi_player_clicked.keys():
        if navi_player_clicked[player]:
            player_data = navi_player_stats[player]
            stats.append(player_data)
            clicked_players.append(player)
    print(stats)
    fig = plot_radar_chart(metrics_label, stats, clicked_players)
    return fig


def show_heatmap():
    print("show_heatmap")


def show_frags():
    print("show_frags")


def show_weapon_stats():
    print("show_weapon_stats")


def show_others():
    print("show_others")
