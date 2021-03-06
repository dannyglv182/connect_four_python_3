
# list of lists representing slots on a 4*4 gameboard
board = [[1, 1], [1, 2], [1, 3], [1, 4],
         [2, 1], [2, 2], [2, 3], [2, 4],
         [3, 1], [3, 2], [3, 3], [3, 4],
         [4, 1], [4, 2], [4, 3], [4, 4]]

# bottom row is legal at first
legal = [[1, 1], [1, 2], [1, 3], [1, 4]]

# list to keep track of moves played
moves_played = []
cpu_moves_played = []

# combination of possible wins for player1 and the cpu
wins = {"x_row_1": [[1, 1], [1, 2], [1, 3], [1, 4]],
        "x_row_2": [[2, 1], [2, 2], [2, 3], [2, 4]],
        "x_row_3": [[3, 1], [3, 2], [3, 3], [3, 4]],
        "x_row_4": [[4, 1], [4, 2], [4, 3], [4, 4]],
        "y_row_1": [[1, 1], [2, 1], [3, 1], [4, 1]],
        "y_row_2": [[1, 2], [2, 2], [3, 2], [4, 2]],
        "y_row_3": [[1, 3], [2, 3], [3, 3], [4, 3]],
        "y_row_4": [[1, 4], [2, 4], [3, 4], [4, 4]],
        "diag_1": [[1, 1], [2, 2], [3, 3], [4, 4]],
        "diag_2": [[4, 1], [3, 2], [2, 3], [1, 4]]
        }

computer_wins = {"x_row_1": [[1, 1], [1, 2], [1, 3], [1, 4]],
                 "x_row_2": [[2, 1], [2, 2], [2, 3], [2, 4]],
                 "x_row_3": [[3, 1], [3, 2], [3, 3], [3, 4]],
                 "x_row_4": [[4, 1], [4, 2], [4, 3], [4, 4]],
                 "y_row_1": [[1, 1], [2, 1], [3, 1], [4, 1]],
                 "y_row_2": [[1, 2], [2, 2], [3, 2], [4, 2]],
                 "y_row_3": [[1, 3], [2, 3], [3, 3], [4, 3]],
                 "y_row_4": [[1, 4], [2, 4], [3, 4], [4, 4]],
                 "diag_1": [[1, 1], [2, 2], [3, 3], [4, 4]],
                 "diag_2": [[4, 1], [3, 2], [2, 3], [1, 4]]
                 }
