from factions.faction import Faction


class Elves(Faction):
    def __init__(self):
        super().__init__(name="Elves")

    def PerformAttack(self):
        if self.first_enemy.is_alive and self.second_enemy.is_alive:
            if self.first_enemy.name == "Orcs":
                self.first_enemy.ReceiveAttack(self,
                                               self.number_of_units * 0.6 * self.attack_point)
                self.second_enemy.ReceiveAttack(self,
                                                self.number_of_units * 0.4 * self.attack_point * 1.5)
            elif self.second_enemy.name == "Orcs":
                self.second_enemy.ReceiveAttack(self,
                                                self.number_of_units * 0.6 * self.attack_point)
                self.first_enemy.ReceiveAttack(self,
                                               self.number_of_units * 0.4 * self.attack_point * 1.5)
        elif self.first_enemy.is_alive and not self.second_enemy.is_alive:
            self.first_enemy.ReceiveAttack(
                self, self.number_of_units * self.attack_point * 1.5 if self.first_enemy.name == "Dwarves" else 1)
        elif not self.first_enemy.is_alive and self.second_enemy.is_alive:
            self.second_enemy.ReceiveAttack(self,
                                            self.number_of_units * self.attack_point * 1.5 if self.second_enemy.name == "Dwarves" else 1)

    def PurchaseWeapons(self, weapon_pt):
        self.attack_point += weapon_pt * 2
        return weapon_pt * 15

    def PurchaseArmors(self, armor_pt):
        self.health_point += armor_pt * 4
        return armor_pt * 5

    def ReceiveAttack(self, attacker, damage):
        if attacker.name == "Orcs":
            damage = damage * 1.25
        elif attacker.name == "Dwarves":
            damage = damage * 0.75
        self.number_of_units -= damage / self.health_point

    def Print(self):
        print('"You cannot reach our elegance.”')
        super().Print()
