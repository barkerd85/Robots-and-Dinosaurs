import Robot
import Dinosaur
import Weapon


laser = Weapon('laserbeam', 10)
atomic_launcher = Weapon('atomic launcher', 50)
one_punch = Weapon('One punch', 5000)

robot1 = Robot('T1000', 300, laser)
robot2 = Robot('T5000', 400, atomic_launcher)
robot3 = Robot('DB-7500', 1000, one_punch)