from Reward import Reward
from Robot import Robot

def check_reward(robot, rewards):
	ok = False
	for reward in rewards:
		if reward.x == robot.x and reward.y == robot.y:
			print('O robô achou a reponsensa: %s' % reward.name)
			ok = True
	return ok

import random
r1 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r2 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r3 = Reward(random.randint(0,10),random.randint(0,10),'arma')
r4 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r5 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r6 = Reward(random.randint(0,10),random.randint(0,10),'arma')
r7 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r8 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r9 = Reward(random.randint(0,10),random.randint(0,10),'arma')
r10 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r11 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r12 = Reward(random.randint(0,10),random.randint(0,10),'arma')

rewards = [r1,r2,r3]
robot = Robot(random.randint(0,10),random.randint(0,10))

for i in range(10):
	moviment = input("Digite up, down, left or right para o movimento: ")
	if moviment == 'up':
		robot.move_up()
	elif moviment == 'down':
		robot.move_down()
	elif moviment == 'left':
		robot.move_left()
	elif moviment == 'right':
		robot.move_right()
	else:
		print('Movimento inválido')
		continue
	print(robot)
	check_reward(robot, rewards)




