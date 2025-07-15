# This is the base game class, and only has those parameters shared by all derived classes.
# It does not actually contain any logic
class Game():
    def __init__(self, player_one="P1", player_two="P2"):
        self.player_one = player_one
        self.player_two = player_two
        pass