
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

def valid_input_num_players (int, bool):
    input = int
    while bool == False:
    if int == 1 or int == 2:
        bool = True
        input = int
    else:
        input = input ("That is not a valid input.  Please only enter 1 or 2 below \n") 
        bool = False
        return (input)