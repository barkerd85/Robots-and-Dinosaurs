from Weapon import Weapon
from Robot import Robot
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
      pass




laser = Weapon('laserbeam', 10)
atomic_launcher = Weapon('atomic launcher', 50)
one_punch = Weapon('One punch', 5000)


robot1 = Robot('T1000', 300, laser)
robot2 = Robot('JD5000', 400, atomic_launcher)
robot3 = Robot('DB-7500', 1000, one_punch)


dino1 = Dinosaur('T-rex', 350, 15)
dino2 = Dinosaur('Raptor', 450, 100)
dino3= Dinosaur('Hybrid', 800, 4000)


fleet = Fleet([robot1,robot2,robot3])

herd = Herd([dino1,dino2,dino3])




