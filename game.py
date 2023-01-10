from human import Human
from ai import Ai
from time import sleep
class Game:
    def __init__(self):
        self.player_one = Human ()

    def run_game (self):
        self.welcome ()
        self.how_many_players
        
   
    def welcome (self):
        rules = ["Welcome to Rock, Paper, Scissors, Lizard, Spock.\n",  "A new take on an old game \n", "In this version of Rock, Paper, Scissors:\n", "Rock crushes Scissors \n", "Scissors cuts Paper\n", "Paper covers Rock \n", "Rock crushes Lizard \n", "Lizard poisons Spock \n", "Spock smashes Scissors \n", "Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock \n", "Spock vaporizes Rock"]
        for item in rules:
            print (item)
            sleep (1)
        play = input ("Would you like to play? yes or no")
        if play == "yes":
            print ("Great!  Lets begin!")
        elif play == "no":
            print ("I see you are no fun!  Goodbye")


    def how_many_players (self):
        self.number_of_players = input ("How many players will be playing the game? Enter 1, 2, or 3")
        if self.number_of_players == 1:
            self.ai_player = Ai ()
        elif self.number_of_players == 2:
            self.player_two = Human ()
        elif self.number_of_players == 3:
            self.player_three = Human ()
    
    def play_phase (self):
        while self.ai_player.number_of_wins < 2 and self.player_one.number_of_wins <2 and self.player_two.number_of_wins < 2 and self.player_three.number_of_wins < 2:
            if self.player_one.player_choice == "Rock"

    def win (self):
        pass