import pygame, random, sys
import easygui as question
from pygame.locals import *
#calls on the inbuilt functions like pygame, random.sys to initiate the game
question.msgbox(msg="WELCOME TO CLASSIC SNAKE GAME")
#introducing the game 
question.msgbox(msg="  This game is a new version of the classic game 'snake' \n These are the rules of the game:-\n 1) eat the food particles to grow \n 2) If you run into the walls or YOUR SELF( the snake's movement is like a car, thus you cannot run into yourself), you DIE \n AND haters would be eaten by the snake \n \nTHANK YOU \n      MADE BY HARSH PATEL")
# to brief the user about the rules and the game
question.msgbox(msg=" pls enter the difficulty level of the game")
# asks for difficiulty


difficulty=(raw_input(" enter difficulty : 1 for beginner . 2 for expert and 3 for extreme   ")) # tells the user to enter difficulty

# this if statement id used for the difficulty of the game. here the frame rate of the game canges according to the user's choice.
if difficulty =="1":
	frame_rate = 10 # frame rate fpr difficulty
elif difficulty == "2":
	frame_rate = 20
elif difficulty =="3":
	frame_rate = 30
else:
	print ("Try again. Follow instructions")
	sys.exit()#Exits system if the user enter invalid numbers or words
	
question.msgbox(msg=" get yourself ready and hit the enter key to start the game")

	
#this fuction is called when the snake dies. its function is to give the final score and terminate the game	
def die(screen, score):
	font_score=pygame.font.SysFont('None', 37) # using system font for the score
	tot_score=font_score.render('Your score was: '+str(score), True, (0, 0, 0)) # printing score on the screen, i had to use a speific font so that i could print it on the screen
	screen.blit(tot_score, (300, 300)) # putting it on th screen
	pygame.display.update()
	pygame.time.wait(2000) # gives the user enough time to see the score 
	pygame.quit()
	question.msgbox("THANK YOU FOR PLAYING ")


def collide(x1, x2, y1, y2, w1, w2, h1, h2):#Detects collision between the food particle and the snake
	if y1+h1>y2 and y1<y2+h2 and x1+w1>x2 and x1<x2+w2:
		return True
	else:
		return False
	
'''
i have used rectangles as my snake and food. here i am initiating my snakes x value and y value. i am making the x and y value diiferenty because thats how i am using my collision function.
'''
x_pos_snake = [290, 290, 290, 290, 290] 
y_pos_snake = [290, 270, 250, 230, 210]
pos = 0
score = 0

food_position = (random.randint(0, 590), random.randint(0, 590)) # this way the food will show up on th screen on random places
pygame.init()

snake=pygame.display.set_mode((600, 600)) # setting up the screen
pygame.display.set_caption(' Snake Classic ') # naming the game

foodimage = pygame.Surface((10, 10)) # food size
foodimage.fill((255, 25, 25)) # food color
img = pygame.Surface((20, 20)) #snake length 
img.fill((255, 255, 25)) # snake color

f = pygame.font.SysFont('None', 37) # font for the score board

clock = pygame.time.Clock() # initiate time 
while True:
	clock.tick(frame_rate) # game spped. i have used this to determine the diificulty of the game.
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		elif event.type == KEYDOWN:
			if event.key == pygame.K_UP:
				pos = 2
			elif event.key == pygame.K_DOWN: 
				pos = 0
			elif event.key == pygame.K_LEFT: 
				pos = 3
			elif event.key == pygame.K_RIGHT:
				pos = 1
				# initiated all the key commands. here i can use all the arrow keys.
	
	i = len(x_pos_snake)-1
	# so the game works. i wanted to find collision so i used a while loop which will work no matter what so the if statement will repeat it self over and over.
	while i >= 2:
		if collide(x_pos_snake[0], x_pos_snake[i], y_pos_snake[0], y_pos_snake[i], 20, 20, 20, 20): #called collide funtion
			die(snake, score) #called die function
		i-= 1
	
	if collide(x_pos_snake[0], food_position[0], y_pos_snake[0], food_position[1], 20, 10, 20, 10):# called colide function but this time if it collides with food particle
		score+=1 # if returns true than increment the score by 1
		x_pos_snake.append(700) # append x value
		y_pos_snake.append(700) # append y value
		food_position=(random.randint(0,590),random.randint(0,590)) #used random and again put the food particle at an random place
	
	if x_pos_snake[0] < 0 or x_pos_snake[0] > 580 or y_pos_snake[0] < 0 or y_pos_snake[0] > 580: # to make sure that the snake dies when it touches the side of the screen, i have used or because i want the snake to die if any of the following statements are true.
		die(snake, score)# called function die
	i = len(x_pos_snake)-1
	
	while i >= 1:
		x_pos_snake[i] = x_pos_snake[i-1]
		y_pos_snake[i] = y_pos_snake[i-1]
		i -= 1
	'''
	here the snake's x and y value are changed as per the user's arrow keys selection.
	everytime an arrow key is pressed than depending on what value 'i' have chosen "pos" to become, than any of the following would be used.
	'''
	if pos==0:
		y_pos_snake[0] += 20 
	
	elif pos==1:
		x_pos_snake[0] += 20
	
	elif pos==2:
		y_pos_snake[0] -= 20
	
	elif pos==3:
		x_pos_snake[0] -= 20
		
	snake.fill ((255, 255, 255)) # background change to white
	
	for i in range(0, len(x_pos_snake)):
		snake.blit(img, (x_pos_snake[i], y_pos_snake[i])) # pasted the snake on the screen with our new x and y value
	
	snake.blit(foodimage, food_position) # pasted the food on the screen
	tot_score=f.render(str(score), True, (0, 0, 0)) #called on the font and updated the score with that particular font
	snake.blit(tot_score, (500, 10)) #pasted the score on the screen
	pygame.display.update()	# updated the display
	

				
				
	
	
