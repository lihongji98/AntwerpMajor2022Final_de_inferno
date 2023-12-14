import json

import mongoengine as mongo
from tqdm import tqdm

from visualization.config import MatchInfo

import database


def connect_db():
    return mongo.connect(db="csgo", username="lihong", password="1998918!", host="localhost", port=27017)


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


frame_data = get_frame_data(MatchInfo.matchID)
file_path = "frame_data.json"
# Write the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(frame_data, json_file)
