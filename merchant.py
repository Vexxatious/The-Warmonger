class Merchant:
    def __init__(self, starting_weapon_pt=10, starting_armor_pt=10):
        self.starting_armor_pt = starting_armor_pt
        self.starting_weapon_pt = starting_weapon_pt
        self.revenue = 0
        self.weapon_pt_left = starting_armor_pt
        self.armor_pt_left = starting_weapon_pt

    def AssgnFactions(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def SellWeapons(self, faction, weapon_pt):
        if not faction.is_alive:
            print("The faction you want to sell weapons is dead!")
            return False
        if self.weapon_pt_left < weapon_pt:
            print("You try to sell more weapons than you have in possession!")
            return

        self.revenue += faction.PurchaseWeapons(weapon_pt)
        self.weapon_pt_left -= weapon_pt
        print("Weapons sold!\n")
        self.Print()
        return True

    def SellArmors(self, faction, armor_pt):
        if not faction.is_alive:
            print("The faction you want to sell armors is dead!")
            return False
        if self.armor_pt_left < armor_pt:
            print("You try to sell more armors than you have in possession!")
            return False
        self.revenue += faction.PurchaseArmors(armor_pt)
        self.armor_pt_left -= armor_pt
        print("Armors sold!\n")
        self.Print()
        return True

    def EndTurn(self):
        self.armor_pt_left = self.starting_armor_pt
        self.weapon_pt_left = self.starting_weapon_pt

        self.Print()

    def Print(self):
        print(f"Revenue:\t\t{self.revenue}".expandtabs(30) +
              f"\nWeapon Points Left:\t{self.weapon_pt_left}".expandtabs(30) +
              f"\nArmor Points Left:\t{self.armor_pt_left}".expandtabs(30)+"\n")
