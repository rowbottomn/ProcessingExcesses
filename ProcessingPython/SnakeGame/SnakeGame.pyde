#Snake Program <==Character Walk PRogram 
#1.0Key controls on a rectangle
#2.0 items appear and dissappear when collected
#3.0 Snake gets longer as items are eaten
#4.0 Enemies move towards snake
#4.1 Enemies movement tweak (random if not in range)
#5.0 Periodic boundary conditions, hit detection on body and tail
#Errors: not detecting tail length <1 (game states needed), need periodic boundary conditions
#
# (13/22)
# (    11 /12)
# Critical Requirements 
# ++++On Time
# +Program has player controlled by keys
# +Enemy chases player
# +Player can pick up items
# +-Multiple types of items (Points, time, health) 
# -Some kind of end states are reached
# ++Documentation and proper header
# +Progression

# 2/10(any combrination of 10) Optional requirements
# +PVectors
# -Sounds
# -Background music
# -Pause
# -Mute sounds
# -Start screen
# -Variety of enemies
# -Variety of items
# -Animation
# -PImage array
# -Bonuses
# -Upgrades
# +***Magical items of an impressive quality 
# Tail of snake gets larger from eating food

def setup():
    size(800,800)
    rectMode(CENTER)
    stroke(200,50,100)
    strokeWeight(5)

#from brick example
#bPos = []
#bSize = PVector (40,20)
    
            
#game constants++++++++++++++++++++++++++++
state = 0#game state

#player variables++++++++++++++++++++++++++
pPos = []
pSize = []
pPos.append(PVector(400, 400))#player position
pSize.append(PVector(40,40))#player size 
speed = 5.0#player speed


pVel = PVector()
pDir = PVector()
score = 0.

attack = 10.0
defence = 10.0

pCol = color(255,0,0)

#item variables++++++++++++++++++++++++++
numItems = 20
iPos = []
iSize = []
iBool = []

#Enemy variables ++++++++++++++++++++++++

numEnemies = 4
ePos = []
eSize = []
eBool = [] #not used currently
eSpeed = 4

#set the item list
for i in range(0,numItems):
    iPos.append(PVector(random(50,750),random(50,750)))#item position
    iSize.append(PVector(5,5))#item size
    iBool.append(False)
iCol = color(50,150,200)
    
#set the item list    
for i in range (0,numEnemies):
    ePos.append(PVector(random(15,50),random(14,50)))#Enemy starting position
    eSize.append(PVector(20,20))#enemy Size
    eBool.append(False)
eCol = color(0,0,250)        

def resetBlocks():
    global iPos, iSize, iBool, numItems
    for i in range(0,numItems):
        iPos[i]=(PVector(random(50,750),random(50,750)))#player position
        iSize[i]=(PVector(15,15))#player
        iBool[i]=(False)
                            
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
    global pVel, pVelX, pVelY, pDir
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
    if key == ' ':
        resetBlocks() 
       
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
    
    
    #move backwards thru the array giving each body 
    #segment the position of the one close to the head
    
    for i in range(1 , len(pos)):
#        print i
        #we start at the end and the i value moves us toward the head
        pos[len(pos) -i ].set(pos[len(pos) -i-1].x, pos[len(pos) - i-1].y)

    if (pPos[0].x > width - pSize[0].x/2):
        pPos[0].x = pSize[0].x/2
    elif pPos[0].x < pSize[0].x/2:
        pPos[0].x = width - pSize[0].x/2
    if (pPos[0].y > height - pSize[0].y/2):
        pPos[0].y = pSize[0].y/2
    elif pPos[0].y < pSize[0].y/2:
        pPos[0].y = height - pSize[0].y/2


resetBlocks()

def enemyMove():
    global ePos, pPos, eSpeed

    #move the enemies towards the head of the snake (for now)
    for i in range (0, len(ePos)):
        if (PVector.dist(pPos[0], ePos[i]) <=width/2):
            #seek the snake if it is close
            eVel = PVector.sub(pPos[0], ePos[i])
        else:
            eVel = PVector(int(random(-1,2)),int(random(-1,2)))
        #add some random vector to prevent clustering
        eVel.normalize()
        eVel.rotate(int(random(-1, 2))*PI*0.75)
        eVel.mult(eSpeed)
        ePos[i].add(eVel)

def enemyCheck():
    global ePos, pPos, pSize, eSize
    #check to see if any of the tail is in contact with the enemy
    #check only every 2nd frame to prevent insta-death
#    if int(frameCount)%1 == 0:
#        return
    for i in range (0, len(ePos)):
        #move them to the other size of the screen if necessary
        if (ePos[i].x > width - eSize[i].x/2):
            ePos[i].x = eSize[i].x/2
        elif ePos[i].x < eSize[i].x/2:
            ePos[i].x = width - eSize[i].x/2
        if (ePos[i].y > height - eSize[i].y/2):
            ePos[i].y = eSize[i].y/2
        elif ePos[i].y < eSize[i].y/2:
            ePos[i].y = height - eSize[i].y/2

        for j in range (0, len(pPos)):                
            if detectHit(pPos[j],ePos[i], pSize[j],eSize[i]) and j < len(pPos) and j < len(pSize):
                pPos.remove(pPos[len(pPos)-1])
                pSize.remove(pSize[len(pSize)-1])
                return
                
def draw():
    global pPos, pVel, pVelX, pVelY, pSize, bPos, bSize,pCol, speed, numItems, score
    background(100)
    
    updatePos(pPos, pSize)
  #  pVel.add(pVelX)
 #   pVel.add(pVelY)
    pVel.normalize()
    pVel.mult(speed)

#from brick example        
#    if int(frameRate) % 60 == 0:
#        addBrick()
    enemyMove()
        
    pPos[0].add(pVel)
    #check positions
#    if (pPos[0].x < pSize[0].x /2 or pPos[0].x > width - pSize[0].x/2):
 #       pPos[0].x -= pVel.x
 #   if (pPos[0].y < pSize[0].y /2 or pPos[0].y >  height - pSize[0].y/2):
 #       pPos[0].y -= pVel.y
    
    #check the items
    for i in range(0,len(iPos)):
        if iBool[i] == False and detectHit(pPos[0], iPos[i], pSize[0], iSize[i]):
            iBool[i] = True
            score +=1
            pPos.append(PVector(pPos[len(pPos)-1].x-pVel.x,pPos[len(pPos)-1].y-pVel.y))
            pSize.append(pSize[0]/0.95)
            for j in range (1, len(pSize)):
                pSize[j].set(pSize[j-1].x*0.95,pSize[j-1].y*0.95)

    enemyCheck()

#draw the player
    fill(pCol)
    
    for i in range(0, len(pPos)):
        rect(pPos[i].x, pPos[i].y, pSize[i].x, pSize[i].y, 10)
#    rect(pPos[0].x, pPos[0].y, pSize[0].x, pSize[0].y, 10)


#from brick example
#    for i in range(0, len(bPos)):
#        rect(bPos[i].x,bPos[i].y, bSize.x, bSize.y)

#draw items
    fill(iCol)    
    for i in range(0,len(iPos)):
        if iBool[i] == False:
            rect (iPos[i].x,iPos[i].y,iSize[i].x,iSize[i].y, 5);
    
    #draw enemies
    fill(eCol)    
    for i in range(0,len(ePos)):
        if eBool[i] == False:
            rect (ePos[i].x,ePos[i].y,eSize[i].x,eSize[i].y, 5);
    
    text(int(score),50,100)        
