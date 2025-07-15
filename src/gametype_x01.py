from game import Game
from player import Player


class GameType_x01(Game):
    def __init__(self, player_one = "P1", player_two = "P2", starting_score = 501, double_in = False, double_out = True):
        super().__init__(player_one, player_two)
        self._highest_throw = None
        self._highest_throw_value = 0
        self.double_in = double_in
        self.double_out = double_out
        self.starting_score = starting_score        
        self.player1 = Player("Boerke", self.starting_score)
        self.player2 = Player("TankTheTech", self.starting_score)

    def record_throw(self, player, throw_score, multiplier):
            player_score = getattr(player, "player_score")
            if self.double_in and not getattr(player, "is_in"):
                if self.multiplier == 2:
                    # The player threw a double, start counting down from the player_score (which should still be the starting_score)
                    setattr(player,"player_score", player_score - (multiplier * throw_score))
                    setattr(player, "is_in", True)
                else:
                     pass # No score
            else:
                # player is either in, or double_in is False
                setattr(player,"player_score", player_score - (multiplier * throw_score))


                
                

    