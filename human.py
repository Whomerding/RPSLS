from player import Player

class Human (Player):
    def __init__(self):
        super ().__init__()
        self.name: "Player"
    
    def create_name (self):
        self.name = input("What is your name?")
        