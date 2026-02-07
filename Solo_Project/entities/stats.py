class Stats:
    def __init__(self, max_hp, attack, defense):

        max_hp = max(max_hp, 1)
        attack = max(attack, 0)
        defense = max(defense, 0)

        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense


    def take_damage(self, amount):
        if amount <= 0:
            return 0

        previous_hp = self.hp

        self.hp -= amount
        self.hp = max(self.hp, 0)

        damage_done = previous_hp - self.hp
        return damage_done


    def heal(self, amount):
        if amount <= 0:
            return 0
        
        previous_hp = self.hp

        self.hp += amount
        self.hp = min(self.hp, self.max_hp)

        heal_done = self.hp - previous_hp
        return heal_done
    

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
        

    def restore_full(self):

        self.hp = self.max_hp


    def modify_attack(self, amount):
        self.attack += amount

        if self.attack < 0:
            self.attack = 0
    

    def modify_defense(self, amount):
        self.defense += amount

        if self.defense < 0:
            self.defense = 0
    

    def modify_max_hp(self, amount):
        self.max_hp += amount

        self.max_hp = max(self.max_hp, 1)

        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
        
        
