import math,os

sudoku = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

def matrix(matrix):
    for i in matrix:
        print(i)

def isValid():
    global sudoku
    valid = True
    for x in range(9):
        for y in range(9):

            for a in range(9):
                if a != y and sudoku[x][a] == sudoku[x][y] and sudoku[x][y] != 0:
                    valid = False

            for b in range(9):
                if b != x and sudoku[b][y] == sudoku[x][y] and sudoku[x][y] != 0:
                    valid = False

    return valid

def fix(a,b):
    while(True):
        if b-1 <0:
                b = 8
                a -= 1
        if a-1 <0:
            break
        b-=1
        if changable[a][b] is True:
            sudoku[a][b] += 1
            if sudoku[a][b] > 9:
                sudoku[a][b] = 0
                fix(a,b)
            break

changable = []
for x in sudoku:
    changable_row = []
    for y in x:
        if y == 0:
            changable_row.append(True)
        else:
            changable_row.append(False)
    changable.append(changable_row)

x=0
while(x<=8):
    y=0
    while(y<=8):
        if (x == 1 and y == 7):
            print("skibidi")
        if changable[x][y] is True:
            sudoku[x][y] += 1
        while(isValid() is False):
            sudoku[x][y] += 1
            if sudoku[x][y] > 9:
                sudoku[x][y] = 0
                fix(x,y)
                y-=1
        y+=1
        os.system("clear")
        matrix(sudoku)

    x+=1