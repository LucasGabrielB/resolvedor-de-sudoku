class SudokuBoard:
    def __init__(self, board):
        self.board = board


    def solve(self):
        ''' Automatically solves the board. '''
        
        # find an empty position
        position = self.find_empty()
        
        # if it doesn't find a position it returns true
        if not position:
            return True

        # otherwise, take that position
        else:
            row, column = position

        # tries to solve the board, using recursion
        for i in range(1,10):
            
            # check if the number can be placed in that position
            if self.is_valid(i, row, column):
                # put the number in that position
                self.board[row][column] = i

                # calls the function recursively
                if self.solve():
                    return True

                # If the number cannot be placed there, 
                # it will come back and remove the number
                self.board[row][column] = 0

        return False


    def is_valid(self, num, row, column):
        ''' Check if a number can be placed in a certain position.
        
        Returns:
            boolean: True if number can be placed otherwise False.
        '''

        # check the row for incompatibilities
        for i in range(9):
            if self.board[row][i] == num and column != i:
                return False

        # check the column for incompatibilities
        for i in range(9):
            if self.board[i][column] == num and row != i:
                return False

        # check the box for for incompatibilities
        box_x_position = column // 3
        box_y_position = row // 3

        for x in range(box_y_position*3, box_y_position*3 + 3):
            for y in range(box_x_position * 3, box_x_position*3 + 3):
                if self.board[x][y] == num and (x,y) != (column, row):
                    return False

        return True


    def print_board(self):
        ''' Print the board in the terminal. '''

        for row in range(9):
            if row % 3 == 0 and row != 0:
                print("-------+--------+------")

            for column in range(9):
                if column % 3 == 0 and column != 0:
                    print(" | ", end="")

                if column == 8:
                    print(self.board[row][column])
                else:
                    print(str(self.board[row][column]) + " ", end="")


    def find_empty(self):
        ''' Find an empty position in the board. 

            Returns:
                tuple (int, int): row and column of the empty position.
                None: if there are no empty positions.
        '''

        # searches for and returns the first empty position it finds
        for row in range(9):
            for column in range(9):
                if self.board[row][column] == 0:
                    return (row, column)

        return None

# example
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_board = SudokuBoard(board)
sudoku_board.solve()
sudoku_board.print_board()
