#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        #To center the top heading numbers on each columns
        column_head = "   " + "   ".join(f"{i:^{self.size}}" for i in range(len(self.board[0])))
        print(column_head)
        
        #display and center the rows
        for row_id, row_values in enumerate(self.board):
            display_row = " | ".join( ' ' if row_value == 0 else f"{row_value:^{self.size}}" for row_value in row_values)

            #display each values in each row 
            print(f'{row_id} {display_row}')

            #space  each row after placing the values in each rows
            if row_id < len(self.board) -1:
                print("  "+ "----------------") 
        
       



    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        
        # Check if the square at the given row and column is 0 (empty) 
        #if the values of the column out of range, it asks user for a new nummber
        try: 
            if self.board[row][col] == 0:
                #print(True)
                return True
                
            elif self.board[row][col] != 0:
                #print(False)
                return False
        except IndexError:
            print("Row or Coloumn number out of range, please try values between 0,1,2 ")

        
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''

        if self.squareIsEmpty(row, col) == True:
            self.board[row][col] = num  # Update the board if the square is empty
            print(f"\nUpdated board at position ({row}, {col}) with {num}")
            self.drawBoard()  # Show the updated board
            return True
        else:
            print(f"\nFailed to update board at position ({row}, {col}), square not empty.")
            return False


    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        #check for any empty box in the each rows
        for row in self.board:
            for each_square in row:
                if each_square == 0: 
                    print('Board is not full')
                    return False  # Exit early and return False if any empty square is found
        
        # If the loop completes without finding any empty square
        # Then the board is full
        print('Board is full')
        return True



        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # Check all rows (horizontal lines)
        for row in self.board:
            if sum(row) == 15:
                print(True)
                return True

        # Check all columns (vertical lines)
        for col in range(self.size):  # Loop over each column index
            column_sum = 0  # Start the sum for this column
            for row in range(self.size):  # Loop over each row for the current column
                column_sum += self.board[row][col]  # Add the value at this row and column to the sum
        
            #After calculating the sum for this column, check if it equals 15
            if column_sum == 15:
                print(True)
                return True
            
        #Check diagonal from top-left to bottom-right
        diagonal1_sum = 0
        for i in range(self.size):
            diagonal1_sum += self.board[i][i]
        if diagonal1_sum == 15:
            print(True)
            return True

        #Check diagonal from top-right to bottom-left
        diagonal2_sum = 0
        for i in range(self.size):
            diagonal2_sum += self.board[i][self.size - 1 - i]
        if diagonal2_sum == 15:
            print(True)
            return True

        # After all condtions has been checked
        # no winning condition is met, return False
        print('\nNo winning condition is met')
        return False
            
            
              
        
     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    myBoard.update(0,0,3)
    myBoard.update(1,1,7)
    myBoard.update(2,2,5)
    myBoard.drawBoard()


    # try to assign a number to a non-empty square. What happens?
    
    # check if the board has a winner. Should there be a winner after only 1 entry?
    
    # check if the board is full. Should it be full after only 1 entry?
    myBoard.squareIsEmpty(2,1)
    
    # add values to the board so that any line adds up to 15. Display
    
    # check if the board has a winner
    myBoard.isWinner()
    
    # check if the board is full
    myBoard.boardFull()
    
    # write additional tests, as needed
    

