import json

from world import World
from player import Player


class Game:

    players = {}

    def __init__(self):
        super().__init__()
        self.world = World()
        self.world.load('levels/example.level')

    def add_player(self, connection):
        if connection in self.players:
            raise ValueError("Player already in game")

        self.players[connection] = Player()

        data = self.world.as_dict()
        data.update({'type': 'world'})

        connection.sendMessage(json.dumps(data).encode('utf8'))

        print("Players connected", len(self.players))

    def remove_player(self, connection):
        if connection in self.players:
            del self.players[connection]

        print("Players connected", len(self.players))

    def tick(self):
        data = {
            'type': 'tick',
            'players': [],
        }

        for connection in self.players.keys():
            connection.sendMessage(json.dumps(data).encode('utf8'))
