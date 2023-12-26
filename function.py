from config import faze_player_stats, navi_player_stats, MatchInfo
import numpy as np
from data import map_scale_parameter, faze_T, faze_CT, navi_T, navi_CT, map_mask
from data import frags_data
import matplotlib.pyplot as plt


def plot_radar_chart(categories, all_values, clicked_players):
    num_plots = len(all_values)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fill_color_list = ['cyan', 'red', 'blue', 'yellow', 'green', 'brown', 'pink', 'purple', 'orange', 'magenta', ]

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


def plot_heatmap(heatmap):
    plt.style.use('default')
    background_image = plt.imread(MatchInfo.map_path)
    fig, ax = plt.subplots(figsize=(7.45, 7.45))

    mask = np.ma.masked_where(heatmap == 0.00, heatmap)
    alpha_values = mask * 1

    heatmap_rgba = plt.cm.get_cmap('coolwarm')(heatmap)
    heatmap_rgba[..., 3] = alpha_values

    ax.imshow(background_image, zorder=0, alpha=1)
    ax.imshow(heatmap_rgba, origin='lower', cmap='coolwarm')  # alpha=0.85)
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.get_xaxis().set_visible(b=False)
    ax.get_yaxis().set_visible(b=False)
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.close(fig)
    return fig


def position_scaling_int(x, y):
    scaled_x = (x - map_scale_parameter["pos_x"]) / map_scale_parameter["scale"]
    scaled_y = (map_scale_parameter["pos_y"] - y) / map_scale_parameter["scale"]
    return round(scaled_x), round(scaled_y)


def position_scaling_float(x, y):
    scaled_x = (x - map_scale_parameter["pos_x"]) / map_scale_parameter["scale"]
    scaled_y = (map_scale_parameter["pos_y"] - y) / map_scale_parameter["scale"]
    return scaled_x, scaled_y


def gaussian_distribution(x, y, mu_x, mu_y):
    sigma_x, sigma_y = 25, 25
    exponent = -0.5 * ((x - mu_x) ** 2 / sigma_x ** 2 + (y - mu_y) ** 2 / sigma_y ** 2)
    return np.exp(exponent) / (2 * np.pi * sigma_x * sigma_y)


def compute_heat_map(tracking_data, heat_map, player_index):
    # faze_players = ["twistzz", "broky", "karrigan", "rain",  "ropz"]
    # navi_players = ["boombl4", "perfecto", "bit", "electronic", "simple"]
    for player_pos_dict in tracking_data:
        for i, player in enumerate(player_pos_dict.keys()):
            if player_index == i:
                player_x, player_y = position_scaling_int(player_pos_dict[player][0], player_pos_dict[player][1])
                player_hp = player_pos_dict[player][-1]
                if player_hp != 0:
                    x = np.linspace(player_x - 50, player_x + 51, 101)
                    y = np.linspace(player_y - 50, player_y + 51, 101)
                    y, x = np.meshgrid(y, x)
                    heat = gaussian_distribution(y, x, player_y, player_x)
                    heat_map[i][player_y - 50:player_y + 51, player_x - 50:player_x + 51] += heat
    heat_map[player_index] = ((heat_map[player_index] - np.min(heat_map[player_index]))
                              / (np.max(heat_map[player_index]) - np.min(heat_map[player_index])))
    heat_map[player_index] *= map_mask
    return heat_map[player_index]


def show_T_heatmap(faze_player_clicked, navi_player_clicked):
    T_heatmaps = []
    faze_heatmap = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
    for player in faze_player_clicked.keys():
        if faze_player_clicked[player]:
            if player == 'Twistzz':
                T_heatmaps.append(compute_heat_map(faze_T, faze_heatmap, 0))
            elif player == 'broky':
                T_heatmaps.append(compute_heat_map(faze_T, faze_heatmap, 1))
            elif player == 'karrigan':
                T_heatmaps.append(compute_heat_map(faze_T, faze_heatmap, 2))
            elif player == 'rain':
                T_heatmaps.append(compute_heat_map(faze_T, faze_heatmap, 3))
            elif player == 'ropz':
                T_heatmaps.append(compute_heat_map(faze_T, faze_heatmap, 4))

    navi_heatmap = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
    for player in navi_player_clicked.keys():
        if navi_player_clicked[player]:
            if player == 'Boombl4':
                T_heatmaps.append(compute_heat_map(navi_T, navi_heatmap, 0))
            elif player == 'Perfecto':
                T_heatmaps.append(compute_heat_map(navi_T, navi_heatmap, 1))
            elif player == 'b1t':
                T_heatmaps.append(compute_heat_map(navi_T, navi_heatmap, 2))
            elif player == 'electroNic':
                T_heatmaps.append(compute_heat_map(navi_T, navi_heatmap, 3))
            elif player == 's1mple':
                T_heatmaps.append(compute_heat_map(navi_T, navi_heatmap, 4))

    T_heatmaps = np.array(T_heatmaps).reshape(-1, 1024, 1024)
    T_heatmaps = np.sum(T_heatmaps, axis=0)

    assert T_heatmaps.shape == (1024, 1024), "Heatmap shape is not correct"
    T_heatmaps = plot_heatmap(T_heatmaps)
    return T_heatmaps


def show_CT_heatmap(faze_player_clicked, navi_player_clicked):
    CT_heatmaps = []
    faze_heatmap = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
    for player in faze_player_clicked.keys():
        if faze_player_clicked[player]:
            if player == 'Twistzz':
                CT_heatmaps.append(compute_heat_map(faze_CT, faze_heatmap, 0))
            elif player == 'broky':
                CT_heatmaps.append(compute_heat_map(faze_CT, faze_heatmap, 1))
            elif player == 'karrigan':
                CT_heatmaps.append(compute_heat_map(faze_CT, faze_heatmap, 2))
            elif player == 'rain':
                CT_heatmaps.append(compute_heat_map(faze_CT, faze_heatmap, 3))
            elif player == 'ropz':
                CT_heatmaps.append(compute_heat_map(faze_CT, faze_heatmap, 4))

    navi_heatmap = [np.zeros(shape=(1024, 1024)) for _ in range(5)]
    for player in navi_player_clicked.keys():
        if navi_player_clicked[player]:
            if player == 'Boombl4':
                CT_heatmaps.append(compute_heat_map(navi_CT, navi_heatmap, 0))
            elif player == 'Perfecto':
                CT_heatmaps.append(compute_heat_map(navi_CT, navi_heatmap, 1))
            elif player == 'b1t':
                CT_heatmaps.append(compute_heat_map(navi_CT, navi_heatmap, 2))
            elif player == 'electroNic':
                CT_heatmaps.append(compute_heat_map(navi_CT, navi_heatmap, 3))
            elif player == 's1mple':
                CT_heatmaps.append(compute_heat_map(navi_CT, navi_heatmap, 4))

    CT_heatmaps = np.array(CT_heatmaps).reshape(-1, 1024, 1024)
    CT_heatmaps = np.sum(CT_heatmaps, axis=0)

    assert CT_heatmaps.shape == (1024, 1024), "Heatmap shape is not correct"
    CT_heatmaps = plot_heatmap(CT_heatmaps)
    return CT_heatmaps


def plot_frag(frags):
    plt.style.use('default')
    frags = np.array(frags).reshape(-1, 5).T
    attackerX, attackerY = position_scaling_float(np.array(frags[0], dtype=np.float32),
                                                  np.array(frags[1], dtype=np.float32))
    victimX, victimY = position_scaling_float(np.array(frags[2], dtype=np.float32),
                                              np.array(frags[3], dtype=np.float32))

    background_image = plt.imread(MatchInfo.map_path)
    fig, ax = plt.subplots(figsize=(7.45, 7.45))
    ax.imshow(background_image, zorder=0, alpha=1, origin="lower")
    ax.scatter(attackerX, attackerY, color='b', zorder=5, marker='o')
    ax.scatter(victimX, victimY, color='r', zorder=5, marker='x')
    for aX, aY, vX, vY in zip(attackerX, attackerY, victimX, victimY):
        plt.annotate('', xy=(vX, vY), xytext=(aX, aY),
                     arrowprops=dict(facecolor='#FFFF00', linewidth=1, alpha=0.9, edgecolor='none', width=1))

    ax.set_ylim(ax.get_ylim()[::-1])
    ax.get_xaxis().set_visible(b=False)
    ax.get_yaxis().set_visible(b=False)
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.close(fig)
    return fig


def show_T_frags(faze_player_clicked, navi_player_clicked):
    T_frags = []
    for player in faze_player_clicked.keys():
        if faze_player_clicked[player]:
            player_frags = frags_data["faze_T"][player]
            for i, frag in enumerate(player_frags):
                T_frags.append(frag)
    for player in navi_player_clicked.keys():
        if navi_player_clicked[player]:
            player_frags = frags_data["navi_T"][player]
            for i, frag in enumerate(player_frags):
                T_frags.append(frag)

    fig = plot_frag(T_frags)
    return fig


def show_CT_frags(faze_player_clicked, navi_player_clicked):
    CT_frags = []
    for player in faze_player_clicked.keys():
        if faze_player_clicked[player]:
            player_frags = frags_data["faze_CT"][player]
            for i, frag in enumerate(player_frags):
                CT_frags.append(frag)
    for player in navi_player_clicked.keys():
        if navi_player_clicked[player]:
            player_frags = frags_data["navi_CT"][player]
            for i, frag in enumerate(player_frags):
                CT_frags.append(frag)

    fig = plot_frag(CT_frags)
    return fig
