# All imports here #
import pygame
import time 
from time import sleep
# End Imports      #

# Initialization of Window #
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 900
display_height = 600
# Main menu #
SXpos = 192
SYpos = 55
Selection = 'start'
Color_Option_A = white
Color_Option_B = red
Color_Option_C = red
Color_Option_D = red
# End Main Menu #

# Settings Menu #
SSXpos = -33
SSYpos = 245
SSXpos2 = -75
SSYpos2 = 245
SColor_Option_A = red
SColor_Option_B = red
BlueNum = 10
RedNum = 10
SSelection = 'start'
# End Settings Menu#
windowDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Box Collectors')

# End of initialization of window #

# Clock initialization(FPS) #
clock = pygame.time.Clock()
FPS = 15
# End of clock initialization(FPS) #

# Initialization of font #
fontA = pygame.font.SysFont(None,14)
fontB = pygame.font.SysFont(None,18)
fontC = pygame.font.SysFont(None,20)
fontD = pygame.font.SysFont(None,25)
fontE = pygame.font.SysFont(None,34)
# End Initialization of font #

# Calculation of area of text # 
def text_objects(text,color,FontName):
    textSurface = FontName.render(text,True,color)
    return textSurface, textSurface.get_rect()
# End of calculation of area of text #

# Message Function #
def message_to_screen(msg,color,FontName,pos,Backwards):
    textSurf, textRect = text_objects(msg,color,FontName)
    textRect.center = ((display_width/2)- Backwards),(pos)
    windowDisplay.blit(textSurf,textRect)
# End Message Function #

def MenuLoop():
    # define global variables #
    global SXpos, SYpos, Selection, Color_Option_A ,Color_Option_B,Color_Option_C,Color_Option_D
    # end define #
    
    MenuChange = False # set menuchange to false

    while not MenuChange: # run loop untill menuChange changes to true
        windowDisplay.fill(black) # change window colour to black
        message_to_screen('START', Color_Option_A,fontE,200,0) # add text to screen
        message_to_screen('INSTRUCTIONS', Color_Option_B,fontE,230,0) # add text to screen
        message_to_screen('SETTINGS', Color_Option_C,fontE,260,0) # add text to screen
        message_to_screen('CREDIT', Color_Option_D,fontE,290,0) # add text to screen
        
        pygame.draw.rect(windowDisplay, white, [(display_width/2) - SYpos,SXpos,10,10]) # Draw the rectangle in this case the selector
        
        
        pygame.display.update() # Update window

        for event in pygame.event.get(): #get every event name and type
            print(event) # print events in the IDLE (For developing use)

            if event.type == pygame.QUIT: # if the event type is equal to the X button (QUIT)
                pygame.quit() #Quit window
                quit() # Terminate window
            if event.type == pygame.KEYDOWN: # if event type is pressed key
                if event.key == pygame.K_DOWN: # if key is Down arrow
                    if Selection == 'start': # if Selection is start do the following
                        Color_Option_A = red #Change colour of START text to red
                        SXpos = 225 #Change x position of rectangle
                        SYpos = 110 # change y position of rectangle
                        Color_Option_B = white # Change colour of INSTRUCTIONS to white
                        Selection = 'second' # Set selector to be equal to second option
                    elif Selection == 'second': #if selector is equal to second
                        Color_Option_B = red #change INSTRUCTION text colour to red
                        SXpos = 255 #Change x position of rectangle
                        SYpos = 75 #Change y position of rectangle
                        Color_Option_C = white #Change SETTINGS text to white
                        Selection = 'third' # Set selector to be equal to third option
                    elif Selection == 'third': #if selector is equal to third
                        Color_Option_C = red #Change SETTINGS text to red
                        SXpos = 285 #Change x position of rectangle
                        SYpos = 60 #Change y position of rectangle
                        Color_Option_D = white #change CREDITS text to white
                        Selection = 'fourth' # Set selector to be equal to fourth option
                # When KEY is UP #
                if event.key == pygame.K_UP: # if key is Up arrow
                    if Selection == 'second': #if selector is equal to second
                        Color_Option_B = red #Change INSTRUCTIONS text to red
                        SXpos = 192 #Change x position of rectangle
                        SYpos = 55 #Change y position of rectangle
                        Color_Option_A = white #Change START text to white
                        Selection = 'start' #change selector to third option
                    elif Selection == 'third': # if selector is third option then
                        Color_Option_C = red #change SETTINGS red colour to red
                        SXpos = 225 #Change x position of rectangle
                        SYpos = 110 #Change y position of rectangle
                        Color_Option_B = white #change INSTRUCTIONS text colour to red
                        Selection = 'second' # set selector to fourth option
                    elif Selection == 'fourth': # if selector is fourth option
                        Color_Option_D = red #change the CREDITS text colour to red
                        SXpos = 255 #Change x position of rectangle
                        SYpos = 75 #Change y position of rectangle
                        Color_Option_C = white #change the SETTINGS text to white
                        Selection = 'third' # change the selector option to fourth
                if event.key == pygame.K_RETURN: # if key pressed is the enter key
                    if Selection == 'third': # if selector is third
                        MenuChange = True #chnage state of menuChange to True to terminate this loop
                        SettingsLoop() #call the SettingsLoop function
                    if Selection == 'fourth': # if selector is fourth
                        MenuChange = True #chnage state of menuChange to True to terminate this loop
                        CreditsLoop() #call the CreditsLoop function
                        
                        

def SettingsLoop():
    global SSXpos, SSYpos,SSXpos2, SSYpos2, SColor_Option_A ,SColor_Option_B,BlueNum,RedNum,SSelection
    MenuChange = False
    while not MenuChange:
        windowDisplay.fill(black)
        if BlueNum < 10:
            message_to_screen('Blue Team   0' + str(BlueNum) + '   ', red,fontE,250,0)
        else:
            message_to_screen('Blue Team   ' + str(BlueNum) + '   ', red,fontE,250,0)
        if RedNum < 10:
            message_to_screen('Red Team   0' + str(RedNum) + '   ', red,fontE,280,0)
        else:
            message_to_screen('Red Team   ' + str(RedNum) + '   ', red,fontE,280,0)
        pygame.draw.rect(windowDisplay, white, [(display_width/2) - SSXpos,SSYpos,10,10])
        pygame.draw.rect(windowDisplay, white, [(display_width/2) - SSXpos2,SSYpos2,10,10])
        pygame.display.update()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MenuChange = True
                    SXpos = 192
                    SYpos = 55
                    Color_Option_A = white
                    Color_Option_C = red
                    Selection = 'start'
                    # reset settings menu #
                    SSYpos = 245
                    SSXpos = -33
                    SSYpos2 = 245
                    SSelection = 'start'
                    # end reset #
                    MenuLoop()
                if event.key == pygame.K_DOWN:
                    if SSelection == 'start':
                        SSYpos = 275
                        SSXpos = -30
                        SSYpos2 = 275
                        SSelection = 'second'
                if event.key == pygame.K_UP:
                    if SSelection == 'second':
                        SSYpos = 245
                        SSXpos = -33
                        SSYpos2 = 245
                        SSelection = 'start'
                if event.key == pygame.K_LEFT:
                    if SSelection == 'start':
                        if BlueNum > 1:    
                            BlueNum -= 1
                    elif SSelection == 'second':
                        if RedNum > 1:
                            RedNum -= 1
                if event.key == pygame.K_RIGHT:
                    if SSelection == 'start':
                        if BlueNum < 20:    
                            BlueNum += 1
                    elif SSelection == 'second':
                        if RedNum < 20:
                            RedNum += 1

 
                        
def CreditsLoop():
    global SXpos, SYpos, Selection, Color_Option_A ,Color_Option_D
    MenuChange = False
    while not MenuChange:
        windowDisplay.fill(black)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MenuChange = True
                    SXpos = 192
                    SYpos = 55
                    Color_Option_A = white
                    Color_Option_D = red
                    Selection = 'start'
                    MenuLoop()

        
MenuLoop()

