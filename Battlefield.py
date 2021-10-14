from Weapon import Weapon
from Robot import Robot
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
import random 

class Battlefield:
    def __init__(self):
      pass




laser = Weapon('laserbeam', 10)
atomic_launcher = Weapon('atomic launcher', 50)
one_punch = Weapon('big hug', 45)

weapons = [laser, atomic_launcher, one_punch]


robot1 = Robot('T1000', 300, random.choice(weapons))
robot2 = Robot('Jimmy5000', 400, random.choice(weapons))
robot3 = Robot('DB-7500', 1000, random.choice(weapons))


dino1 = Dinosaur('T-rex', 350, 15)
dino2 = Dinosaur('Raptor', 500, 35)
dino3 = Dinosaur('Triceratops', 950, 50)


fleet = Fleet([robot1,robot2,robot3])

herd = Herd([dino1,dino2,dino3])


def attack(self, target):
    if isinstance(self, Dinosaur):
        if self.health > 0 and target.health > 0:
            target.health = target.health - self.attack_power
            attack_names = ('slashe', 'megabite', 'tail whip')
            print(f'{self.name} {random.choice(attack_names)}s {target.name}')
        
            if target.health  < 1:
                print(f'{target.name} have died!')
    if isinstance(self, Robot):
        if self.health > 0 and target.health >0:
            target.health = target.health - self.weapon.attack_power
            print(f'{self.name} blasts {target.name} with a {self.weapon.name}')
            if target.health  < 1:
                print(f'{target.name} have died!')

while True: 
    randomdino = random.choice(herd.members_of_herd)
    randomrobo = random.choice(fleet.robot_members)
    randomorder = random.choice([randomdino, randomrobo])
    if randomorder == randomdino:
        attack(randomdino, randomrobo)
    else:
        attack(randomrobo, randomdino)
    if herd.members_of_herd[0].health < 1 and herd.members_of_herd[1].health <1 and herd.members_of_herd[2].health <1 :
        print('All the Dinosaurs have died.  Robots win!')
        break
    if fleet.robot_members[0].health < 1 and fleet.robot_members[1].health <1 and fleet.robot_members[2].health <1 :
        print('All the Robots have died.  Dinosaurs win!')
        break

    
    
    
 