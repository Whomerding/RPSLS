class Player:
    def __init__(self):
        self.choice_options= ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.number_of_wins = 0
        self.name = ""
        self.choice = ""
    def make_a_choice (self, name):
        self.name = name
        self.choice = input (f"{self.name} choose: Rock, Paper, Scissors, Lizard, or Spock by typing your input below.\n")
        return (self.choice)
    

        
