""" Connect four game between a player and the cpu. Moves are played as tuples
    representing slots
    Author: Daniel Galvez
"""

import random
from lists import *


def player_move(move, player):
    """ If move is illegal, move is rejected. If move is legal, move is played
        and the slot above the move becomes legal
        move_index: the list position of the player move
        legal_spot: the newly legal position based on move_index

        Args:
            move: the slot [row,col] the player decides to play
            player: 'player_1' for player, 'cpu' for computer

    """
    if move not in legal:
        print ("sorry try again, move not allowed")
        return False
    else:
        # the [row, col] slot is compared to each item in the board until
        # there is a match
        # The move index is set to the move that was played
        move_index = -1
        for item in board:
            move_index += 1
            if item == move:
                break

        # adds the newly legal position to the list of legal moves
        # based on the move_index value
        if move[0] != 4:
            legal_spot = move_index + 4
            if board[legal_spot] not in legal:
                legal.append(board[legal_spot])

        # remove played move from legal list so it can't be played twice.
        list_pos = -1
        for i in legal:
            list_pos += 1
            if i == move:
                legal.pop(list_pos)
        return True


def remove_from_win_lists(move, player):
    """ The game is over when any of the lists of possible wins in the wins or 
        computer_wins dictionaries are empty. Every time a move is played, that
        move is popped from the lists where it is present.

        Args:
            move: the slot (list_item) played by the user
            player: the player making the move. Either 'player 1' or 'cpu'
    """
    # removes move from wins dictionary. Once one of the win
    # lists is empty, player has won.
    if player == "player_1":
        for key, value in wins.items():
            for x in value:
                if x == move:
                    value.remove(x)
    else:
        for key, value in computer_wins.items():
            for x in value:
                if x == move:
                    value.remove(x)        
    return


def get_move(row, col):
    """ Takes a row and col value for player_1 and returns it as a an array in
        the form [row, col]
    """

    # Check that row and col are numeric values
    try:
        row = int(row)
        col = int(col)
    except:
        raise ValueError("Values must be numeric.")

    # Outside of upper bound
    if row > 4 or col > 4:
        return False

    # Outside of lower bound
    if row < 1 or col < 1:
        return False

    return [row, col]


def generate_cpu_move():
    """ generates a random move to be played by the cpu
    """
    spots = len(legal)
    cpu_move = random.randint(0, spots-1)
    return legal[cpu_move]


def return_game_board():
    """ Creates a visual of the gameboard using a list of lists.
        Each list represents a row on the gameboard.
    """
    visual = [[[1, 1], [1, 2], [1, 3], [1, 4]],
             [[2, 1], [2, 2], [2, 3], [2, 4]],
             [[3, 1], [3, 2], [3, 3], [3, 4]],
             [[4, 1], [4, 2], [4, 3], [4, 4]]]

    
    # Sets the player's moves as x and the cpu's moves as o
    for row in visual:
        list_pos = -1
        for i in row:
            list_pos +=1
            if i in moves_played:
                row[list_pos] = " x  "
            elif i in cpu_moves_played:
                row[list_pos] = " o  "

    # Prints the board to the shell
    print (visual[3])
    print (visual[2])
    print (visual[1])
    print (visual[0])


def run_game():
    """ Runs the game
    """
    game_is_over = False
    return_game_board()
    while game_is_over == False:


        # Player move
        # Obtain the move from the command line as a string and pass row and col
        # to the get_move function
        player_1_move = input("\nWhat move would you like to play? FORMAT: ROW,COL\n")
        move = get_move(player_1_move[0], player_1_move[2])

        if player_move(move, "player_1"):
            remove_from_win_lists(move, "player_1")
            moves_played.append(move)
        else:
            pass


        # cpu move
        cpu_move = generate_cpu_move()
        print ("cpu plays" + str(cpu_move))
        player_move(cpu_move, "cpu")
        remove_from_win_lists(cpu_move, "cpu")
        cpu_moves_played.append(cpu_move)


        # Check for a win/loss/draw
        # Moves are popped from the wins list. A win occurs when a list
        # in the wins or computer_wins list becomes empty

        if legal == []:
            print ("Draw")
            game_is_over = True
            break


        for key in wins:
            if wins[key] == []:
                print ("You won!")
                game_is_over = True
                break


        for key in computer_wins:
            if computer_wins[key] == []:
                print ("Sorry you lost.")
                game_is_over = True
                break

        return_game_board()
run_game()
