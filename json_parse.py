import json
import pandas as pd


class JsonParser:
    def __init__(self):
        self.Matches = {}
        self.Teams = {}
        self.Players = {}
        self.Rounds = {}
        self.Frags = {}
        self.Frames = {}

    def parse(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

        # First get the general match information.
        general_info_keys = ['matchID', 'mapName']  # 'gameRounds'
        for key in general_info_keys:
            self.Matches[key] = data[key]

        self.Matches['team1'] = data['gameRounds'][0]['ctSide']['teamName']
        self.Matches['team2'] = data['gameRounds'][0]['tSide']['teamName']

        print(self.Matches)
a = JsonParser()
a.parse("D:/Liquid-Faze-BLAST2022.json")
