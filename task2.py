class Piyada():
    def gedis(self):
        print("Pawn: one or two steps forward")
class Top():
    def gedis(self):
        print("Rook: plus (+) direction")
class At():
    def gedis(self):
        print("Knight: L direction")
class Fil():
    def gedis(self):
        print("Bishop: cross (X) forward")
class Vezir():
    def gedis(self):
        print("Queen: all directions")
class Sah():
    def gedis(self):
        print("king: one step around")

def Gedisler(figur):
    figur.gedis()


pawn=Piyada()
rook=Top()
knight=At()
bishop=Fil()
queen=Vezir()
king=Sah()


Gedisler(pawn)
Gedisler(rook)
Gedisler(knight)
Gedisler(bishop)
Gedisler(queen)
Gedisler(king)