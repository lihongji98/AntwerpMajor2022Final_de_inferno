import json

import mongoengine as mongo
from tqdm import tqdm

from visualization.config import MatchInfo

import database
from visualization.config import faze_players, navi_players


def connect_db():
    return mongo.connect(db="csgo", username="lihong", password="1998918!", host="localhost", port=27017)


def get_team_player_info():
    faze_player_list, navi_player_list = [], []
    connect_db()
    faze_players = database.Player.objects(team='FaZe Clan')
    for player in faze_players:
        faze_player_list.append(player.player_name)
    navi_players = database.Player.objects(team="Natus Vincere")
    for player in navi_players:
        navi_player_list.append(player.player_name)
    return faze_player_list, navi_player_list


def get_frame_data(matchID):
    connect_db()
    frame_data = {}
    seconds_d = {}
    round_recorder = 0
    total_frames = database.Frame.objects(matchID=matchID)
    for i, frame in enumerate(tqdm(total_frames)):
        roundNum = total_frames[i].roundNum
        second = total_frames[i].seconds
        team1Name, team2Name = total_frames[i].team1FrameDict.teamName, total_frames[i].team2FrameDict.teamName
        team1PlayerFrame = total_frames[i].team1FrameDict.playerFrameDict
        team1player1Name = team1PlayerFrame[0]['playerName']
        team1player2Name = team1PlayerFrame[1]['playerName']
        team1player3Name = team1PlayerFrame[2]['playerName']
        team1player4Name = team1PlayerFrame[3]['playerName']
        team1player5Name = team1PlayerFrame[4]['playerName']

        team1player1Info = [team1PlayerFrame[0]['playerX'], team1PlayerFrame[0]['playerY'], team1PlayerFrame[0]['hp']]
        team1player2Info = [team1PlayerFrame[1]['playerX'], team1PlayerFrame[1]['playerY'], team1PlayerFrame[1]['hp']]
        team1player3Info = [team1PlayerFrame[2]['playerX'], team1PlayerFrame[2]['playerY'], team1PlayerFrame[2]['hp']]
        team1player4Info = [team1PlayerFrame[3]['playerX'], team1PlayerFrame[3]['playerY'], team1PlayerFrame[3]['hp']]
        team1player5Info = [team1PlayerFrame[4]['playerX'], team1PlayerFrame[4]['playerY'], team1PlayerFrame[4]['hp']]

        team2PlayerFrame = total_frames[i].team2FrameDict.playerFrameDict
        team2player1Name = team2PlayerFrame[0]['playerName']
        team2player2Name = team2PlayerFrame[1]['playerName']
        team2player3Name = team2PlayerFrame[2]['playerName']
        team2player4Name = team2PlayerFrame[3]['playerName']
        team2player5Name = team2PlayerFrame[4]['playerName']

        team2player1Info = [team2PlayerFrame[0]['playerX'], team2PlayerFrame[0]['playerY'], team2PlayerFrame[0]['hp']]
        team2player2Info = [team2PlayerFrame[1]['playerX'], team2PlayerFrame[1]['playerY'], team2PlayerFrame[1]['hp']]
        team2player3Info = [team2PlayerFrame[2]['playerX'], team2PlayerFrame[2]['playerY'], team2PlayerFrame[2]['hp']]
        team2player4Info = [team2PlayerFrame[3]['playerX'], team2PlayerFrame[3]['playerY'], team2PlayerFrame[3]['hp']]
        team2player5Info = [team2PlayerFrame[4]['playerX'], team2PlayerFrame[4]['playerY'], team2PlayerFrame[4]['hp']]

        team1_player_d = {team1player1Name: team1player1Info,
                          team1player2Name: team1player2Info,
                          team1player3Name: team1player3Info,
                          team1player4Name: team1player4Info,
                          team1player5Name: team1player5Info}
        team2_player_d = {team2player1Name: team2player1Info,
                          team2player2Name: team2player2Info,
                          team2player3Name: team2player3Info,
                          team2player4Name: team2player4Info,
                          team2player5Name: team2player5Info}

        team1_d, team2_d = {team1Name: team1_player_d}, {team2Name: team2_player_d}

        seconds_d[second] = [team1_d, team2_d]

        frame_data[roundNum] = seconds_d
        if roundNum != round_recorder:
            round_recorder += 1
            seconds_d = {}

    return frame_data


def get_frag_data(matchID):
    connect_db()
    frag_T_faze_data = {faze_players[0]: [],
                        faze_players[1]: [],
                        faze_players[2]: [],
                        faze_players[3]: [],
                        faze_players[4]: []
                        }

    frag_T_navi_data = {navi_players[0]: [],
                        navi_players[1]: [],
                        navi_players[2]: [],
                        navi_players[3]: [],
                        navi_players[4]: []
                        }

    frag_CT_faze_data = {faze_players[0]: [],
                         faze_players[1]: [],
                         faze_players[2]: [],
                         faze_players[3]: [],
                         faze_players[4]: []
                         }

    frag_CT_navi_data = {navi_players[0]: [],
                         navi_players[1]: [],
                         navi_players[2]: [],
                         navi_players[3]: [],
                         navi_players[4]: []
                         }

    total_frags = database.Frag.objects(matchID=matchID)
    round_counter = 0
    for i, frag in enumerate(total_frags):
        if 1 <= int(frag.roundNum) + 1 <= 15 or 34 <= int(frag.roundNum) + 1 <= 35:
            frame_frag = [float(frag.attackerX), float(frag.attackerY),
                          float(frag.victimX), float(frag.victimY),
                          frag.weaponClass]
            if frag.attackerName in faze_players: frag_T_faze_data[frag.attackerName].append(frame_frag)
            else: frag_CT_navi_data[frag.attackerName].append(frame_frag)

        elif 16 <= int(frag.roundNum) + 1 <= 30 or 31 <= int(frag.roundNum) + 1 <= 33:
            frame_frag = [float(frag.attackerX), float(frag.attackerY),
                          float(frag.victimX), float(frag.victimY),
                          frag.weaponClass]
            if frag.attackerName in faze_players: frag_CT_faze_data[frag.attackerName].append(frame_frag)
            else: frag_T_navi_data[frag.attackerName].append(frame_frag)
    return frag_T_faze_data, frag_T_navi_data, frag_CT_faze_data, frag_CT_navi_data


# frame_data = get_frame_data(MatchInfo.matchID)
# file_path = "frame_data.json"
# with open(file_path, 'w') as json_file:
#     json.dump(frame_data, json_file)

faze_player_list, navi_player_list = get_team_player_info()
frag_T_faze_data, frag_T_navi_data, frag_CT_faze_data, frag_CT_navi_data = get_frag_data(MatchInfo.matchID)
frag_data = {"faze_T": frag_T_faze_data,
             "faze_CT": frag_CT_faze_data,
             "navi_T": frag_T_navi_data,
             "navi_CT": frag_CT_navi_data}
file_path = "frag_data.json"
with open(file_path, 'w') as json_file:
    json.dump(frag_data, json_file)
