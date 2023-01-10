class Player:
    def __init__(self):
        self.choice_options= ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def make_a_choice (self):
        self.player_choice: input ("Choose: Rock, Paper, Scissors, Lizard, or Spock by typing your input below.\n")
        