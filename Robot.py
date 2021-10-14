

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.weapon =  weapon
        self.health = health
    
    def attack(self, target):
        target.health = target.health - self.weapon.attack_power

