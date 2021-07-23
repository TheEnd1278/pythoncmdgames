import time


class Feld:
    def __init__(self):
        self.zustand = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.list2 = []

    def feld_zustand(self):
        for x in self.zustand:
            if x == 0:
                self.list2.append(" ")
            elif x == 1:
                self.list2.append("x")
            else:
                self.list2.append("o")

    def print_feld(self):
        self.list2 = []
        self.feld_zustand()
        feld = " {} | {} | {} \n {} | {} | {} \n {} | {} | {} ".format(self.list2[0], self.list2[1], self.list2[2],
                                                                       self.list2[3], self.list2[4], self.list2[5],
                                                                       self.list2[6], self.list2[7], self.list2[8], )
        return feld

    def reset_zustand(self):
        self.zustand = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Game:
    def __init__(self):
        self.x = 1
        self.o = -1
        self.feld = Feld()
        self.punktestand = {
            "x": 0,
            "o": 0
        }

    def play_game(self):
        print("---Willkommen bei Tiktaktoe!---\n")
        answer = input("\nMöchtest du eine Runde starten?\nGebe q für nein und "
                       "eine beliebige Taste für ja an!").lower()
        while answer != "q":
            self.feld.reset_zustand()

            print("\n")
            if len(self.feld.list1) == 9 and answer != "q":
                print(self.feld.print_feld())

            while len(self.feld.list1) > 0 and answer != "Q":
                while True:
                    try:
                        input1 = int(input(f"Auf welcher Stelle {self.feld.list1} möchtest du dein x setzen?"))
                        if input1 in self.feld.list1:
                            self.feld.zustand[input1 - 1] = self.x
                            self.feld.list1.remove(input1)
                            print(self.feld.print_feld())
                            # print(self.feld.zustand)
                            break
                        else:
                            print("Falsche Eingabe")
                            continue
                    except ValueError:
                        print("Falsche Eingabe")
                        continue
                if self.feld.zustand[0] == 1 and self.feld.zustand[1] == 1 and self.feld.zustand[2] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[3] == 1 and self.feld.zustand[4] == 1 and self.feld.zustand[5] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[6] == 1 and self.feld.zustand[7] == 1 and self.feld.zustand[8] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[0] == 1 and self.feld.zustand[3] == 1 and self.feld.zustand[6] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[2] == 1 and self.feld.zustand[5] == 1 and self.feld.zustand[8] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[0] == 1 and self.feld.zustand[4] == 1 and self.feld.zustand[8] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[2] == 1 and self.feld.zustand[4] == 1 and self.feld.zustand[6] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif self.feld.zustand[1] == 1 and self.feld.zustand[4] == 1 and self.feld.zustand[7] == 1:
                    print("x gewinnt")
                    self.punktestand["x"] += 1
                    break
                elif not self.feld.list1:
                    print("Unentschieden")
                    break

                while True:
                    try:
                        input2 = int(input("Auf welcher Stelle {} möchtest du dein o setzen?".format(self.feld.list1)))
                        if input2 in self.feld.list1:
                            self.feld.zustand[input2 - 1] = self.o
                            self.feld.list1.remove(input2)
                            print(self.feld.print_feld())
                            # print(self.feld.zustand)
                            break
                        else:
                            print("Falsche Eingabe")
                            continue
                    except ValueError:
                        print("Falsche Eingabe")
                        continue
                if self.feld.zustand[0] == -1 and self.feld.zustand[1] == -1 and self.feld.zustand[2] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[3] == -1 and self.feld.zustand[4] == -1 and self.feld.zustand[5] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[6] == -1 and self.feld.zustand[7] == -1 and self.feld.zustand[8] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[0] == -1 and self.feld.zustand[3] == -1 and self.feld.zustand[6] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[2] == -1 and self.feld.zustand[5] == -1 and self.feld.zustand[8] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[0] == -1 and self.feld.zustand[4] == -1 and self.feld.zustand[8] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[2] == -1 and self.feld.zustand[4] == -1 and self.feld.zustand[6] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif self.feld.zustand[1] == -1 and self.feld.zustand[4] == -1 and self.feld.zustand[7] == -1:
                    print("o gewinnt")
                    self.punktestand["o"] += 1
                    break
                elif not self.feld.list1:
                    print("Unentschieden")
                    break
            answer = input("\n Möchtest du eine erneute Runde starten?\n Gebe q für nein und "
                           "eine beliebige Taste für ja an!").lower()


i = Game()
i.play_game()
print("######Game History######")
for x, y in i.punktestand.items():
    print(f"Der Spieler mit dem Symbol {x} hat {y} mal gewonnen.")
if i.punktestand["x"] > i.punktestand["o"]:
    print("Der Spieler mit dem Symbol x gewinnt, da er die meisten Runden gewonnen hat.")
elif i.punktestand["x"] < i.punktestand["o"]:
    print("Der Spieler mit dem Symbol o gewinnt, da er die meisten Runden gewonnen hat.")
else:
    print("Beide Spieler haben gleichoft gewonnen, deswegen ist es ein unentschieden.")

time.sleep(5)