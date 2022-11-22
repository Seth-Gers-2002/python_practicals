from musician import Musician

class Band(Musician):

    def __init__(self, name ,Band=""):
        super().__init__(self, name )
        self.PlayerName = PlayerName

    def __str__(self):
        return f"{self.PlayerName}"

    def add(self, name):
        self.PlayerName.append(name)

