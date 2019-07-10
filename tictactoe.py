#This is program for tic tack toe 
tictactoe = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
def printtictactoe():
    print("1:", tictactoe[1], "    2:", tictactoe[2], "    3:", tictactoe[3])
    print()
    print("4:", tictactoe[4], "    5:", tictactoe[5], "    6:", tictactoe[6])    
    print()
    print("7: ", tictactoe[7], "    8:", tictactoe[8], "    9:", tictactoe[9])
def checkforwin():
    if ((tictactoe[1] == 'X' and tictactoe[2] == 'X' and tictactoe[3] == 'X')
        or(tictactoe[1] == 'X' and tictactoe[4] == 'X' and tictactoe[7] == 'X')
        or (tictactoe[4] == 'X' and tictactoe[5] == 'X' and tictactoe[6] == 'X')
        or (tictactoe[7] == 'X' and tictactoe[8] == 'X' and tictactoe[9] == 'X')
        or (tictactoe[2] == 'X' and tictactoe[5] == 'X' and tictactoe[8] == 'X')
        or (tictactoe[3] == 'X' and tictactoe[6] == 'X' and tictactoe[9] == 'X')
        or (tictactoe[1] == 'X' and tictactoe[5] == 'X' and tictactoe[9] == 'X')
        or (tictactoe[3] == 'X' and tictactoe[5] == 'X' and tictactoe[7] == 'X')):
        return('X')       
    elif ((tictactoe[1] == 'O' and tictactoe[2] == 'O' and tictactoe[3] == 'O')
        or(tictactoe[1] == 'O' and tictactoe[4] == 'O' and tictactoe[7] == 'O')
        or (tictactoe[4] == 'O' and tictactoe[5] == 'O' and tictactoe[6] == 'O')
        or (tictactoe[7] == 'O' and tictactoe[8] == 'O' and tictactoe[9] == 'O')
        or (tictactoe[2] == 'O' and tictactoe[5] == 'O' and tictactoe[8] == 'O')
        or (tictactoe[3] == 'O' and tictactoe[6] == 'O' and tictactoe[9] == 'O')
        or (tictactoe[1] == 'O' and tictactoe[5] == 'O' and tictactoe[9] == 'O')
        or (tictactoe[3] == 'O' and tictactoe[5] == 'O' and tictactoe[7] == 'O')):
        return('O')
temp = ''
while(True):
    printtictactoe()
    print("pick a number between 1 and 9")
    numberpicked = int(input())
    if tictactoe[numberpicked] != "":
        print("enter a different number")
        numberpicked = int(input())
    if tictactoe[numberpicked] == "":
        if temp == '' or temp == 'O':
            tictactoe[numberpicked] = 'X'
            temp = 'X'
        else:
            tictactoe[numberpicked] = 'O'
            temp = 'O'
        if checkforwin() == 'X':
            print("X wons the game")
            break
        elif checkforwin() == 'O':
            print("O wons the game")
            break
printtictactoe()

