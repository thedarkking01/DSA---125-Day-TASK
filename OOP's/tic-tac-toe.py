class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', 
                      ' ', ' ', ' ', 
                      ' ', ' ', ' ']
    
    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

class Player:
    def __init__(self, type):
        self.type = type
        self.name = self.get_name()
    
    # method to take players name input
    def get_name(self):
        if self.type == 'X':
            name = input('Player selecting X, enter your name: ')
        else:
            name = input('Player selecting O, enter your name: ')
        return name

# creating Player objects for testing
player1 = Player('X')
player2 = Player('O')