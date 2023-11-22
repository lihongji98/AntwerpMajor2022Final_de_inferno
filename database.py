from mongoengine.fields import *
import mongoengine as meng


class Team(meng.DynamicDocument):
    team = StringField(required=True, unique=True)

    meta = {
        'indexes': ['team'],
        'db_alias': 'default'
    }


class Match(meng.DynamicDocument):
    matchID = StringField(required=True, unique=True)
    mapName = StringField()
    team1 = StringField(required=True)
    team2 = StringField(required=True)

    meta = {
        'indexes': ['matchID', 'team1', 'team2'],
        'db_alias': 'default'
    }


class Player(meng.DynamicDocument):
    player_name = StringField(required=True, unique=True)
    steam_id = IntField(required=True)
    team = StringField()

    meta = {
        'indexes': ['player_name', 'steam_id'],
        'db_alias': 'default'
    }
