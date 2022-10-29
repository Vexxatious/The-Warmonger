from factions.faction import Faction


class Orcs(Faction):
    def __init__(self):
        super().__init__(name="Orcs")

    def PerformAttack(self):
        if self.first_enemy.is_alive and self.second_enemy.is_alive:
            if self.first_enemy.name == "Elves":
                self.first_enemy.ReceiveAttack(self,
                                               self.number_of_units * 0.7 * self.attack_point)
                self.second_enemy.ReceiveAttack(self,
                                                self.number_of_units * 0.3 * self.attack_point)
            elif self.second_enemy.name == "Elves":
                self.second_enemy.ReceiveAttack(self,
                                                self.number_of_units * 0.7 * self.attack_point)
                self.first_enemy.ReceiveAttack(self,
                                               self.number_of_units * 0.3 * self.attack_point)
        elif self.first_enemy.is_alive and not self.second_enemy.is_alive:
            self.first_enemy.ReceiveAttack(
                self, self.number_of_units * self.attack_point)
        elif not self.first_enemy.is_alive and self.second_enemy.is_alive:
            self.second_enemy.ReceiveAttack(self,
                                            self.number_of_units * self.attack_point)

    def PurchaseWeapons(self, weapon_pt):
        self.attack_point += weapon_pt * 2
        return weapon_pt * 20

    def PurchaseArmors(self, armor_pt):
        self.health_point += armor_pt * 3
        return armor_pt * 1

    def ReceiveAttack(self, attacker, damage):
        if attacker.name == "Elves":
            damage = damage * 0.7
        elif attacker.name == "Dwarves":
            damage = damage * 0.8
        self.number_of_units -= damage / self.health_point

    def Print(self):
        print('"Stop running, you’ll only die tired!”')
        super().Print()
