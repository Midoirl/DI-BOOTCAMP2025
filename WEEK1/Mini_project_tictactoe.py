#Making tic tac toe 
#Step 1: Represnting the game board 3x3 grid
game_board = [[" ", " ", " "], #Initially each cell in the grid is empty
              [" ", " ", " "],
              [" ", " ", " "]
              ]

#Step 2:Create a function that prints the current the state of the game board
#We display the board like how we usually draw it on papers
def display_board(board): 
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")  
    print("--|---|--")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("--|---|--")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

#Step 3: Getting player input
#Create a function to get player 1 move and update it to the board
def player_input_player1(player1):
    while True:
        print("Player 1 : Your turn now (X)")
        row = int(input("Enter row number: ")) #Store the row number in a variable
        col = int(input("Enter column number: ")) #Store the column number in a variable
         #Validate the input to ensure its within the valid range and that the chosen cell is empty
        #Case 1, row and cols are within range and the cell is empty
        if (1 <= row <= 3) and (1 <= col <= 3) and game_board[row-1][col-1] == " ":
        # add the X to the game_board in that specific cell
            (game_board[row-1][col-1]) = "X" # -1 is used so that user starts counting from 1 (Like any non programmer person would Lmao )
            break #break the loop
        #Case 2, row and cols are within range but the cell is not empty
        elif (1 <= row <= 3) and (1 <= col <= 3) and game_board != " ":
            print("That cell is already taken, Please choose another spot.")
            continue #restart the loop
        #Case 3, row and cols are not within range
        else:
            print("That is outside the row and column number range, Please enter a valid row and column number.")
            continue #restart the loop
#Create a function to get player 2 move and update it to the board
def player_input_player2(player2):
    while True:
        print("Player 2 : Your turn now (O)")
        row = int(input("Enter row number: ")) #Store the row number in a variable
        col = int(input("Enter column number: ")) #Store the column number in a variable
        print("")
         #Validate the input to ensure its within the valid range and that the chosen cell is empty
        #Case 1, row and cols are within range and the cell is empty
        if (1 <= row <= 3) and (1 <= col <= 3) and game_board[row-1][col-1] == " ":
        # add the O to the game_board in the specific cell
            (game_board[row-1][col-1]) = "O" # -1 is used so that user starts counting from 1 (Like any non programmer person would Lmao )
            break #break the loop
        #Case 2, row and cols are within range but the cell is not empty
        elif (1 <= row <= 3) and (1 <= col <= 3) and game_board[row-1][col-1] != " ":
            print("That cell is already taken, Please choose another spot.")
            continue #Restart the loop
        #Case 3, row and cols are not within range
        else:
            print("That is outside the row or column number range, Please enter a valid row and column number.")
            continue #Restart the loop
        
#Step 3: Checking for a winner 
#Create a function that checks for the winner
def check_win(board,symbol):
    #Iterate through each row in the board and check the symbol 
    for row in board:
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True #if the whole row has the symbol it returns true
    #Iterate through each column in the board and check the symbol
    for col_index in range(3):
         if board[0][col_index] == symbol and board[1][col_index] == symbol and board[2][col_index] == symbol:
            return True #if the whole column has the symbol it returns true
    #Check the diagonal conditions , only two cases
    if (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or (board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol):
        return True #if the either of the two diagonals have the symbol

#Step 4: Checking for a tie
#function should check if all the positions of the board are full without a winner
def check_if_tie():
    for row in game_board:
        for cell in row:
            if cell == " ":
                return False
    if (not check_win(game_board,"X")) and (not check_win(game_board,"O")):
                return True
    
 #Main game loop function
def play():
    while True:
            display_board(game_board) #Show the most recently updated board 
            player_input_player1(game_board) #Put the "X" as input from player1 on the board
            display_board(game_board)
            if check_win(game_board,"X"):
                print("Player 1 (X) Has won!") #If Player 1 (X) wins , print that he has won and break the main game loop 
                break 
            elif check_if_tie():
                print("It's a tie!")
                break
            else:
        
                player_input_player2(game_board) #Put the "O" as input from player2 on the board
                if check_win(game_board,"O"): #If player 2 (O) wins, print that he has won and break the main game loop
                    display_board(game_board)
                    print("Player 2 (O) Has won! ")
                    break
                elif check_if_tie(): #if its a tie, print its a tie and break the main game loop
                    print("It's a tie!")
                    break
                
#Call play()
play()
        
    


    




    





