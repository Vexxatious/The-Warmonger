from factions.dwarves import Dwarves
from factions.elves import Elves
from factions.orcs import Orcs
from merchant import Merchant
import os


class Game:
    def __init__(self):
        os.system("clear")
        print("Welcome to The Warmonger: A New Dimension\n")

        self.orcs = Orcs()
        self.elves = Elves()
        self.dwarves = Dwarves()
        self.merchant = Merchant()

        self.factions = [self.orcs, self.elves, self.dwarves]

        self.orcs.AssgnEnemies(self.elves, self.dwarves)
        self.elves.AssgnEnemies(self.orcs, self.orcs)
        self.dwarves.AssgnEnemies(self.orcs, self.elves)

        self.merchant.AssgnFactions(self.orcs, self.dwarves, self.elves)

        self.gameOver = False
        self.merchant.Print()
        while not self.gameOver:
            menu_input = getMenuInput()
            while not menu_input in ["1", "2", "3", "4", "5", "6"]:
                os.system("clear")
                print("Wrong input")
                menu_input = getMenuInput()

            os.system("clear")
            if menu_input == "1":
                faction_input = selectFaction()
                while not faction_input in ["1", "2", "3", "4"]:
                    os.system("clear")
                    print("Wrong input")
                    faction_input = selectFaction()
                os.system("clear")
                if faction_input == "1":
                    self.orcs.Print()
                elif faction_input == "2":
                    self.elves.Print()
                elif faction_input == "3":
                    self.dwarves.Print()

            elif menu_input == "2":
                faction_input, sell_amount = getWeaponsSellInput()
                while not faction_input == "4" and not self.merchant.SellWeapons(
                        self.factions[int(faction_input) - 1], int(sell_amount)):
                    faction_input, sell_amount = getWeaponsSellInput()

            elif menu_input == "3":
                faction_input, sell_amount = getArmorsSellInput()
                while not faction_input == "4" and not self.merchant.SellArmors(
                        self.factions[int(faction_input) - 1], int(sell_amount)):
                    faction_input, sell_amount = getArmorsSellInput()
            elif menu_input == "4":
                self.orcs.PerformAttack()
                self.elves.PerformAttack()
                self.dwarves.PerformAttack()

                self.orcs.EndTurn()
                self.elves.EndTurn()
                self.dwarves.EndTurn()
                self.merchant.EndTurn()

                if sum([self.orcs.is_alive, self.dwarves.is_alive, self.elves.is_alive]) == 1:
                    self.gameOver = True
                    print(
                        f"Game Over!\nTotal Revenue: {self.merchant.revenue}\n")
                    play_again = input("Play Again ? (y/n)\n")
                    if play_again == "y":
                        self.__init__()
            elif menu_input == "5":
                self.__init__()

            elif menu_input == "6":
                self.gameOver = True


def getWeaponsSellInput():
    faction_input = selectFaction()
    while not faction_input in ["1", "2", "3", "4"]:
        os.system("clear")
        print("Wrong input")
        faction_input = selectFaction()
    if faction_input == "4":
        return "4", 0
    sell_amount = input("How many weapons do you want to sell?\n")
    while not sell_amount.isnumeric():
        os.system("clear")
        print("Wrong input")
        sell_amount = input(
            "How many weapons do you want to sell?\n")
    return faction_input, sell_amount


def getArmorsSellInput():
    faction_input = selectFaction()
    while not faction_input in ["1", "2", "3", "4"]:
        os.system("clear")
        print("Wrong input")
        faction_input = selectFaction()
    if faction_input == "4":
        return "4", 0
    sell_amount = input("How many armors do you want to sell?\n")
    while not sell_amount.isnumeric():
        os.system("clear")
        print("Wrong input")
        sell_amount = input(
            "How many armors do you want to sell?\n")
    return faction_input, sell_amount


def selectFaction():
    return input("1-Orcs\n2-Elves\n3-Dwarves\n4-Back\n")


def getMenuInput():
    return input("1- See the information of a faction\n" +
                 "2- Sell weapons to a faction\n" +
                 "3- Sell armors to a faction\n" +
                 "4- End the turn\n"
                 "5- End the game\n"
                 "6- Quit\n")
