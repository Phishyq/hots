class World:

    def __init__(self):
        super().__init__()
        self.items = []
        self.tiles = None

    def load(self, fname):
        with open(fname, 'r') as f:
            self.tiles = [[int(i) for i in line if i != '\n'] for line in f]

    def serialise(self):
        return {'world': self.tiles}