#Snake Program <==Character Walk PRogram 
#1.0Key controls on a rectangle
#2.0 items appear and dissappear when collected
#3.0 Snake gets longer as items are eaten
#4.0 Enemies move towards snake
#4.1 Enemies movement tweak (random if not in range)
#5.0 Periodic boundary conditions, hit detection on body and tail
#Errors: not detecting tail length <1 (game states needed), need periodic boundary conditions
#6.0 Game states implemented, added enemies play zone defence to prevent clustering
#7.0 Sounds using minim
# (16.5/22)
# (    12 /12)
# Critical Requirements 
# ++++On Time
# +Program has player controlled by keys
# +Enemy chases player
# +Player can pick up items
# +-Multiple types of items (Points, time, health) 
# +Some kind of end states are reached
# ++Documentation and proper header
# +Progression

# 4.5/10(any combrination of 10) Optional requirements
# +PVectors
# +Sounds
# -Background music
# -Pause
# -Mute sounds
# ~Start screen
# -Variety of enemies
# -Variety of items
# -Animation
# -PImage array
# -Bonuses
# -Upgrades
# ++**Magical items of an impressive quality 
# Tail of snake gets larger from eating food
# AI prevents clustering

def setup():
    
    size(800,800)
    rectMode(CENTER)
    stroke(200,50,100)
    strokeWeight(5)
    
    #minim Instances
  #  minim_bg = Minim()
  #  minim_eating = Minim
  #  minim_attacked = Minim 
    initialize()

#from brick example
#bPos = []
#bSize = PVector (40,20)
#game constants++++++++++++++++++++++++++++
state = 0#game state
            
def initialize():
    global pPos, pSize, ePos, eSize, speed, score, numItems
    global iBool, iPos, iSize, numEnemies , eHome, eBool, eSpeed

    #item variables++++++++++++++++++++++++++
    numItems = 20
    iPos = []
    iSize = []
    iBool = []
    
    #Enemy variables ++++++++++++++++++++++++
    
    numEnemies = 4
    ePos = []
    eHome = [] #used to prevent enemy clustering 
    eSize = []
    eBool = [] #not used currently
    eSpeed = 4
    
                                                                                                
    score = 0

    #player variables++++++++++++++++++++++++++
    pPos = []
    pSize = []
    pPos.append(PVector(400, 400))#player position
    pSize.append(PVector(40,40))#player size 
    speed = 5.0#player speed

    #set the item list
    for i in range(0,numItems):
        iPos.append(PVector(random(50,750),random(50,750)))#item position
        iSize.append(PVector(15,15))#item size
        iBool.append(False)

    #set the item list    
    for i in range (0,numEnemies):
        ePos.append(PVector(random(15,50),random(14,50)))#Enemy starting position
        eHome.append(PVector((i%2+0.5)*400,(i/2+0.5)*400))
      #  print eHome
        eSize.append(PVector(20,20))#enemy Size
        eBool.append(False)


        
                
                                

pVel = PVector()
pDir = PVector()
attack = 10.0
defence = 10.0

pCol = color(255,0,0)


iCol = color(50,150,200)
    
eCol = color(0,0,250)        




def resetBlocks():
    global iPos, iSize, iBool, numItems
    numItems = 20
    iPos = []
    iSize = []
    for i in range(0,numItems):
        iPos.append(PVector(random(50,750),random(50,750)))#player position
        iSize.append(PVector(15,15))

#iVel = PVector()
#iDir = PVector()

def addBrick():
    global bPos, bSize
    #calc the verical position using //
    vertPos = height - len(bPos)//(width//bSize.x)*bSize.y - bSize.y/2
    horPos = width - len(bPos)%(width//bSize.x)*bSize.x - bSize.y/2
    bPos.append(PVector(horPos, vertPos))
    # 
    #calc the bricks final position
    
    #Add the position vector to the list

def keyPressed():
    global pVel, pVelX, pVelY, pDir, state
    if state == 0:
        if key == ' ':
            state = 1
    elif state == 1:
   # print keyCode
        if (keyCode == UP):
            pVel.set(PVector(0,-1.))
        elif (keyCode == DOWN):
            pVel.set(PVector(0,1.))
        elif (keyCode == LEFT):
            pVel.set(PVector(-1.,0))
        elif (keyCode == RIGHT):
            pVel.set(PVector(1, 0))
        else:
            pVel.set(PVector(0, 0))
        if key== 'f':
            fire()
    elif state == 2:#end game state
        if key == ' ':
            
            initialize()
            state = 1 
        
def detectHit(p1,p2,s1,s2):
   # print p1, p2, s1, s2
    if abs(p1.x-p2.x)<(s1.x+s2.x)/2 and abs(p1.y-p2.y)<(s1.y+s2.y)/2:
        return True
    return False

#def keyReleased():
   # global pVelX, pVelY
    #if (keyCode == 40 or keyCode == 38):
    #    pVelY.set(0,0)
   # if (keyCode == LEFT or keyCode == RIGHT):
  #      pVelX.set(0,0)

def updatePos(pos, siz):
    #check periodic boundary conditions
    
    #
    #move backwards thru the array giving each body 
    #segment the position of the one close to the head
    
    for i in range(1 , len(pos)):
#        print i
        #we start at the end and the i value moves us toward the head
        pos[len(pos) -i ].set(pos[len(pos) -i-1].x, pos[len(pos) - i-1].y)
        
              
def checkBounds(pos, siz):
    if (pos.x > width - siz.x/2):
        pos.x = siz.x/2
    elif pos.x < siz.x/2:
        pos.x = width - siz.x/2
    if (pos.y > height - siz.y/2):
        pos.y = siz.y/2
    elif pos.y < siz.y/2:
        pos.y = height - siz.y/2



def enemyMove():
    global ePos, pPos, eSpeed, state

    #move the enemies towards the head of the snake (for now)
    for i in range (0, len(ePos)):
        if len(pPos) < 1:
            state = 2
            return
        eVel = PVector.sub(eHome[i], ePos[i])
        eVel.mult(0.1)
        if (PVector.dist(pPos[0], ePos[i]) <=width/2):
            #seek the snake if it is close
            eVel.add(PVector.sub(pPos[0], ePos[i]))
        
        eVel.normalize()
        eVel.rotate(random(-PI, PI)*0.5)
        eVel.mult(eSpeed)
        ePos[i].add(eVel)

def enemyCheck():
    global ePos, pPos, pSize, eSize, state
    #check to see if any of the tail is in contact with the enemy
    #check only every 2nd frame to prevent insta-death
#    if int(frameCount)%1 == 0:
#        return
    for i in range (0, len(ePos)):
        #move them to the other size of the screen if necessary
        checkBounds(ePos[i], eSize[i])
        
        for j in range (0, len(pPos)):        
            if len(pPos) < 1:
                state = 2
                return       
            if detectHit(pPos[j],ePos[i], pSize[j],eSize[i]) and j < len(pPos) and j < len(pSize):
                pPos.remove(pPos[len(pPos)-1])
                pSize.remove(pSize[len(pSize)-1])
                return

def drawStuff():
    global pCol, pPos, pSize, eCol, eSize, ePos, eBool, score, iCol, iSize, iPos, iBool
#draw the player
    fill(pCol)
    
    for i in range(0, len(pPos)):
        rect(pPos[i].x, pPos[i].y, pSize[i].x, pSize[i].y, 10)
#    rect(pPos[0].x, pPos[0].y, pSize[0].x, pSize[0].y, 10)   

#draw items
    fill(iCol)    
    for i in range(0,len(iPos)):
        rect (iPos[i].x,iPos[i].y,iSize[i].x,iSize[i].y, 5);
    
    #draw enemies
    fill(eCol)    
    for i in range(0,len(ePos)):
        if eBool[i] == False:
            rect (ePos[i].x,ePos[i].y,eSize[i].x,eSize[i].y, 5);

    text(int(score),50,100)                 
                            
                                            
                                                                
                                                                                                
def draw():
    global pPos, pVel, pVelX, pVelY, pSize, bPos, bSize,pCol, speed, numItems, score, state
    background(200)

    if state == 0:
        #pregame state
        textSize = 60
        x= int(frameCount%width)
        text("Snake Game!", x,100)
        
        text("press start to continue",100,300)
    elif state == 1:    
        updatePos(pPos, pSize)
    #  pVel.add(pVelX)
    #   pVel.add(pVelY)
        pVel.normalize()
        pVel.mult(speed)
    
    #from brick example        
    #    if int(frameRate) % 60 == 0:
    #        addBrick()
        enemyMove()
        if state == 2:
            return

        pPos[0].add(pVel)
    
        checkBounds(pPos[0], pSize[0]);
        
        #check the items
        for i in range(0,len(iPos)):
            if i >= numItems:
                break
            if  detectHit(pPos[0], iPos[i], pSize[0], iSize[i]):
                iPos.remove(iPos[i])
                iSize.remove(iSize[i])
                numItems -=1
                score +=1
                pPos.append(PVector(pPos[len(pPos)-1].x-pVel.x,pPos[len(pPos)-1].y-pVel.y))
                pSize.append(pSize[0]/0.95)
                for j in range (1, len(pSize)):
                    pSize[j].set(pSize[j-1].x*0.95,pSize[j-1].y*0.95)
  #      print numItems    
        if numItems < 1:
            resetBlocks()
            print "WTF"
        enemyCheck()
        
        
        drawStuff()
       
    
    elif state == 2:
        drawStuff()
        text("Game Over!", width/2 , height/2)
    
