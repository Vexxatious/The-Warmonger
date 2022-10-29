from factions.faction import Faction


class Dwarves(Faction):
    def __init__(self):
        super().__init__(name="Dwarves")

    def PerformAttack(self):
        if self.first_enemy.is_alive and self.second_enemy.is_alive:
            self.second_enemy.ReceiveAttack(self,
                                            self.number_of_units * 0.5 * self.attack_point)
            self.first_enemy.ReceiveAttack(self,
                                           self.number_of_units * 0.5 * self.attack_point)
        elif self.first_enemy.is_alive and not self.second_enemy.is_alive:
            self.first_enemy.ReceiveAttack(
                self, self.number_of_units * self.attack_point)
        elif not self.first_enemy.is_alive and self.second_enemy.is_alive:
            self.second_enemy.ReceiveAttack(self,
                                            self.number_of_units * self.attack_point)

    def PurchaseWeapons(self, weapon_pt):
        self.attack_point += weapon_pt
        return weapon_pt * 10

    def PurchaseArmors(self, armor_pt):
        self.health_point += armor_pt * 2
        return armor_pt * 3

    def ReceiveAttack(self, attacker, damage):
        self.number_of_units -= damage / self.health_point

    def Print(self):
        print('"Taste the power of our axes!”')
        super().Print()
