from player import Player
import random
class Ai (Player):
    def __init__(self):
        super().__init__()
        self.name = "AI"
        
    def make_a_choice (self):
        self.player_choice = random.choice (self.choice_options)
        return (self.player_choice)