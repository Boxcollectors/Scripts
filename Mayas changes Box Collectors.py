# All imports here #
import pygame
import time
from time import sleep
import random
import pickle
# End Imports      #

# Initialization of Window #
pygame.init()


#settings load#

SettingsFile = open('BCSettings.txt','rb')
SettingsDict = pickle.load(SettingsFile)
SettingsFile.close()

#end of settings load#



# Sounds load #

MoveSound = pygame.mixer.Sound('Sounds/move.wav') #Loads the sound in the system
SelectSound = pygame.mixer.Sound('Sounds/select.wav')#Loads the sound in the system
pygame.mixer.music.load('Sounds/Credits.mp3')#Loads the sound in the system
LogoImg = pygame.image.load('Graphics/Logo.png')#Loads the image in the system
LogoP2Img = pygame.image.load('Graphics/LogoP2.png')#Loads the image in the system
BlueManImg = pygame.image.load('Graphics/BlueMan.png')#Loads the image in the system
RedManImg = pygame.image.load('Graphics/RedMan.png')#Loads the image in the system
#end of sounds load #

#Image load#

LogoImg = pygame.image.load('Graphics/Logo.png')#Loads the image in the system
LogoP2Img = pygame.image.load('Graphics/LogoP2.png')#Loads the image in the system
BlueManImg = pygame.image.load('Graphics/BlueMan.png')#Loads the image in the system
RedManImg = pygame.image.load('Graphics/RedMan.png')#Loads the image in the system
#end of sounds load #

#finish loading images#

#defining colours#
white = (255,255,255) #argb value of white
black = (0,0,0) #argb value of black
red = (255,0,0) #argb value of red
green = (0,155,0) #argb value of green
#end of defining colours#

#setting the pixels for the window#
display_width = 900 #setting width to 900 pixels
display_height = 600 #setting height to 600 pixels
#end of setting pixels#

#Start loop definitions#
ShowInstruction = True #setting bool ShowInstructions to True
StartTimer = False#Setting bool StartTimer to False
B1X = 10 #setting B1X cord to 10
B1Y = 90 #setting B1Y cord to 90
B2X = 10#Set B2X variable to 10
B2Y = 160#Set B2Y variable to 160
B3X = 10#Set B3X variable to 10
B3Y = 230#Set B3Y variable to 230
B4X = 10#Set B4X variable to 10
B4Y = 300#Set B4Y variable to 300
B5X = 10#Set B5X variable to 10
B5Y = 370#Set B5Y variable to 370
B6X = 10#Set B6X variable to 10
B6Y = 440#Set B6Y variable to 440
B7X = 10#Set B7X variable to 10
B7Y = 510#Set B7Y variable to 510


R1X = 820
R1Y = 90
#end start loop definitions#

# Main menu #

SXpos = 192 #setting SXpos cord to 192
SYpos = 55 #setting SYpos to 55
Selection = 'start' #setting selection variable to start
Color_Option_A = white #setting color A to white
Color_Option_B = red #setting color B to red
Color_Option_C = red #setting color C to red
Color_Option_D = red #setting color D to red 
# End Main Menu #

# Settings Menu #
SSXpos = -33 #setting SSXpos to -33
SSYpos = 245 #setting SSYpos to 245
SSXpos2 = -75 #Setting SSXpos2 to -75
SSYpos2 = 245 #setting SSYpos2 to 245
SColor_Option_A = red #setting Scolor A to red
SColor_Option_B = red #setting Scolor B to red
BlueNum = int(SettingsDict['BlueNumS'])  #setting blue num variable to 7
RedNum = int(SettingsDict['RedNumS']) #setting blue num variable to 7
TimeNum = int(SettingsDict['TimeNumS']) #setting time num variable to 40 (minimum 40 for best performance)
SSelection = 'start' #setting SSelection variable to start
# End Settings Menu#

# credits menu #
CYpos = 600 #Setting CYpos to 600 (pixels)
# end credits menu#

windowDisplay = pygame.display.set_mode((display_width,display_height)) #initializes the window
pygame.display.set_caption('Box Collectors') #changes the title of the window

# End of initialization of window #

# Clock initialization(FPS) #
clock = pygame.time.Clock() #initializes the clock value which ticks in FPS(frames per second)
FPS = 15 #set the FPS variable to 15
# End of clock initialization(FPS) #

# Initialization of font #
fontA = pygame.font.SysFont(None,14)#setting fontA to size 14
fontB = pygame.font.SysFont(None,18)#setting fontB to size 18
fontC = pygame.font.SysFont(None,20)#setting fontC to size 20
fontD = pygame.font.SysFont(None,25)#setting fontD to size 25
fontE = pygame.font.SysFont(None,34)#setting fontE to size 34
# End Initialization of font #



#Save settings#

def Save():
    SettingsDict = {'BlueNumS':str(BlueNum),'RedNumS':str(RedNum),'TimeNumS':str(TimeNum)}
    SettingsFile = open('BCSettings.txt','wb')
    pickle.dump(SettingsDict,SettingsFile)
    SettingsFile.close()
# Calculation of area of text # 
def text_objects(text,color,FontName): #function to calculate area arround text
    textSurface = FontName.render(text,True,color)#renders the shape around text(Rect)
    return textSurface, textSurface.get_rect()#returns the surface area of rect
# End of calculation of area of text #

# Message Function #
def message_to_screen(msg,color,FontName,pos,Backwards):#function to initialize text
    textSurf, textRect = text_objects(msg,color,FontName)#gets the message of text
    # color and the font size(FontName)
    textRect.center = ((display_width/2)- Backwards),(pos)#centers text on screen
    windowDisplay.blit(textSurf,textRect)#blits the text on screen(similar to images)
# End Message Function #

def MenuLoop():
    # define global variables #
    global CYpos
    global SXpos, SYpos, Selection, Color_Option_A ,Color_Option_B,Color_Option_C,Color_Option_D
    # end define #
    
    MenuChange = False # set menuchange to false

    while not MenuChange: # run loop until menuChange changes to true
        
        windowDisplay.fill(black) # change window colour to black
        windowDisplay.blit(LogoImg,(display_width/2 - 185,30))#blit the LogoImg
        windowDisplay.blit(LogoP2Img,(display_width/2 - 50,80))#blit the LogoP2Img
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
                    MoveSound.play() #play move sound file
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
                    MoveSound.play()# play move sound file
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
                    SelectSound.play() #play select sound file
                    time.sleep(0.1)
                    if Selection == 'start': # if selector is start
                        MenuChange = True #chnage state of menuChange to True to terminate this loop
                        StartLoop() #call the SettingsLoop function
                    if Selection == 'third': # if selector is third
                        MenuChange = True #chnage state of menuChange to True to terminate this loop
                        SettingsLoop() #call the SettingsLoop function
                    if Selection == 'fourth': # if selector is fourth
                        MenuChange = True #chnage state of menuChange to True to terminate this loop
                        CYpos = 600 # Setting the CYpos to 600
                        CreditsLoop() #call the CreditsLoop function

def FirstTimeInstructions():#MAYA
    MenuChange = False #setting menuchange bool to False

    while not MenuChange:#runs code while as long menuchange bool is false

        windowDisplay.fill(black)#fills window colour to black

        message_to_screen('To skip this window use the ESC button', green,fontE,20,0)#blit seconds to screen
        message_to_screen('To move between menu items use the UP and DOWN arrow keys', white,fontE,70,0)#blit seconds to screen
        message_to_screen('To edit a setting or other variable use the LEFT and RIGHT arrow keys', white,fontE,120,0)#blit seconds to screen
        message_to_screen('To to select an option use the ENTER key', white,fontE,170,0)#blit seconds to screen

        #if event.type == pygame_KEYDOWN:

            #if event.key == pygame.K_UP:
                # pygame.K_UP= True
                # message_to_screen('UP', red,fontE,300,0)
            #elif event.key == pygame.K_DOWN:
                # message_to_screen('DOWN', red,fontE,300,0)
            #elif event.key == pygame.K_LEFT:
                # message_to_screen('LEFT', red,fontE,300,0)
            #elif event.key == pygame.K_RIGHT:
                # message_to_screen('RIGHT', red,fontE,300,0)
          


        
        pygame.display.update()#update the window to display changes


        for event in pygame.event.get():#gets the events used by user
            print(event)#prints the events to the CLI (for development use)
            if event.type == pygame.QUIT:# if the user has pressed the x
                pygame.quit()#call the quit function
                quit()#terminate window
            if event.type == pygame.KEYDOWN:#if the event type is a when a key is pressed down
                
                if event.key == pygame.K_ESCAPE:#if the key type is the ESC key
                    MenuChange = True#set menu change bool to True
                    MenuLoop()#calls the start loop
    
                        
def StartLoop():#PADDY
    #defining global variables#
    global SXpos,SYpos, Color_Option_A,Color_Option_C,Selection
    global ShowInstruction,StartTimer,B1X,B1Y,B2X,B2Y,B3X,B3Y,B4X,B4Y
    global B1X,B1Y,B2X,B2Y,B3X,B3Y,B4X,B4Y,B5X,B5Y,B6X,B6Y,B7X,B7Y
    global R1X,R1Y,R2X,R2Y,R3X,R3Y,R4X,R4Y,R5X,R5Y,R6X,R6Y,R7X,R7Y
    #end of defining global variables#
    MenuChange = False #setting menuchange bool to False
    STimes = 0 #Setting STimes variable to 0
    GetDirectionX = 0 #setting GetDirectionX variable to 0
    GetDirectionY = 0 #setiing GetDirectionT variable to 0
    Seconds=TimeNum #Setting that the seconds variable is equal to the TimeNum


    
    
    while not MenuChange:#runs code while as long menuchange bool is false
        windowDisplay.fill(black)#fills window colour to black
        if BlueNum == 1:#if Blue num is equal to 1 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y)) #blit 1st man
        elif BlueNum == 2:#if Blue num is equal to 2 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
        elif BlueNum == 3:#if Blue num is equal to 3 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
            windowDisplay.blit(BlueManImg,(B3X,B3Y))#blit 3rd Blue man
        elif BlueNum == 4:#if Blue num is equal to 4 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
            windowDisplay.blit(BlueManImg,(B3X,B3Y))#blit 3rd Blue man
            windowDisplay.blit(BlueManImg,(B4X,B4Y))#blit 4th Blue man
        elif BlueNum == 5:#if Blue num is equal to 5 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
            windowDisplay.blit(BlueManImg,(B3X,B3Y))#blit 3rd Blue man
            windowDisplay.blit(BlueManImg,(B4X,B4Y))#blit 4th Blue man
            windowDisplay.blit(BlueManImg,(B5X,B5Y))#blit 5th Blue man
        elif BlueNum == 6:#if Blue num is equal to 6 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
            windowDisplay.blit(BlueManImg,(B3X,B3Y))#blit 3rd Blue man
            windowDisplay.blit(BlueManImg,(B4X,B4Y))#blit 4th Blue man
            windowDisplay.blit(BlueManImg,(B5X,B5Y))#blit 5th Blue man
            windowDisplay.blit(BlueManImg,(B6X,B6Y))#blit 6th Blue man
        elif BlueNum == 7:#if Blue num is equal to 7 then
            windowDisplay.blit(BlueManImg,(B1X,B1Y))#blit 1st Blue man
            windowDisplay.blit(BlueManImg,(B2X,B2Y))#blit 2nd Blue man
            windowDisplay.blit(BlueManImg,(B3X,B3Y))#blit 3rd Blue man
            windowDisplay.blit(BlueManImg,(B4X,B4Y))#blit 4th Blue man
            windowDisplay.blit(BlueManImg,(B5X,B5Y))#blit 5th Blue man
            windowDisplay.blit(BlueManImg,(B6X,B6Y))#blit 6th Blue man
            windowDisplay.blit(BlueManImg,(B7X,B7Y))#blit 7th Blue man


        if RedNum == 1:# if red num is equal to 1 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st man
        elif RedNum == 2:# if red num is equal to 2 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
        elif RedNum == 3:# if red num is equal to 3 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
            windowDisplay.blit(RedManImg,(820,230))#blit 3rd red man
        elif RedNum == 4:# if red num is equal to 4 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
            windowDisplay.blit(RedManImg,(820,230))#blit 3rd red man
            windowDisplay.blit(RedManImg,(820,300))#blit 4th red man
        elif RedNum == 5:# if red num is equal to 5 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
            windowDisplay.blit(RedManImg,(820,230))#blit 3rd red man
            windowDisplay.blit(RedManImg,(820,300))#blit 4th red man
            windowDisplay.blit(RedManImg,(820,370))#blit 5th red man
        elif RedNum == 6:# if red num is equal to 6 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
            windowDisplay.blit(RedManImg,(820,230))#blit 3rd red man
            windowDisplay.blit(RedManImg,(820,300))#blit 4th red man
            windowDisplay.blit(RedManImg,(820,370))#blit 5th red man 
            windowDisplay.blit(RedManImg,(820,440))#blit 6th red man
        elif RedNum == 7:# if red num is equal to 7 then
            windowDisplay.blit(RedManImg,(R1X,R1Y))#blit 1st red man
            windowDisplay.blit(RedManImg,(820,160))#blit 2nd red man
            windowDisplay.blit(RedManImg,(820,230))#blit 3rd red man
            windowDisplay.blit(RedManImg,(820,300))#blit 4th red man
            windowDisplay.blit(RedManImg,(820,370))#blit 5th red man 
            windowDisplay.blit(RedManImg,(820,440))#blit 6th red man
            windowDisplay.blit(RedManImg,(820,510))#blit 7th red man
        
        
        if ShowInstruction: #if the ShowInstruction variable is set to True then
            message_to_screen('PRESS S TO START', Color_Option_A,fontE,display_height/2,0) # blit text to screen
            pygame.draw.rect(windowDisplay, white, [80,0,10,600]) # Draw the rectangle in this case left line
            pygame.draw.rect(windowDisplay, white, [800,0,10,600])# Draw the rectangle in this case right line
        else:# for every other case
            pygame.draw.rect(windowDisplay, white, [5,5,890,40])#draw white box
            message_to_screen(str(Seconds), black,fontE,20,0)#blit seconds to scren
            
        pygame.display.update()#update the window to display changes
        for event in pygame.event.get():#gets the events used by user
            print(event)#prints the events to the CLI (for development use)
            if event.type == pygame.QUIT:# if the user has pressed the x
                pygame.quit()#call the quit function
                quit()#terminate window
            if event.type == pygame.KEYDOWN:#if the event type is a when a key is pressed down
                
                if event.key == pygame.K_ESCAPE:#if the key type is the ESC key
                    MenuChange = True#set menu change bool to True
                    
                    #reset menuLoop to initial state#
                    
                    SXpos = 192#set SXpos to 192 
                    SYpos = 55#set the SYpos to 55
                    Color_Option_A = white#set colour A to white
                    Color_Option_C = red#set colour C to red
                    Selection = 'start'#set selection variable to start

                    StartTimer = False#set StartTimer bool to False
                    ShowInstruction = True#Set ShowInstructions bool to True
                    Seconds = TimeNum#Set the seconds variable to the value of the TimeNum variable
                    B1X = 10#Set B1X variable to 10
                    B1Y = 90#Set B1Y variable to 90
                    B2X = 10#Set B2X variable to 10
                    B2Y = 160#Set B2Y variable to 160
                    B3X = 10#Set B3X variable to 10
                    B3Y = 230#Set B3Y variable to 230
                    B4X = 10#Set B4X variable to 10
                    B4Y = 300#Set B4Y variable to 300
                    B5X = 10#Set B5X variable to 10
                    B5Y = 370#Set B5Y variable to 370
                    B6X = 10#Set B6X variable to 10
                    B6Y = 440#Set B6Y variable to 440
                    B7X = 10#Set B7X variable to 10
                    B7Y = 510#Set B7Y variable to 510

                    R1X = 820#Set R1X variable to 820
                    R1Y = 90#Set R1Y variable to 90

                    
                    
                    #end of reset of menu loop#
                    
                    MenuLoop()#call the MenuLopp
                if event.key == pygame.K_s:#if key type is the S key then
                    if ShowInstruction: #If ShowInstruction is equal to True then
                        ShowInstruction = False#set ShowInstruction bool to False
                        StartTimer = True#Set startTimer bool to True
                        
        if StartTimer: #if startTimer bool is true then
            MovementListX = ['LEFT','RIGHT']#MovementListX is a list with 2 values
            MovementListY = ['UP','DOWN']#MovementListY is a list with 2 values
            GetDirectionX = random.choice(MovementListX)#Set GetDirectionX variable to random value from list MovementListX
            GetDirectionY = random.choice(MovementListY) #Set GetDirectionY variable to random value from list MovementListY

            GetDirectionX2 = random.choice(MovementListX)#Set GetDirectionX2 variable to random value from list MovementListX
            GetDirectionY2 = random.choice(MovementListY) #Set GetDirectionY2 variable to random value from list MovementListY

            GetDirectionX3 = random.choice(MovementListX)#Set GetDirectionX3 variable to random value from list MovementListX
            GetDirectionY3 = random.choice(MovementListY) #Set GetDirectionY3 variable to random value from list MovementListY

            GetDirectionX4 = random.choice(MovementListX)#Set GetDirectionX4 variable to random value from list MovementListX
            GetDirectionY4 = random.choice(MovementListY) #Set GetDirectionY4 variable to random value from list MovementListY

            GetDirectionX5 = random.choice(MovementListX)#Set GetDirectionX5 variable to random value from list MovementListX
            GetDirectionY5 = random.choice(MovementListY) #Set GetDirectionY5 variable to random value from list MovementListY

            GetDirectionX6 = random.choice(MovementListX)#Set GetDirectionX6 variable to random value from list MovementListX
            GetDirectionY6 = random.choice(MovementListY) #Set GetDirectionY6 variable to random value from list MovementListY

            GetDirectionX7 = random.choice(MovementListX)#Set GetDirectionX7 variable to random value from list MovementListX
            GetDirectionY7 = random.choice(MovementListY) #Set GetDirectionY7 variable to random value from list MovementListY


            #RED MAN
                        
            GetDirectionX8 = random.choice(MovementListX)#Set GetDirectionX8 variable to random value from list MovementListX
            GetDirectionY8 = random.choice(MovementListY) #Set GetDirectionY8 variable to random value from list MovementListY

            GetDirectionX9 = random.choice(MovementListX)#Set GetDirectionX9 variable to random value from list MovementListX
            GetDirectionY9 = random.choice(MovementListY) #Set GetDirectionY9 variable to random value from list MovementListY

            GetDirectionX10 = random.choice(MovementListX)#Set GetDirectionX10 variable to random value from list MovementListX
            GetDirectionY10 = random.choice(MovementListY) #Set GetDirectionY10 variable to random value from list MovementListY

            GetDirectionX11 = random.choice(MovementListX)#Set GetDirectionX11 variable to random value from list MovementListX
            GetDirectionY11 = random.choice(MovementListY) #Set GetDirectionY11 variable to random value from list MovementListY

            GetDirectionX12 = random.choice(MovementListX)#Set GetDirectionX12 variable to random value from list MovementListX
            GetDirectionY12 = random.choice(MovementListY) #Set GetDirectionY12 variable to random value from list MovementListY

            GetDirectionX13 = random.choice(MovementListX)#Set GetDirectionX13 variable to random value from list MovementListX
            GetDirectionY13 = random.choice(MovementListY) #Set GetDirectionY13 variable to random value from list MovementListY

            GetDirectionX14 = random.choice(MovementListX)#Set GetDirectionX14 variable to random value from list MovementListX
            GetDirectionY14 = random.choice(MovementListY) #Set GetDirectionY14 variable to random value from list MovementListY

            

            if B1X <= 0:#if B1X is less or equal to 0 then
                GetDirectionX = 'RIGHT' #set GetDirectionX variable to RIGHT
            elif B1X >= 840:#if B1X is bigger or equal to 840 then
                GetDirectionX = 'LEFT'#set GetDirectionX variable to LEFT
            if B1Y <= 50:#if B1Y is less or equal to 50 then 
                B1Y = 100#set B1Y to 100 
            elif B1Y >= 540:#if B1Y is more or equal to 540 then 
                B1Y = 500#set B1Y to 500
            if GetDirectionX == 'LEFT':#if GetDirectionX variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B1X -= 3#get B1X value and subtract 3 from it then set it as the new value
            elif GetDirectionX == 'RIGHT':#if GetDirectionX variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B1X += 3#get B1X value and add 3 from it then set it as the new value
            if GetDirectionY == 'UP':#if GetDirectionY variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B1Y -= 3#get B1Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY == 'DOWN':#if GetDirectionY variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B1Y += 3 #get B1Y value and add 3 from it then set it as the new value


            if B2X <= 0:#if B2X is less or equal to 0 then
                GetDirectionX2 = 'RIGHT' #set GetDirectionX2 variable to RIGHT
            elif B2X >= 840:#if B2X is bigger or equal to 840 then
                GetDirectionX2 = 'LEFT'#set GetDirectionX2 variable to LEFT
            if B2Y <= 50:#if B2Y is less or equal to 50 then 
                B2Y = 100#set B2Y to 100 
            elif B2Y >= 540:#if B2Y is more or equal to 540 then 
                B2Y = 500#set B2Y to 500
            if GetDirectionX2 == 'LEFT':#if GetDirectionX2 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B2X -= 3#get B2X value and subtract 3 from it then set it as the new value
            elif GetDirectionX2 == 'RIGHT':#if GetDirectionX2 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B2X += 3#get B2X value and add 3 from it then set it as the new value
            if GetDirectionY2 == 'UP':#if GetDirectionY2 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B2Y -= 3#get B2Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY2 == 'DOWN':#if GetDirectionY2 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B2Y += 3 #get B2Y value and add 3 from it then set it as the new value


            if B3X <= 0:#if B3X is less or equal to 0 then
                GetDirectionX3 = 'RIGHT' #set GetDirectionX3 variable to RIGHT
            elif B3X >= 840:#if B3X is bigger or equal to 840 then
                GetDirectionX3 = 'LEFT'#set GetDirectionX3 variable to LEFT
            if B3Y <= 50:#if B3Y is less or equal to 50 then 
                B3Y = 100#set B3Y to 100 
            elif B3Y >= 540:#if B3Y is more or equal to 540 then 
                B3Y = 500#set B3Y to 500
            if GetDirectionX3 == 'LEFT':#if GetDirectionX3 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B3X -= 3#get B3X value and subtract 3 from it then set it as the new value
            elif GetDirectionX3 == 'RIGHT':#if GetDirectionX3 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B3X += 3#get B3X value and add 3 from it then set it as the new value
            if GetDirectionY3 == 'UP':#if GetDirectionY3 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B3Y -= 3#get B3Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY3 == 'DOWN':#if GetDirectionY3 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B3Y += 3 #get B3Y value and add 3 from it then set it as the new value


            if B4X <= 0:#if B4X is less or equal to 0 then
                GetDirectionX4 = 'RIGHT' #set GetDirectionX4 variable to RIGHT
            elif B4X >= 840:#if B4X is bigger or equal to 840 then
                GetDirectionX4 = 'LEFT'#set GetDirectionX4 variable to LEFT
            if B4Y <= 50:#if B4Y is less or equal to 50 then 
                B4Y = 100#set B4Y to 100 
            elif B4Y >= 540:#if B4Y is more or equal to 540 then 
                B4Y = 500#set B4Y to 500
            if GetDirectionX4 == 'LEFT':#if GetDirectionX4 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B4X -= 3#get B4X value and subtract 3 from it then set it as the new value
            elif GetDirectionX4 == 'RIGHT':#if GetDirectionX4 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B4X += 3#get B4X value and add 3 from it then set it as the new value
            if GetDirectionY4 == 'UP':#if GetDirectionY4 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B4Y -= 3#get B4Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY4 == 'DOWN':#if GetDirectionY4 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B4Y += 3 #get B4Y value and add 3 from it then set it as the new value


            if B5X <= 0:#if B5X is less or equal to 0 then
                GetDirectionX5 = 'RIGHT' #set GetDirectionX5 variable to RIGHT
            elif B5X >= 840:#if B5X is bigger or equal to 840 then
                GetDirectionX5 = 'LEFT'#set GetDirectionX5 variable to LEFT
            if B5Y <= 50:#if B5Y is less or equal to 50 then 
                B5Y = 100#set B5Y to 100 
            elif B5Y >= 540:#if B5Y is more or equal to 540 then 
                B5Y = 500#set B5Y to 500
            if GetDirectionX5 == 'LEFT':#if GetDirectionX5 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B5X -= 3#get B5X value and subtract 3 from it then set it as the new value
            elif GetDirectionX5 == 'RIGHT':#if GetDirectionX5 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B5X += 3#get B5X value and add 3 from it then set it as the new value
            if GetDirectionY5 == 'UP':#if GetDirectionY5 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B5Y -= 3#get B5Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY5 == 'DOWN':#if GetDirectionY5 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B5Y += 3 #get B5Y value and add 3 from it then set it as the new value


            if B6X <= 0:#if B6X is less or equal to 0 then
                GetDirectionX6 = 'RIGHT' #set GetDirectionX6 variable to RIGHT
            elif B6X >= 840:#if B6X is bigger or equal to 840 then
                GetDirectionX6 = 'LEFT'#set GetDirectionX6 variable to LEFT
            if B6Y <= 50:#if B6Y is less or equal to 50 then 
                B6Y = 100#set B6Y to 100 
            elif B6Y >= 540:#if B6Y is more or equal to 540 then 
                B6Y = 500#set B6Y to 500
            if GetDirectionX6 == 'LEFT':#if GetDirectionX6 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B6X -= 3#get B6X value and subtract 3 from it then set it as the new value
            elif GetDirectionX6 == 'RIGHT':#if GetDirectionX6 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B6X += 3#get B6X value and add 3 from it then set it as the new value
            if GetDirectionY6 == 'UP':#if GetDirectionY6 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B6Y -= 3#get B6Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY6 == 'DOWN':#if GetDirectionY6 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B6Y += 3 #get B6Y value and add 3 from it then set it as the new value


            if B7X <= 0:#if B7X is less or equal to 0 then
                GetDirectionX7 = 'RIGHT' #set GetDirectionX7 variable to RIGHT
            elif B7X >= 840:#if B7X is bigger or equal to 840 then
                GetDirectionX7 = 'LEFT'#set GetDirectionX7 variable to LEFT
            if B7Y <= 50:#if B7Y is less or equal to 50 then 
                B7Y = 100#set B7Y to 100 
            elif B7Y >= 540:#if B7Y is more or equal to 540 then 
                B7Y = 500#set B7Y to 500
            if GetDirectionX7 == 'LEFT':#if GetDirectionX7 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    B7X -= 3#get B7X value and subtract 3 from it then set it as the new value
            elif GetDirectionX7 == 'RIGHT':#if GetDirectionX7 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    B7X += 3#get B7X value and add 3 from it then set it as the new value
            if GetDirectionY7 == 'UP':#if GetDirectionY7 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    B7Y -= 3#get B7Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY7 == 'DOWN':#if GetDirectionY7 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    B7Y += 3 #get B7Y value and add 3 from it then set it as the new value



            #RED MAN

            if R1X <= 0:#if R1X is less or equal to 0 then
                GetDirectionX8 = 'RIGHT' #set GetDirectionX8 variable to RIGHT
            elif R1X >= 840:#if R1X is bigger or equal to 840 then
                GetDirectionX8 = 'LEFT'#set GetDirectionX8 variable to LEFT
            if R1Y <= 50:#if R1Y is less or equal to 50 then 
                R1Y = 100#set R1Y to 100 
            elif R1Y >= 540:#if R1Y is more or equal to 540 then 
                R1Y = 500#set R1Y to 500
            if GetDirectionX8 == 'LEFT':#if GetDirectionX8 variable it equal to LEFT then
                for i in range(8):#Repeat for 8 times
                    R1X -= 3#get R1X value and subtract 3 from it then set it as the new value
            elif GetDirectionX8 == 'RIGHT':#if GetDirectionX8 variable it equal to RIGHT then
                for i in range(8):#Repeat for 8 times
                    R1X += 3#get R1X value and add 3 from it then set it as the new value
            if GetDirectionY8 == 'UP':#if GetDirectionY8 variable it equal to UP then
                for i in range(8):#Repeat for 8 times
                    R1Y -= 3#get R1Y value and subtract 3 from it then set it as the new value
            elif GetDirectionY8 == 'DOWN':#if GetDirectionY8 variable it equal to DOWN then
                for i in range(16):#repeat for 16 times
                    R1Y += 3 #get R1Y value and add 3 from it then set it as the new value

             
        if StartTimer:#if StartTimer bool is True
            if Seconds > 0:#if seconds variable is more than 0 then
                if STimes == 17:#if STimes is equal to 17 then
                    Seconds -= 1#Get the value of seconds subtract 1 and set it as the new value
                    STimes = 0#set STimes variable to 0
                clock.tick(15)#Tick with 15 FPS
                STimes += 1 #Get the value of STimes add 1 and set it as the new value
                if Seconds == 0:#if seconds variable is equal to 0
                    StartTimer = False#set StartTimer bool to False
                    ShowInstruction = True#Set ShowInstructions bool to True
                    Seconds = TimeNum#Set the seconds variable to the value of the TimeNum variable
                    B1X = 10#Set B1X variable to 10
                    B1Y = 90#Set B1Y variable to 90
                    B2X = 10#Set B2X variable to 10
                    B2Y = 160#Set B2Y variable to 160
                    B3X = 10#Set B3X variable to 10
                    B3Y = 230#Set B3Y variable to 230
                    B4X = 10#Set B4X variable to 10
                    B4Y = 300#Set B4Y variable to 300
                    B5X = 10#Set B5X variable to 10
                    B5Y = 370#Set B5Y variable to 370
                    B6X = 10#Set B6X variable to 10
                    B6Y = 440#Set B6Y variable to 440
                    B7X = 10#Set B7X variable to 10
                    B7Y = 510#Set B7Y variable to 510

                    R1X = 820#Set R1X variable to 820
                    R1Y = 90#Set R1Y variable to 90
                    
                             

def SettingsLoop():#ASHWIN
    # define global variables#
    global SXpos,SYpos,SSXpos, SSYpos,SSXpos2, SSYpos2
    global Color_Option_A,Color_Option_C,BlueNum,RedNum,TimeNum ,SSelection,Selection
    #end of global variable defining#
    MenuChange = False# set the ManuChange bool to False
    
    while not MenuChange:#Repeat loop untill MenuChange bool is True
        windowDisplay.fill(black)#fill window with the color black
        
        message_to_screen('Blue Team   0' + str(BlueNum) + '   ', red,fontE,250,0)#blit text to window

        message_to_screen('Red Team    0' + str(RedNum) + '   ', red,fontE,280,0)#blit text to window
        if TimeNum < 10:#if TimeNum is les than 10 then
            message_to_screen('     Time       0' + str(TimeNum) + '   ', red,fontE,310,0)#blit text to window
        else:#for any other case
            message_to_screen('     Time        ' + str(TimeNum) + '   ', red,fontE,310,0)#blit text to window

        pygame.draw.rect(windowDisplay, white, [(display_width/2) - SSXpos,SSYpos,10,10])#Blit rect in this case Selector 1
        pygame.draw.rect(windowDisplay, white, [(display_width/2) - SSXpos2,SSYpos2,10,10])#Blit rect in this case Selector 2
        pygame.display.update()#Update Window to display changes
        for event in pygame.event.get():#get events from the user
            print(event)#print events to CLI used by the user
            if event.type == pygame.QUIT:#if user presses the X to close the window
                Save()
                pygame.quit()#call the pygame quit function
                quit()#quit CLI
                
            if event.type == pygame.KEYDOWN:#if the event type is a key pressed down then 
                if event.key == pygame.K_ESCAPE:#if the key type is the ESC button then
                    MenuChange = True#change ManuChange bool to True

                    # reset the Main menu#
                    SXpos = 192 #set SXpos to 192
                    SYpos = 55 #Set SYpos to 55
                    Color_Option_A = white #set color A to white
                    Color_Option_C = red # set Color C to red
                    Selection = 'start'# set selection variable to start
                    #end of Main Menu reset
                    # reset settings menu #
                    SSYpos = 245#set SSYpos to 245
                    SSXpos = -33#set SSXpos to -33
                    SSYpos2 = 245#Set SSYpos2 to 245
                    SSelection = 'start'
                    Save()
                    # end reset #
                    MenuLoop()#call MenuLoop function
                if event.key == pygame.K_DOWN:#if Key pressed is the down arrow
                    MoveSound.play() #play move sound file
                    time.sleep(0.1)#delay code for 0.1 second
                    if SSelection == 'start':#If SSelection variable is equal to start
                        SSYpos = 275#set SSYpos to 275
                        SSXpos = -30#set SSXpos to -30
                        SSYpos2 = 275#set SSYpos2 to 275
                        SSelection = 'second'#set the SSelection variable to second
                    elif SSelection == 'second':#if SSelection variable is equal to second
                        SSYpos = 305#set SSYpos to 305
                        SSXpos = -30#set SSXpos to -30
                        SSYpos2 = 305#set SSYpos2 to 305
                        SSelection = 'third'#set the SSelection Variable to third
                if event.key == pygame.K_UP:#if Key pressed is the UP arrow
                    MoveSound.play() #play move sound file
                    time.sleep(0.1)#delay code for 0.1 second
                    if SSelection == 'second':#if SSelection variable is equal to second
                        SSYpos = 245#set SSYpos to 245
                        SSXpos = -33#set SSXpos to -33
                        SSYpos2 = 245#set SSYpos2 to 245
                        SSelection = 'start'#set the SSelection variable to start
                    elif SSelection == 'third':#If SSelection variable is equal to third
                        SSYpos = 275#set SSYpos to 275
                        SSXpos = -30#set SSXpos to -30
                        SSYpos2 = 275#set SSYpos2 to 275
                        SSelection = 'second'#set the SSelection variable to second
                if event.key == pygame.K_LEFT:#if key pressed is equal to the LEFT arrow then
                    MoveSound.play() #play move sound file
                    time.sleep(0.1)#delay code for 0.1 second
                    if SSelection == 'start':#if SSelection variable is equal to start
                        if BlueNum > 1:#if BlueNum variable is greater than 1 then   
                            BlueNum -= 1#get the value of the The BlueNum variable subtract 1 and set it to the new value
                    elif SSelection == 'second':#if SSelection variable is equal to second
                        if RedNum > 1:#if RedNum variable is greater than 1 then 
                            RedNum -= 1#get the value of the The RedNum variable subtract 1 and set it to the new value
                    elif SSelection == 'third':#if SSelection variable is equal to third
                        if TimeNum > 20:#if TimeNum variable is greater than 21 then 
                            TimeNum -= 1#get the value of the The TimeNum variable subtract 1 and set it to the new value
                if event.key == pygame.K_RIGHT:#if key pressed is equal to the RIGHT arrow then
                    MoveSound.play() #play move sound file
                    time.sleep(0.1)#delay code for 0.1 second
                    if SSelection == 'start':#if SSelection variable is equal to start
                        if BlueNum < 7:#if BlueNum variable is less than 7 then
                            BlueNum += 1#get the value of the The RedNum variable add 1 and set it to the new value
                    elif SSelection == 'second':#if SSelection variable is equal to second
                        if RedNum < 7:#if RedNum variable is less than 7 then
                            RedNum += 1#get the value of the The RedNum variable add 1 and set it to the new value
                    elif SSelection == 'third':#if SSelection variable is equal to third
                        if TimeNum < 99:#if TimeNum variable is less than 99 then 
                            TimeNum += 1#get the value of the The TimeNum variable add 1 and set it to the new value

 
                        
def CreditsLoop():#ADRIAN
    #define global variable#
    global CYpos, SXpos, SYpos, Selection, Color_Option_A ,Color_Option_D
    #end of defining global variables#
    MenuChange = False#set MenuChange bool to False
    MovementDelay = 3 #set MovementDelay variable to 3

    pygame.mixer.music.play(-1)#play music for ever(-1)
    
    while not MenuChange:
        windowDisplay.fill(black)
        message_to_screen('Team Members', white,fontE,CYpos,0)#blit text
        message_to_screen('Panayiotis Paschalides', red,fontD,CYpos + 30,0)#blit text with space 30 from previous text
        message_to_screen('Adrian Raszkiewicz', red,fontD,CYpos + 60,0)#blit text with space 30 from previous text
        message_to_screen('Maya Tulsi Patel', red,fontD,CYpos + 90,0)#blit text with space 30 from previous text
        message_to_screen('Pranav Parmar', red,fontD,CYpos + 120,0)#blit text with space 30 from previous text
        message_to_screen('Ashwin Ravichandran', red,fontD,CYpos + 150,0)#blit text with space 30 from previous text
        message_to_screen('test', red,fontD,CYpos + 180,0)#blit text with space 30 from previous text
        
        CYpos -= MovementDelay#get the value from the CYpos variable subtract MovementDelay Value(3) from it then set it as the new value
        time.sleep(0.05)#delay code for 0.05 seconds
        pygame.display.update()#update window to display changes
        if CYpos == -180: #if CYpos variable is equal to -150
            MenuChange = True #set MenuChange bool to True

            #reset the Main menu#
            SXpos = 192 #set SXpos variable to 192
            SYpos = 55#set SYpos Variable to 55
            Color_Option_A = white#set color A to white
            Color_Option_D = red#set color D to red
            Selection = 'start'#set Selection variable to start
            #end of reset#
            
            pygame.mixer.music.stop()#stop playing the music
            MenuLoop()#call the MenuLoop function
        for event in pygame.event.get():#get events from users input
            print(event)#print the events to the CLI(for development reasons)
            if event.type == pygame.QUIT:#if the user presses the X to close the window
                pygame.quit()#call the pygame quit function to terminate window
                quit()#quit the CLI
            if event.type == pygame.KEYDOWN:#if event type is key pressed then
                if event.key == pygame.K_ESCAPE:#if key type is the ESC button then
                    MenuChange = True #set MenuChange bool to True

                    #reset the Main menu#
                    SXpos = 192 #set SXpos variable to 192
                    SYpos = 55#set SYpos Variable to 55
                    Color_Option_A = white#set color A to white
                    Color_Option_D = red#set color D to red
                    Selection = 'start'#set Selection variable to start
                    #end of reset#
                    
                    pygame.mixer.music.stop()#stop playing the music
                    MenuLoop()#call the MenuLoop function

        
FirstTimeInstructions()#Call First Time Insturctions function to start the program

