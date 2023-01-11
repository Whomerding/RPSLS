from human import Human
from ai import Ai
from time import sleep
class Game:
    def __init__(self):
        self.player_one = Human ()

    def run_game (self):
        self.welcome ()
        self.how_many_players ()
        
   
    def welcome (self):
        rules = [f"Welcome to Rock, Paper, Scissors, Lizard, Spock.\n",  "A new take on an old game \n", "In this version of Rock, Paper, Scissors:\n", "Rock crushes Scissors \n", "Scissors cuts Paper\n", "Paper covers Rock \n", "Rock crushes Lizard \n", "Lizard poisons Spock \n", "Spock smashes Scissors \n", "Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock \n", "Spock vaporizes Rock"]
        for item in rules:
            print (item)
            sleep (1)
        play = input ("Would you like to play? yes or no")
        if play == "yes":
            print ("Great!  Lets begin!")
            self.player_one.create_name ()
        elif play == "no":
            print ("I see you are no fun!  Goodbye")


    def how_many_players (self):
        self.number_of_players = input ("How many players will be playing the game? Enter 1 or 2")
        if self.number_of_players == "1":
            self.ai_player = Ai ()
        elif self.number_of_players == "2":
            self.player_two = Human ()
            print ("Welcome new player!")
            self.player_one.create_name ()

    """def play_phase (self):
        while self.ai_player.number_of_wins < 2 and self.player_one.number_of_wins <2 and self.player_two.number_of_wins < 2:

            self.player_one_choice = self.player_one.make_a_choice ()
            if self.number_of_players == "1":
                 self.ai_choice = self.ai_player.make_a_choice ()
            elif self.number_of_players == "2":
                self.player_two_choice = self.player_two.make_a_choice ()
           if self.player_one_choice == "Rock": 
                          
    def win (self):
        pass

    def eval_round (self):
        if self.player_choice == "Rock":
            if self.ai_player == "Scissor" or self.ai_player == "Lizard": 
                if self.otherplayer1 == "Scissor" or self.otherplayer1 == "Lizard":
                    if self.otherplayer2 =="Scissor" or self.otherplayer2 == "Lizard":
                        print ("Player One Wins this Round!!")
                        self.player_one.number_of_wins += 1
        if self.player_choice == ""
        """