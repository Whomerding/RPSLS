from human import Human
from ai import Ai
from time import sleep
import validate

class Game:
    def __init__(self):
        self.player_one = Human ()

    def run_game (self):
        self.welcome ()
        self.how_many_players ()
        self.play_phase ()
        self.win ()
        
   
    def welcome (self):
        rules = [f"Welcome to Rock, Paper, Scissors, Lizard, Spock.\n",  "A new take on an old game \n", "In this version of Rock, Paper, Scissors:\n", "Rock crushes Scissors \n", "Scissors cuts Paper\n", "Paper covers Rock \n", "Rock crushes Lizard \n", "Lizard poisons Spock \n", "Spock smashes Scissors \n", "Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock \n", "Spock vaporizes Rock"]
        for item in rules:
            print (item)
            sleep (.25)
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

    def play_phase (self):
        self.has_won = ""
        self.player_one_choice = ""
        if self.number_of_players == "1":
            while self.ai_player.number_of_wins < 2 and self.player_one.number_of_wins <2:
                self.player_one.choice = self.player_one.make_a_choice ()
                print (f"{self.player_one.name} chose {self.player_one.choice}.")
                self.ai_player.choice = self.ai_player.make_a_choice ()
                print (f"AI chose {self.ai_player.choice}. ")
                self.has_won = validate.eval_winner (self.player_one.choice, self.ai_player.choice, "")
                if self.has_won == "this player":
                    print (f"Congratulations {self.player_one.name}!  You win the round!")
                    self.player_one.number_of_wins += 1
                elif self.has_won == "tie":
                    print ("It's a tie!  No one wins!")
                else:
                    print ("The AI has bested you!  The AI wins the round!")
                    self.ai_player.number_of_wins += 1
        elif self.number_of_players == "2":
             while self.player_one.number_of_wins <2 and self.player_two.number_of_wins < 2:
                self.player_one.choice = self.player_one.make_a_choice ()
                print (f"{self.player_one.name} chose {self.player_one.choice}.")
                self.player_two.choice = self.player_two.make_a_choice ()
                print (f"{self.player_two.name} chose {self.player_two.choice}. ")
                self.has_won = validate.eval_winner (self.player_one.choice, self.player_two.choice, "")
                if self.has_won == "this player":
                    print (f"Congratulations {self.player_one.name}!  You win the round")
                    self.player_one.number_of_wins += 1
                elif self.has_won == "tie":
                    print ("It's a tie!  No one wins!")
                else:
                    print (f"Congrats! {self.player_two.name}.  You win!")
                    self.player_two.number_of_wins += 1
                    print (f"{self.player_one.name} has won {self.player_one.number_of_wins} rounds. \n {self.player_two.name} has won {self.player_two.number_of_wins} rounds!")
                          
    def win (self):
        print ("Declare winner here")

  