#Capstone Project II

#Module imports
import pygame 
import random 

# Initializing the pygame module
pygame.init() 

#Creating a screen/window that the game will run on using defined height and width values
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height)) 

#Creating the player and enemies using their corresponding images
player = pygame.image.load('image.png')
enemy1 = pygame.image.load('enemy.png')
enemy2 = pygame.image.load('enemy2.png')
enemy3 = pygame.image.load('enemy3.png')

#creating prize that player could collide with and win
prize = pygame.image.load("prize.png")

#Setting the dimensions(width & height) for the player and enemies, to use them later (keeping the characters on screen and detecting collisions)
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

#setting prize dimension
prize_height = prize.get_height()
prize_width = prize.get_width()

#Creating the player's initial starting position within the screen
player_XPosition = 100
player_YPosition = 50

#Creating the enemy start positions(edge of the screen - right side - and a random y position within the screen height)
enemy1_XPosition =  screen_width
enemy1_YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2_XPosition =  screen_width
enemy2_YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3_XPosition =  screen_width
enemy3_YPosition =  random.randint(0, screen_height - enemy3_height)

#creating a screen position for the prize
prize_XPosition = screen_width - prize_width
prize_YPosition = random.randint(0, screen_height - prize_height)

#Initializing the variables that will be used to check whether is key is pressed - or not - to false(as they're not currently in use)
keyUp= False
keyDown = False
keyLeft= False
keyRight = False

#Main game loop. This will loop the code within the loop until the game/program quits
while True: 
    #Clearing the screen and then drawing the player, enemy and prize images at their previously specified positions
    screen.fill(0)
    screen.blit(player, (player_XPosition, player_YPosition))
    screen.blit(enemy1, (enemy1_XPosition, enemy1_YPosition))
    screen.blit(enemy2, (enemy2_XPosition, enemy2_YPosition))
    screen.blit(enemy3, (enemy3_XPosition, enemy3_YPosition))
    screen.blit(prize, (prize_XPosition, prize_YPosition))

    
    #Update the screen
    pygame.display.flip() 
    
    #Loop through events occuring in the game.
    for event in pygame.event.get():
    
        #Check if user quit the program and quit the program if so. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #Check if the user presses on a key.
        if event.type == pygame.KEYDOWN:
        
            #Check which of the directional keys is pressed, then set the corresponding variable to true
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        #Otherwise if the user is not pressing on a key.
        if event.type == pygame.KEYUP:
        
            #Check which key is not pressed and set the corresponding variable to false
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    #After checking which keys are pressed, move the player accordingly by updating the X andY positions
    if keyUp == True:
        #The screen height starts at 0 at the top of the screen, so moving up is done by decreasing the Y position
        if player_YPosition > 0 : #Check added to ensure the player does not move up beyond the screen border
            player_YPosition -= 1
        
    if keyDown == True:
        if player_YPosition < (screen_height - player_height): #ensure player doesn't move down below the screen border
            player_YPosition += 1   #Moving down is done by increasing the Y position
    
    if keyLeft == True:
        #The screen width starts at 0 at the left side of the screen, so moving left is done by decreasing the X position
        if player_XPosition > 0 : #Check added to ensure the player does not move left beyond the screen border
            player_XPosition -= 1  
    
    if keyRight == True:
        if player_XPosition < (screen_width - player_width):    #ensure player doesn't move right past the screen border
            player_XPosition += 1   #Moving right is done by increasing the X position
    
    #Creating a bounding box around the player to use when detecting collisions with the enemies
    playerBox = pygame.Rect(player.get_rect())

    #Constantly updating the bounding box to move with the player
    playerBox.top = player_YPosition
    playerBox.left = player_XPosition
    
    #Creating bounding boxes for the enemies and updating them so they move with the enemy
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1_YPosition
    enemy1Box.left = enemy1_XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2_YPosition
    enemy2Box.left = enemy2_XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3_YPosition
    enemy3Box.left = enemy3_XPosition    

    #Creating & updating a bounding box for the prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_YPosition
    prizeBox.left = prize_XPosition


    #If any of the 3 enemies collide (bounding boxes intersecting) into the player, the player loses and the game quits
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    #If all 3 enemies reach the left side of the screen without colliding into the player, or if the player is able to make it to the prize. The player wins and the game quits.
    if (enemy1_XPosition < 0 - enemy1_width and enemy2_XPosition < 0 - enemy2_width and enemy3_XPosition < 0 - enemy3_width) or (playerBox.colliderect(prizeBox)): 
        print("You win!") 
        pygame.quit()
        exit(0)

     
    #Move enemies towards player. The enemies have different movement speeds.
    enemy1_XPosition -= 0.5
    enemy2_XPosition -= 0.65
    enemy3_XPosition -= 1.2


    