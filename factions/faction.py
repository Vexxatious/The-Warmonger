import math


class Faction:
    def __init__(self, name="Default", number_of_units=50, attack_point=30, health_point=150, regen=10):
        self.name = name
        self.number_of_units = number_of_units
        self.attack_point = attack_point
        self.health_point = health_point
        self.regen = regen
        self.total_health = number_of_units * health_point
        self.is_alive = True

    def AssgnEnemies(self, first, second):
        self.first_enemy = first
        self.second_enemy = second

    def PerformAttack(self):
        pass

    def ReceiveAttack(self):
        pass

    def PurchaseWeapons(self):
        pass

    def PurchaseArmors(self):
        pass

    def Print(self):
        status = "Alive" if self.is_alive else "Dead"

        print(f"Faction Name:\t{self.name}".expandtabs(30) +
              f"\nStatus:\t{status}".expandtabs(30) +
              f"\nNumber of Units:\t{self.number_of_units}".expandtabs(30) +
              f"\nAttack Point:\t{self.attack_point}".expandtabs(30) +
              f"\nHealth Point:\t{self.health_point}".expandtabs(30) +
              f"\nUnit Regen Number:\t{self.regen}".expandtabs(30) +
              f"\nTotal Faction Health:\t{self.total_health}".expandtabs(30)+"\n")

    def EndTurn(self):
        self.number_of_units = math.floor(self.number_of_units)

        if self.number_of_units < 0:
            self.number_of_units = 0
            self.is_alive = False

        self.total_health = self.number_of_units * self.health_point
        self.Print()
