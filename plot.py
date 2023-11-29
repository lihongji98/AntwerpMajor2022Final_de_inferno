import database
import pandas as pd
import numpy as np
import mongoengine as mongo
import matplotlib.pyplot as plt


def connect_db():
    return mongo.connect(db="csgo", username="lihong", password="1998918!", host="localhost", port=27017)


class FrameVisualizer:
    def __init__(self, matchMap="de_mirage.png"):
        self.matchID = None
        self.map = matchMap
        self.mirage_parameter = {"pos_x": -3230.0,
                                 "pos_y": 1713.0,
                                 "scale": 5.0}
        self.inferno_parameter = {"pos_x": -2087.0,
                                  "pos_y": 3870.0,
                                  "scale": 4.9}

    def position_transformation(self, coordinate, pos_type):
        start_x = self.mirage_parameter["pos_x"]
        start_y = self.mirage_parameter["pos_y"]
        scale = self.mirage_parameter["scale"]
        if pos_type == "player":
            coordinate = np.array(coordinate).reshape(5, 2)
            for i in range(len(coordinate)):
                coordinate[i][0] = (coordinate[i][0] - start_x) / scale
                coordinate[i][1] = (start_y - coordinate[i][1]) / scale
        elif pos_type == "bomb":
            coordinate = np.array(coordinate).reshape(1, 2)
            coordinate[0][0] = (coordinate[0][0] - start_x) / scale
            coordinate[0][1] = (start_y - coordinate[0][1]) / scale
        else:
            msg = "Choose 'player' or 'bomb' position!"
            ValueError(msg)
        return coordinate

    def match_info_retrieve(self,
                            series="Liquid-Faze-BLAST2022",
                            map_name="de_mirage",
                            team_lose="FaZe Clan",
                            team_win="Team Liquid"):
        self.matchID = database.Match.objects(Series=series,
                                              mapName=map_name,
                                              teamLose=team_lose,
                                              teamWin=team_win)[0].id

    def frame_info_retrieve(self, round_num=0):
        frame_info = database.Frame.objects(matchID=self.matchID, roundNum=round_num)
        frameNum = len(frame_info)

        first_frame = frame_info[0]  # choose which frame to plot
        bomb_coordinate = [[first_frame.bomb.x, first_frame.bomb.y]]

        # "name": first_frame.team1FrameDict.teamName,
        def get_player_position(teamSide):
            if teamSide == "team1":
                playerInfoDict = first_frame.team1FrameDict.playerFrameDict
            elif teamSide == "team2":
                playerInfoDict = first_frame.team2FrameDict.playerFrameDict
            else:
                ValueError("Choose 'team1' or 'team2' to extract position information.")
            team = {"player1_pos": [playerInfoDict[0].playerX,
                                    playerInfoDict[0].playerY],
                    "player2_pos": [playerInfoDict[1].playerX,
                                    playerInfoDict[1].playerY],
                    "player3_pos": [playerInfoDict[2].playerX,
                                    playerInfoDict[2].playerY],
                    "player4_pos": [playerInfoDict[3].playerX,
                                    playerInfoDict[3].playerY],
                    "player5_pos": [playerInfoDict[4].playerX,
                                    playerInfoDict[4].playerY]
                    }
            team_pos = [[team[player_index][0], team[player_index][1]] for player_index in team.keys()]
            return team_pos

        team1_pos = get_player_position("team1")
        team2_pos = get_player_position("team2")

        team1_position = self.position_transformation(team1_pos, "player")
        team2_position = self.position_transformation(team2_pos, "player")
        bomb_position = self.position_transformation(bomb_coordinate, "bomb")
        pos_dict = {"team1": {"name": first_frame.team1FrameDict.teamName, "position": team1_position},
                    "team2": {"name": first_frame.team2FrameDict.teamName, "position": team2_position},
                    "bomb": bomb_position}
        return pos_dict

    def plot(self, pos_dict):
        img = plt.imread(self.map)
        fig, ax = plt.subplots(dpi=300)
        ax.imshow(img, zorder=0)

        team1_name, team1_position = pos_dict["team1"]["name"], pos_dict["team1"]["position"]
        team2_name, team2_position = pos_dict["team2"]["name"], pos_dict["team2"]["position"]
        bomb_position = pos_dict["bomb"]

        x_values1, y_values1 = zip(*team1_position)
        x_values2, y_values2 = zip(*team2_position)
        x_bomb, y_bomb = zip(*bomb_position)

        plt.scatter(
            x=x_values1,
            y=y_values1,
            color='blue',
            marker='.')
        plt.scatter(
            x=x_values2,
            y=y_values2,
            color='red',
            marker='.')
        plt.scatter(
            x=x_bomb,
            y=y_bomb,
            color='orange',
            marker='.')

        ax.get_xaxis().set_visible(b=False)
        ax.get_yaxis().set_visible(b=False)
        plt.show()

    def run(self):
        connect_db()
        self.match_info_retrieve(series="Liquid-Faze-BLAST2022",
                                 map_name="de_mirage",
                                 team_lose="FaZe Clan",
                                 team_win="Team Liquid")
        pos = self.frame_info_retrieve(round_num=0)
        self.plot(pos)


a = FrameVisualizer()
a.run()
