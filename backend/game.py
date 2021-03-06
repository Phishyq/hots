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

        player = Player()
        self.players[connection] = player
        self.world.add_player(player)

        data = {
            'id': player.id,
        }

        data.update(**self.world.serialise_world())

        self.send(connection, data, 'world')
        print("Players connected", len(self.players))

    def remove_player(self, connection):
        if connection in self.players:
            player = self.players[connection]
            del self.players[connection]
            self.world.remove_player(player)

        print("Players connected", len(self.players))

    def tick(self):
        self.broadcast(self.world.serialise_state(), 'tick')

    def receive_message(self, connection, message):
        command = json.loads(message)
        if command['type'] == 'movement':
            self.world.move_player(
                self.players[connection],
                command['direction'],
                command['angle'],
            )

    # Utility Methods

    def broadcast(self, data, message_type):
        for connection in self.players.keys():
            self.send(connection, data, message_type)

    def send(self, connection, data, message_type):
        data.update(type=message_type)
        connection.sendMessage(json.dumps(data).encode('utf8'))
