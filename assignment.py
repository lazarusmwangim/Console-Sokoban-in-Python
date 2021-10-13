"""
Name:
UPI:
Description:
"""


class Sokoban:
    """Your code here"""
    moves = 0
    boards = []
    adds = 0
    def __init__(self, board):
        #stach = board
        self.__base_map = board
        
        #print(Sokoban.boards)
    
    def brds(self):
        Sokoban.adds += 1
        stach = []
        stach.extend(self.__base_map)
        #print(stach)
        sdr=[]
        for list in stach:
            temp = []
            for item in list:
                temp.append(list[list.index(item)])
            #print(temp)
            sdr.append(temp)
        #print(sdr)
        Sokoban.boards.append(sdr)
    
    def find_player(self):
        brd=self.__base_map
        char = 'P'
        for row in brd:
            if char in row:
                return (brd.index(row), row.index(char))
        
    def complete(self):
        brd = self.__base_map
        char = 'o'
        self.brds()
        choice = any(char in list for list in brd)
        print(choice)
        if choice == True:
            return False
        return True
        
    def get_steps(self):
        
        return Sokoban.moves
    
    def restart(self):
        Sokoban.moves = 0
        Sokoban.adds = 0
        del Sokoban.boards[1:]
        #print(Sokoban.boards)
        #return
        crd=Sokoban.boards[0]
        del Sokoban.boards[0:]
        return main(crd)
    
    def undo(self):
        
        print(Sokoban.adds)
        print(Sokoban.moves)
        print(Sokoban.boards)
        
        goto = Sokoban.moves
        
        if goto > 0:
            theb = Sokoban.boards[goto-1]
            Sokoban.boards.pop(goto-1)
            print("HG")
            #Sokoban.boards.pop(Sokoban.adds-1)
            #print(theb)
            
            Sokoban.moves -= 1
            Sokoban.adds -= 2
            del Sokoban.boards[Sokoban.moves:]
        # elif goto == 0 and Sokoban.adds == 1:
        #     theb = Sokoban.boards[0]
        #     Sokoban.adds=0
        #     #Sokoban.boards.pop(1)
        else:
            print("JK")
            theb = Sokoban.boards[0]
            Sokoban.adds=0
            del Sokoban.boards[1:]
            
        
        print(Sokoban.adds)
        print(Sokoban.moves)
        print(Sokoban.boards)
        
        return main(theb)
    
    def move(self, direction):
        
        brd = self.__base_map
        a,b = self.find_player()
        row = a
        col = b
        if direction == 'w' and brd[row - 1][col] != '*':
            row -= 1
            
            if brd[row][col] == '#' and brd[row - 1][col] != '*' and brd[row - 1][col] != 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row - 1][col] = "#"
                Sokoban.moves += 1
            elif brd[row][col] == '#' and brd[row - 1][col] == 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row - 1][col] = " "
                Sokoban.moves += 1
            elif brd[row][col] != '#' and brd[row][col] != '*':
                brd[a][b] = " "
                brd[row][col] = "P"
                Sokoban.moves += 1
        elif direction == 's' and brd[row + 1][col] != '*':
            row += 1
            if brd[row][col] == '#' and brd[row + 1][col] != '*' and brd[row + 1][col] != 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row + 1][col] = "#"
                Sokoban.moves += 1
            elif brd[row][col] == '#' and brd[row + 1][col] == 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row + 1][col] = " "
                Sokoban.moves += 1
            elif brd[row][col] != '#' and brd[row][col] != '*':
                brd[a][b] = " "
                brd[row][col] = "P"
                Sokoban.moves += 1
        elif direction == 'a' and brd[row][col - 1] != '*':
            col -= 1
            if brd[row][col] == '#' and brd[row][col - 1] != '*' and brd[row][col - 1] != 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row][col - 1] = "#"
                Sokoban.moves += 1
            elif brd[row][col] == '#' and brd[row][col - 1] == 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row][col - 1] = " "
                Sokoban.moves += 1
            elif brd[row][col] != '#' and brd[row][col] != '*':
                brd[a][b] = " "
                brd[row][col] = "P"
                Sokoban.moves += 1
        elif direction == 'd' and brd[row][col + 1] != '*':
            col += 1
            if brd[row][col] == '#' and brd[row][col + 1] != '*' and brd[row][col + 1] != 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row][col + 1] = "#"
                Sokoban.moves += 1
            elif brd[row][col] == '#' and brd[row][col + 1] == 'o':
                brd[a][b] = " "
                brd[row][col] = "P"
                brd[row][col + 1] = " "
                Sokoban.moves += 1
            elif brd[row][col] != '#' and brd[row][col] != '*':
                brd[a][b] = " "
                brd[row][col] = "P"
                Sokoban.moves += 1
        #del Sokoban.boards[Sokoban.moves:]
        return main(brd)
    
    
    def __str__(self):
        output = ""
        for row in self.__base_map:
            for char in row:
                output += char + " "
            output += "\n"
        return output


def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')


# This is here for you to test your code. You will need to test your code
# yourself for this assignment. Remove any testing code (including the code
# provided below) when you submit this file.
#
# The only code in your submission should be:
#   - the Sokoban class
#   - the main function
#
# There should be no other code included in your submission.
test_board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
main(test_board)
