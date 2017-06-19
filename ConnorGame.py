import pygame
import random

 
# defining colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (55, 255, 12,)
LBLUE = (90, 202, 255 )

level = 1
score = 0

# Sprite Codes for enemies/player/bullet etc.
class Block1(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
            """ Constructor. Pass in the color of the block,
            and its x and y position. """
            # Call the parent class (Sprite) constructor
            super().__init__()
     
            self.image = pygame.image.load("alienS.gif").convert()
           
            self.image.set_colorkey(WHITE)
      
            self.rect = self.image.get_rect()                 
        
    def reset_pos(self):
            self.rect.y = random.randrange(-300, -20)
            self.rect.x = random.randrange(0, screen_width)
     
    def update(self):
            
     
        # Move block down 1 and 3 pixels
        self.rect.y += 1
        if level == 2:
            self.rect.y += 3
          
     
            # If block is too far down it resets it to the top
        if self.rect.y > 690:
            self.reset_pos()    

class Block2(pygame.sprite.Sprite):
    
    def __init__(self):
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            self.image = pygame.image.load("alien1.gif").convert()
           
      
             # Set background color to be transparent. Adjust to WHITE if your
             # background is WHITE.
            self.image.set_colorkey(WHITE)
      
             # Fetch the rectangle object that has the dimensions of the image
             # image.
             # Update the position of this object by setting the values 
             # of rect.x and rect.y
            self.rect = self.image.get_rect()     
     
    def reset_pos(self):
            self.rect.y = random.randrange(-300, -20)
            self.rect.x = random.randrange(0, screen_width)
     
    def update(self):
            
     
            # Move block down 3 or 5 pixels
            self.rect.y += 3
            if level == 2:
                self.rect.y += 5
            
     
            # If block is at the bottom bring back to the top
            if self.rect.y > 690:
                self.reset_pos()    
                
 
 
class Player(pygame.sprite.Sprite):
  
 
    def __init__(self):
         # Call the parent class (Sprite) constructor
        super().__init__() 
  
        #loads image for the player sprite
        self.image = pygame.image.load("player.gif").convert()
       
  
         # Set background color to be transparent. Adjust to WHITE if your
         # background is WHITE.
        self.image.set_colorkey(WHITE)
  
         # Fetch the rectangle object that has the dimensions of the image
         # image.
         # Update the position of this object by setting the values 
         # of rect.x and rect.y
        self.rect = self.image.get_rect()
               
               
      
    
    def update(self):

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Allows the sprite to move freely
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
 
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        # This is code for the bullet sprite
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# Start pygame
pygame.init()

pygame.display.set_caption("Aliens Attack")

pygame.mouse.set_visible(False)
 
gameover = False

# loops until you close the game
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

# For the Main Menu 
display_instructions = True
instruction_page = 1
 
# Set the height and width of the screen
screen_width = 500
screen_height = 690
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()

block2_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 

#creating the sprites
for i in range(35):
    # This represents a block
    block = Block1()
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    
for i in range(20):
      # This represents a lock
    block = Block2()
     
        # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
     
        # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loads custom images for the main menu and game background
background_image = pygame.image.load("Background.gif").convert()
menu_image = pygame.image.load("mainmenu.gif").convert()

# displays level text and what level you are on
if level == 1:
    text = font.render("Level 1 ", True, WHITE)
    screen.blit(text, [10, 10])

if level == 2:
    text = font.render("Level 2 ", True, WHITE)
    screen.blit(text, [10, 10])
        


# sets score to 0
score = 0
player.rect.y = 370

# code for the instruction page/ main menu
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 4:
               display_instructions = False
               
    # Set the screen background
    screen.fill(WHITE)
    screen.blit(menu_image , [0, 0])
 
    if instruction_page == 1:
        # Draw instructions page 1
 
        text = font.render("WELCOME TO MY GAME ", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("CLICK TO CONTINUE", True, WHITE)
        screen.blit(text, [10, 40])
 
    if instruction_page == 2:
        # Draw instructions page 2
        text = font.render("MOVE SHIP WITH MOUSE", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render("CLICK TO SHOOT ", True, WHITE)
        screen.blit(text, [10, 40])
       
        text = font.render("KILL 25 ENEMIES FOR NEXT LEVEL ", True, WHITE)
        screen.blit(text, [10, 70])   
        
        text = font.render("KILL 55 ENEMIES TO END THE GAME ", True, WHITE)
        screen.blit(text, [10, 100])              
        
         
         
    
    if instruction_page == 3:
            # Draw instructions page 3
        text = font.render("MOVE YOUR MOUSE TO THE BOTTOM ", True, WHITE)
        screen.blit(text, [10, 10])
     
        text = font.render("OF THE SCREEN AND THEN CLICK TO", True, WHITE)
        screen.blit(text, [10, 40])   
        
        text = font.render("TO PLAY", True, WHITE)
        screen.blit(text, [10, 70])         
        
        
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Updates the screen
    pygame.display.flip()
 
# -------- Main Program Loop ----------

while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if you clickvb
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x+32
            bullet.rect.y = player.rect.y 
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
   
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
            if score == 25:
                level += 1            
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        


             
     
            
            

   
   
    # Clear the screen
    
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    
    
    #displays the text for level 1
    if level == 1:
        text = font.render("Level 1 ", True, WHITE)
        screen.blit(text, [10, 10])
    # displays text for level 2
    if level == 2:
        text = font.render("Level 2 ", True, WHITE)
        screen.blit(text, [10, 10])  
    
    # collision detection
    if pygame.sprite.spritecollide(player, block_list, True):
        gameover = True
        
    # displays game over screen        
    if gameover == True:
        screen.blit(background_image, [0, 0])
        screen.fill(BLACK)
        text = font.render("GAME OVER", True, WHITE)
        screen.blit(text, [100, 130])
        text = font.render("CLOSE GAME TO PLAY AGAIN", True, WHITE)
        screen.blit(text, [100, 160 ])
        for sprites in all_sprites_list:
            all_sprites_list.remove(sprites)
            
    if score == 55:
        screen.blit(background_image, [0, 0])
        screen.fill(BLACK)
        text = font.render("YOU WIN", True, WHITE)
        screen.blit(text, [100, 130])

        for sprites in all_sprites_list:
            all_sprites_list.remove(sprites)        
        
            
        
    
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()