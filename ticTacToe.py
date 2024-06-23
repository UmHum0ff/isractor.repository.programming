coordinates = {" ", " ", " "},{" ", " ", " "},{" ", " ", " "}
P1CrossOrCircle = ""
P1CrossOrCircle = ""

while ((P1CrossOrCircle != "X") and (P1CrossOrCircle != "O")):
    P1CrossOrCircle = input("P1 choose X or O?").upper()
if (P1CrossOrCircle == "X"):
    P2CrossOrCircle = "O"
else:
    P2CrossOrCircle = "X"
endOfGame = False
o_as = Game()
o_as()




a_knight = Knight()


class Knight(object):
    def __call__(self, foo, bar, baz=None):
        print(foo)
        print(bar)
        print(bar)
        print(bar)
        print(baz)
class Game(object):
    def __call__(self):
        print(coordinates[0][0]+"|"+coordinates[1][0]+"|"+coordinates[2][0])
        print("-"+"-"+"-"+"-"+"-")
        print(coordinates[0][1]+"|"+coordinates[1][1]+"|"+coordinates[2][1])
        print("-"+"-"+"-"+"-"+"-")
        print(coordinates[0][2]+"|"+coordinates[1][2]+"|"+coordinates[2][2])