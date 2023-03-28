def createGrid():
    grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
    ]
    return grid

def nextTurn(grid, player):
    print("Player", player + "'s", "turn, select a position from 1 to 9." )
    print()
    print("-------------")
    print("|", grid[0][0], "|", grid[0][1], "|", grid[0][2], "|")
    print("-------------")
    print("|", grid[1][0], "|", grid[1][1], "|", grid[1][2], "|")
    print("-------------")
    print("|", grid[2][0], "|", grid[2][1], "|", grid[2][2], "|")
    print("-------------")
    print()

def pickSpot(grid, player, spot):
    if not spot.isnumeric():
        return False

    for row in grid:
        if spot in row:
            row[row.index(spot)] = player
            return True
    return False

def swapPlayer(player):
    if player == 'X':
        return 'O'
    if player == 'O':
        return 'X'
        
def checkWin(grid):
    def checkRow():
        for row in grid:
            if row[0] == row[1] and row[1] == row[2]:
                return row[0]

    def checkColumn():
        for i in range(3):
            column = [row[i] for row in grid]
            if column[0] == column[1] and column[1] == column[2]:
                return column[0]

    def checkDiagonal():
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            return grid[0][0]
        if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            return grid[0][2]
    
    if checkRow():
        return checkRow()
    elif checkColumn():
        return checkColumn()
    elif checkDiagonal():
        return checkDiagonal()
    else:
        return None

def tictactoe():
    grid = createGrid()
    player = 'X'
    winner = None

    while winner == None:
        player = swapPlayer(player)
        nextTurn(grid, player)
        spot = input("Input spot: ")

        if not pickSpot(grid, player, spot):
            print("Not a valid spot")
            continue
        
        winner = checkWin(grid)

    print("Winner is", winner)


tictactoe()