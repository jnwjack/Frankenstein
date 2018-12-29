import Level, Sprite
import pygame, os, threading, time

running = True
moving = False
dest_x,dest_y = 100,880
GRAB = pygame.image.load(os.path.join("images","grab.png"))
POINT = pygame.image.load(os.path.join("images","point.png"))
ARROW = pygame.image.load(os.path.join("images","arrow.png"))

def start(surface):
    global running
    running = True
    background = Level.Level(pygame.image.load(os.path.join("images","forest_2.jpg")))
    player = Sprite.Sprite(pygame.image.load(os.path.join("images","frank.png")))
    log = Sprite.Sprite(pygame.image.load(os.path.join("images","log.png")))
    TEXT = ""
    hasLog = False
    player_x,player_y = 100,800
    initializeSprites(player)
    addObjects(background)
    frank_thread = threading.Thread(target=changeFrank,args=(player,))
    frank_thread.start()
    while(running):
        m_x,m_y = pygame.mouse.get_pos()
        handleEvents((m_x,m_y))
        player_x,player_y = move(player_x,player_y,player,background)
        if(background.doors["door"].collidepoint((m_x,m_y))):
            cursor = ARROW
        elif(not hasLog and background.grabs["log"].collidepoint((m_x,m_y))):
            cursor = GRAB
            TEXT = "\"...I discovered the cause and busied myself in collecting a great quantity of wood.\""
        else:
            cursor = POINT
            TEXT = ""
        p_rect = pygame.Rect(player_x,player_y,player.width,player.height)
        if(not hasLog and p_rect.colliderect(background.grabs["log"]) and background.grabs["log"].collidepoint((dest_x,dest_y))):
            hasLog = True
            del background.grabs["log"]
        elif(p_rect.colliderect(background.doors["door"]) and background.doors["door"].collidepoint((dest_x,dest_y))):
            running = False
            return hasLog
        bottom_text = smallFont(TEXT,(255,255,255))
        surface.blit(background.image,(0,0))
        if(not hasLog):
            surface.blit(log.image,(1050,870))
        surface.blit(player.image,(player_x,player_y),(player.crop()))
        surface.blit(bottom_text,((1280-bottom_text.get_width()),(960-bottom_text.get_height())))
        surface.blit(cursor, (m_x+(cursor.get_width()/2),m_y+(cursor.get_height()/2)))
        pygame.display.flip()

def changeFrank(frank):
    global running
    while(running):
        time.sleep(0.1)
        if(moving):
            if(frank.x < 220):
                frank.setX(frank.x+55)
            else:
                frank.setX(0)

def handleEvents(pos):
    global dest_x,dest_y,running
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            dest_x,dest_y = pos
        if(event.type == pygame.QUIT):
            running = False
            pygame.quit()

def move(x,y,player,bg):
    global moving
    if(dest_x != (x+player.width/2) or dest_y != (y+player.height-player.y)):
        moving = True
        if((x+player.width/2) > dest_x):
            if(player.flipped):
                player.image = player.flip()
            x-=1
            rect = pygame.Rect(x,y,player.width,player.height)
            for block in bg.blocks:
                if(rect.colliderect(block)):
                    x+=1
                    break
        elif((x+player.width/2) < dest_x):
            if(not player.flipped):
                player.image = player.flip()
            x+=1
            rect = pygame.Rect(x,y,player.width,player.height)
            for block in bg.blocks:
                if(rect.colliderect(block)):
                    x-=1
                    break
        if((y+player.height-player.y)  > dest_y):
            y-=1
            rect = pygame.Rect(x,y,player.width,player.height)
            for block in bg.blocks:
                if(rect.colliderect(block)):
                    y+=1
                    break
        elif((y+player.height-player.y) < dest_y):
            y+=1
            rect = pygame.Rect(x,y,player.width,player.height)
            for block in bg.blocks:
                if(rect.colliderect(block)):
                    y-=1
                    break
    else:
        moving = False
    return(x,y)

def initializeSprites(player):
    player.setX(0)
    player.setY(15)
    player.setWidth(45)
    player.setHeight(95)

def addObjects(bg):
    door = pygame.Rect(0,830,40,130)
    bg.loadDoor(door,"door")
    log = pygame.Rect(1050,870,30,21)
    bg.loadGrab(log,"log")
    mid = pygame.Rect(0,0,1280,750)
    bg.loadBlock(mid)
    tree = pygame.Rect(875,750,180,70)
    bg.loadBlock(tree)


def smallFont(text, color):
    f = pygame.font.SysFont("Arial", 15)
    rendered = f.render(text,1,color)
    return rendered
