
def eval_winner (eval_player_choice, other_player_choice, winner):
    eval_player_choice = eval_player_choice
    other_player_choice = other_player_choice
    winner = winner
    
    if eval_player_choice == "Rock":
        if other_player_choice == "Scissors" or other_player_choice == "Lizard":
            winner = "this player"
        elif other_player_choice == "Rock":
            winner = "tie"
    elif eval_player_choice == "Paper":
        if other_player_choice == "Rock" or other_player_choice == "Spock":
            winner = "this player"
        elif other_player_choice == "Paper":
            winner = "tie"
    elif eval_player_choice == "Scissors":
        if other_player_choice == "Paper" or other_player_choice == "Lizard":
            winner = "this player"
        elif other_player_choice == "Scissors":
            winner = "tie"
    elif eval_player_choice == "Lizard":
        if other_player_choice == "Spock" or other_player_choice == "Paper":
            winner = "this player"
        elif other_player_choice == "Lizard":
            winner = "tie"
    elif eval_player_choice == "Spock":
        if other_player_choice == "Scissors" or other_player_choice == "Rock":
            winner = "this player"
        elif other_player_choice == "Spock":
            winner = "tie"
    else:
        winner = "not the winner"
    return (winner)


def valid_input_num_players (user_input):
    valid_response = False
    while valid_response != True:
        if user_input == "1" or user_input == "2":
            valid_response = True
        else:
            user_input = input ("That is not a valid input.  Please only enter 1 or 2 below: \n") 
            valid_response = False
    return (user_input)

def valid_input_choice (user_input):
    valid_response = False
    while valid_response != True:
        if user_input == "Rock" or user_input == "Paper" or user_input == "Scissors" or user_input == "Lizard" or user_input == "Spock":
            valid_response = True
        else:
            user_input = input ("That is not a valid input.  Please only enter Rock, Paper, Scissors, Lizard, Spock below: \n") 
            valid_response = False
    return (user_input)

def valid_input_yes_no (user_input):
    valid_response = False
    while valid_response != True:
        if user_input == "yes" or user_input == "no":
            valid_response = True
        else:
            user_input = input ("That is not a valid input.  Please only enter yes or no below: \n") 
            valid_response = False
    return (user_input)