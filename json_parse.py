import json
import pandas as pd
import database
import mongoengine as mongo


def connect_db():
    return mongo.connect(db="csgo", username="lihong", password="1998918!", host="localhost", port=27017)


class JsonParser:
    def __init__(self):
        self.Matches = []
        self.Teams = []
        self.Players = []
        self.Rounds = []
        self.Frags = []
        self.Frames = []

    def parse(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

        """
        First get the general match information.
        """
        general_info_keys = ['matchID', 'mapName']  # 'gameRounds'
        match_info_dict = {}
        for key in general_info_keys:
            match_info_dict[key] = data[key]

        match_info_dict['team1'] = data['gameRounds'][0]['ctSide']['teamName']
        match_info_dict['team2'] = data['gameRounds'][0]['tSide']['teamName']
        self.Matches.append(match_info_dict)

        """
        Second get the team information.
        """
        self.Teams.append({'team': data['gameRounds'][0]['ctSide']['teamName']})
        self.Teams.append({'team': data['gameRounds'][0]['tSide']['teamName']})

        """
        Third get the Player information.
        """

        def player_info_retrieve(team_side):
            for i in range(len(data['gameRounds'][0]['frames'][0][team_side]['players'])):
                player_name = data['gameRounds'][0]['frames'][0][team_side]['players'][i]['name']
                player_steam_id = data['gameRounds'][0]['frames'][0][team_side]['players'][i]['steamID']
                player_team = data['gameRounds'][0]['frames'][0][team_side]['players'][i]['team']
                self.Players.append({'player_name': player_name, 'steam_id': player_steam_id, 'team': player_team})

        player_info_retrieve('t')
        player_info_retrieve('ct')

        """
        Forth get the round information
        """

#    {'matchID': 'Liquid-Faze-BLAST2022', 'mapName': 'de_mirage', 'team1': 'FaZe Clan', 'team2': 'Team Liquid'}
#    {'team': 'FaZe Clan'}
#    {'player_name': 'YEKINDAR', 'steam_id': 76561198134401925, 'team': 'Team Liquid'}

    def update(self):
        connect_db()
        team_json = json.dumps(self.Teams)
        for item in json.loads(team_json):
            existing = database.Team.objects(team=item['team']).first()
            if existing:
                print(f"The team : '{item['team']}' is already in Team collection.")
            else:
                database.Team(**item).save()

        match_json = json.dumps(self.Matches)
        for item in json.loads(match_json):
            if database.Match.objects(matchID=item['matchID']).first():
                print(f"The match with mathID '{item['matchID']}' is already in Match collection.")
            else:
                database.Match(**item).save()

        player_json = json.dumps(self.Players)
        for item in json.loads(player_json):
            if database.Player.objects(player_name=item['player_name']).first():
                print(f"The player: '{item['player_name']}' is already in Player collection.")
            else:
                database.Player(**item).save()


a = JsonParser()
a.parse("D:/Liquid-Faze-BLAST2022.json")
a.update()
