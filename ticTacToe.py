

coordinates = {' ', ' ', ' '},{' ', ' ', ' '},{' ', ' ', ' '}

while P1CrossOrCircle != 'X' & P1CrossOrCircle != 'O':
    P1CrossOrCircle = input("P1 choose X or O?").upper()
if (P1CrossOrCircle == 'X'):
    P2CrossOrCircle = 'O'
else:
    P2CrossOrCircle = 'X'
endOfGame = False

def Main(arg):
    while endOfGame == False: 
        Board()
        endOfGame = True
def Board():
    print(coordinates[0][0]+'|'+coordinates[1][0]+'|'+coordinates[2][0])
    print('-'+'-'+'-'+'-'+'-')
    print(coordinates[0][1]+'|'+coordinates[1][1]+'|'+coordinates[2][1])
    print('-'+'-'+'-'+'-'+'-')
    print(coordinates[0][2]+'|'+coordinates[1][2]+'|'+coordinates[2][2])