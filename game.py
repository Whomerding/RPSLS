from human import Human
from ai import Ai
from time import sleep
import validate
import sys

class Game:
    def __init__(self):
        self.player_one = Human ()

    def run_game (self):
        self.welcome ()
        self.how_many_players ()
        self.play_phase ()
        self.win ()
        self.play_again ()
        
   
    def welcome (self):
        rules = [f"Welcome to Rock, Paper, Scissors, Lizard, Spock.\n",  "A new take on an old game \n", "In this version of Rock, Paper, Scissors:\n", "Rock crushes Scissors \n", "Scissors cuts Paper\n", "Paper covers Rock \n", "Rock crushes Lizard \n", "Lizard poisons Spock \n", "Spock smashes Scissors \n", "Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock \n", "Spock vaporizes Rock\n", "Best two out of three win\n"]
        for item in rules:
            print (item)
            sleep (.50)
        play = input ("Would you like to play? Yes or no? \n")
        play = validate.valid_input_yes_no (play)
        if play == "yes":
            print ("Great!  Lets begin!")
            self.player_one.create_name ()
        elif play == "no":
            print ("I see you are no fun!  Goodbye")
            sys.exit ()
          

    def how_many_players (self):
        self.number_of_players = input ("How many players will be playing the game? Enter 1 or 2")
        self.number_of_players = validate.valid_input_num_players (self.number_of_players)
        if self.number_of_players == "1":
            self.ai_player = Ai ()
        elif self.number_of_players == "2":
            self.player_two = Human ()
            print ("Welcome new player!")
            self.player_two.create_name ()

    def play_phase (self):
        self.has_won = ""
        self.player_one_choice = ""
        if self.number_of_players == "1":
            while self.ai_player.number_of_wins < 2 and self.player_one.number_of_wins <2:
                self.player_one.choice = self.player_one.make_a_choice (self.player_one.name)
                self.player_one.choice = validate.valid_input_choice (self.player_one.choice)
                print (f"\n{self.player_one.name} chose {self.player_one.choice}.")
                self.ai_player.choice = self.ai_player.make_a_choice ()
                self.ai_player.choice = validate.valid_input_choice (self.ai_player.choice)
                print (f"AI chose {self.ai_player.choice}.\n ")
                self.has_won = validate.eval_winner (self.player_one.choice, self.ai_player.choice, "")
                if self.has_won == "this player":
                    print (f"Congratulations {self.player_one.name}!  You win the round!\n")
                    self.player_one.number_of_wins += 1
                elif self.has_won == "tie":
                    print ("It's a tie!  No one wins!\n")
                else:
                    print ("The AI has bested you!  The AI wins the round!\n")
                    self.ai_player.number_of_wins += 1
                print (f"{self.player_one.name} has won {self.player_one.number_of_wins} rounds.\nThe computer has won {self.ai_player.number_of_wins} rounds!\n")

        elif self.number_of_players == "2":
             while self.player_one.number_of_wins <2 and self.player_two.number_of_wins < 2:
                self.player_one.choice = self.player_one.make_a_choice (self.player_one.name)
                self.player_one.choice = validate.valid_input_choice (self.player_one.choice)
                self.player_two.choice = self.player_two.make_a_choice (self.player_two.name)
                self.player_two.choice = validate.valid_input_choice (self.player_two.choice)
                print (f"\n{self.player_one.name} chose {self.player_one.choice}.\n")
                print (f"{self.player_two.name} chose {self.player_two.choice}. \n")
                self.has_won = validate.eval_winner (self.player_one.choice, self.player_two.choice, "")
                if self.has_won == "this player":
                    print (f"Congratulations {self.player_one.name}!  You win the round\n")
                    self.player_one.number_of_wins += 1
                elif self.has_won == "tie":
                    print ("It's a tie!  No one wins!\n")
                else:
                    print (f"Congrats! {self.player_two.name}.  You win!\n")
                    self.player_two.number_of_wins += 1
                print (f"{self.player_one.name} has won {self.player_one.number_of_wins} rounds.\n{self.player_two.name} has won {self.player_two.number_of_wins} rounds!\n")
                          
    def win (self):
        if self.number_of_players == "1":
            if self.player_one.number_of_wins == 2:
                print (f"{self.player_one.name} has won two out of three rounds!!  {self.player_one.name} is the champion!!\n")
            else:
                print (f"The AI has has won two out of three rounds proving that computers are better than people!  You lose the AI wins!\n")
        if self.number_of_players == "2":
            if self.player_one.number_of_wins == 2:
                print (f"{self.player_one.name} is victorious in two out of three rounds!!  Congratulations!!  Too bad, so sad {self.player_two.name}\n")
            else:
                print (f"{self.player_two.name} is victorious in two out of three rounds!!  Congratulations!!  Too bad, so sad {self.player_one.name}\n")
    
    def play_again (self):
        self.play_again = True
        while self.play_again == True:
            self.play_again_input = input ("Would you like to play again? yes or no?\n")
            self.play_again_input = validate.valid_input_yes_no (self.play_again_input)
            if self.play_again_input == "yes":
                self.play_again = True
                self.player_one.number_of_wins = 0
                if self.number_of_players == "1":
                    self.ai_player.number_of_wins = 0
                else:
                    self.player_two.number_of_wins = 0  
                self.play_phase ()
                self.win ()
                  
            else:
                print("Goodbye")
                self.play_again = False




  