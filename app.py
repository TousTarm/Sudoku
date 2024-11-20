import math,os,time
from colorama import Fore, Style

sudoku = [
        [6,5,0,0,0,7,2,0,0],
        [0,1,0,3,9,6,4,5,0],
        [0,8,0,0,5,1,0,3,6],
        [0,9,0,6,0,3,8,2,7],
        [1,0,0,0,0,0,6,9,0],
        [0,0,0,0,0,9,0,4,0],
        [7,4,0,0,0,0,0,0,0],
        [0,0,9,0,0,5,1,8,4],
        [5,0,8,0,4,0,0,0,3]
        ]


def matrix(matrix):
    os.system("clear")
    for x,row in enumerate(matrix):
        for y,number in enumerate(row):
            if changable[x][y] == False:
                print(" " + str(number) + " ", end="")
            elif changable[x][y] == True and number != 0:
                if(number == 10):
                    print("   ", end="")
                else:
                    print(Fore.BLUE + " " + str(number) + " " + Style.RESET_ALL, end="")
            else:
                print("   ", end="")
        print()
    time.sleep(0.07)



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
            
            for m in range(3):
                for n in range(3):
                    c = math.ceil((x)/3 -1) * 3
                    d = math.ceil((y)/3 -1) * 3
                    for p in range(3):
                        for r in range(3):
                            if(sudoku[c+m][d+n] == sudoku[c+p][d+r] and m!=p and p!=d and sudoku[c+m][d+n] != 0):
                                valid = False
                    
    return valid

    
  
def fix(x,y):
    while(True):
        y-=1
        if y <0:
                y = 8
                x -= 1
        if x-1 <0:
            break
        if changable[x][y] is True:
            sudoku[x][y] += 1
            if sudoku[x][y] > 9:
                sudoku[x][y] = 0
                matrix(sudoku)
                fix(x,y)
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
        if changable[x][y] is True:
            sudoku[x][y] += 1
        while(isValid() is False):
            if changable[x][y] is True:
                sudoku[x][y] += 1
                matrix(sudoku)
                if sudoku[x][y] > 9:
                    sudoku[x][y] = 0
                    fix(x,y)
                    while(sudoku[x][y] == 0):
                        y-=1
                        if(y<0):
                            y = 8
                            x-=1
                        if(x<0):
                            break
            else:
                y-=1
                if(y<0):
                    y = 8
                    x-=1
                if(x<0):
                    break
           
        y+=1
        matrix(sudoku)
    x+=1