import time
from grovepi import *

# === set grovepi+ port 4 as output ===

em = 4
pinMode(em,"OUTPUT")
def em_control(state):
	em = 4
	try:
		digitalWrite(em,state)	# 1: Switch on, 0: Switch off
		time.sleep(1)
	except KeyboardInterrupt:
		digitalWrite(em,0)
	except IOError:
		digitalWrite(em,0)
		print ("Error")

w = 15
h = 16
moves = [[0 for x in range(w)] for y in range(h)]

i = 0
j = 0
lines = [line.rstrip('\n') for line in open('moves.txt')]
for line in lines:
	elements = line.split(',')
	j=0
	for e in elements:
		moves[i][j] = float(e)
		j+=1
	i+=1

def move_robot(poppy,motor_angles,mov_time):
	delay = 0.05
	poppy.motors[0].goto_position(motor_angles[0],mov_time)
	time.sleep(delay)
	poppy.motors[1].goto_position(motor_angles[1],mov_time)
	time.sleep(delay)
	poppy.motors[2].goto_position(motor_angles[2],mov_time)
	time.sleep(delay)
	poppy.motors[3].goto_position(motor_angles[3],mov_time)
	time.sleep(delay)
	poppy.motors[4].goto_position(motor_angles[4],mov_time)
	time.sleep(delay)
	poppy.motors[5].goto_position(motor_angles[5],mov_time)
	time.sleep(delay)
	poppy.motors[6].goto_position(motor_angles[6],mov_time)
	time.sleep(delay)
	poppy.motors[7].goto_position(motor_angles[7],mov_time)
	time.sleep(delay)
	poppy.motors[8].goto_position(motor_angles[8],mov_time)
	time.sleep(delay)
	poppy.motors[9].goto_position(motor_angles[9],mov_time)
	time.sleep(delay)
	poppy.motors[10].goto_position(motor_angles[10],mov_time)
	time.sleep(delay)
	poppy.motors[11].goto_position(motor_angles[11],mov_time)
	time.sleep(delay)
	poppy.motors[12].goto_position(motor_angles[12],mov_time)
	time.sleep(delay)
	poppy.motors[13].goto_position(motor_angles[13],mov_time)
	time.sleep(delay)
	poppy.motors[14].goto_position(motor_angles[14],mov_time)
	time.sleep(delay)
	time.sleep(1.5)
def move_robot_alternative(poppy,motor_angles,mov_time):
	delay = 0.05
	poppy.motors[0].goto_position(motor_angles[0],mov_time)
	time.sleep(delay)
	poppy.motors[3].goto_position(motor_angles[3],mov_time)
	time.sleep(delay)
	poppy.motors[4].goto_position(motor_angles[4],mov_time)
	time.sleep(delay)
	poppy.motors[5].goto_position(motor_angles[5],mov_time)
	time.sleep(delay)
	poppy.motors[6].goto_position(motor_angles[6],mov_time)
	time.sleep(delay)
	poppy.motors[7].goto_position(motor_angles[7],mov_time)
	time.sleep(delay)
	poppy.motors[8].goto_position(motor_angles[8],mov_time)
	time.sleep(delay)
	poppy.motors[9].goto_position(motor_angles[9],mov_time)
	time.sleep(delay)
	poppy.motors[10].goto_position(motor_angles[10],mov_time)
	time.sleep(delay)
	poppy.motors[11].goto_position(motor_angles[11],mov_time)
	time.sleep(delay)
	poppy.motors[12].goto_position(motor_angles[12],mov_time)
	time.sleep(delay)
	poppy.motors[13].goto_position(motor_angles[13],mov_time)
	time.sleep(delay)
	poppy.motors[14].goto_position(motor_angles[14],mov_time)
	time.sleep(delay)
	poppy.motors[1].goto_position(motor_angles[1],mov_time)
	time.sleep(delay)
	poppy.motors[2].goto_position(motor_angles[2],mov_time)
	time.sleep(delay)
	time.sleep(1.5)
def initial_pos(poppy):
	motor_angles = [0,0,45,0,5,-5,0,-10,15,20,-10,-180,0,-20,0]
	mov_time = 1.5
	move_robot_alternative(poppy,motor_angles,mov_time)
	em_control(0)
def pre_grab(poppy):
	motor_angles = moves[0]
	mov_time = 1.5
        move_robot(poppy,motor_angles,mov_time)
def center(poppy):
	mov_time = 1.5
        motor_angles = moves[6]
        move_robot(poppy,motor_angles,mov_time)
def wave(poppy):
	return
	#em_control(0)
	#mov_time = 0.5
	#for i in range(0,3):
	#	motor_angles = [1.63, -3.22, 42.95, 3.65, 12.53, -5.43, 0.38, -22.62, 39.76, 45.76, -76.81, -170.57, -11.36, 1.71, 3.36]
	#	move_robot(poppy,motor_angles,mov_time)
	#	motor_angles = [2.42, -8.05, 42.15, 2.86, 17.19, -5.43, 0.38, -27.1, 36.33, 38.9, -14.48, -171.8, -11.19, 1.54, 3.71]
	#	move_robot(poppy,motor_angles,mov_time)
def take_piece_1(poppy):
	# prepare to take a piece
	pre_grab(poppy)
	# low the hand to the piece
	motor_angles = moves[1]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)
	pre_grab(poppy)
def take_piece_2(poppy):
	# prepare to take a piece
	pre_grab(poppy)
	# low the hand to the piece
	motor_angles = moves[2]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)
	pre_grab(poppy)
def take_piece_3(poppy):
	# prepare to take a piece
	pre_grab(poppy)
	# low the hand to the piece
	motor_angles = moves[3]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)
	pre_grab(poppy)
def take_piece_4(poppy):
	# prepare to take a piece
	pre_grab(poppy)
	# low the hand to the piece
	motor_angles = moves[4]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)
	pre_grab(poppy)
def take_piece_5(poppy):
	# prepare to take a piece
	pre_grab(poppy)
	# low the hand to the piece
	motor_angles = moves[5]
	mov_time = 1.5
	move_robot(poppy,motor_angles,mov_time)
	# turn on em
	em_control(1)
	pre_grab(poppy)
def move_to_board(poppy,row,col):
	# move to the center of the board
	mov_time = 1.5
	center(poppy)
	# select where to play

	if(row == 0):
		if(col == 0):
			motor_angles = moves[7]
		elif(col == 1):
			motor_angles = moves[8]
		elif(col == 2):
			motor_angles = moves[9]
	elif(row == 1):
		if(col == 0):
			motor_angles = moves[10]
		elif(col == 1):
			motor_angles = moves[11]
		elif(col == 2):
			motor_angles = moves[12]
	elif(row == 2):
		if(col == 0):
			motor_angles = moves[13]
		elif(col == 1):
			motor_angles = moves[14]
		elif(col == 2):
			motor_angles = moves[15]

	move_robot(poppy,motor_angles,mov_time)
	time.sleep(3)
	em_control(0)
	 # move to the center of the board
        mov_time = 2.5
        motor_angles = [23.08,-4.1,50.68,-2.86,16.57,-9.53,10.06,-4.95,11.01,-25.63,-76.81,-133.91,-1.34,17.98,45.16]
        move_robot(poppy,motor_angles,mov_time)
	initial_pos(poppy)
def robot_play(n_play,robot,player_1,player_2,row,col,poppy):
	if((robot == player_1 and n_play == 1) or (robot == player_2 and n_play == 2)):
		take_piece_1(poppy)
	elif((robot == player_1 and n_play == 3) or (robot == player_2 and n_play == 4)):
		take_piece_2(poppy)
	elif((robot == player_1 and n_play == 5) or (robot == player_2 and n_play == 6)):
		take_piece_3(poppy)
	elif((robot == player_1 and n_play == 7) or (robot == player_2 and n_play == 8)):
		take_piece_4(poppy)
	elif(robot == player_1 and n_play == 9):
		take_piece_5(poppy)

	move_to_board(poppy,row,col)
	initial_pos(poppy)
def robot_action(current_winner, poppy,robot,empty):
	mov_time=1.5
	if (current_winner==empty):
		return 
	elif(current_winner==robot):
		motor_angles = [8.57,0.74,50.15,-14.81,19.82,-80.79,8.01,-92.33,98.84,-105.19,67.36,-95.32,12.81,77.23,-3.58]
	else:
		motor_angles = [5.41,-5.51,75.74,-26.95,12.35,-4.25,0.67,-0.2,10.31,-20.0,-76.55,-102.97,4.55,17.98,68.24]
	move_robot(poppy,motor_angles,mov_time)
	em_control(0)
