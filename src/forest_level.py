import Level, Sprite
import pygame, os, threading, time

running = True
moving = False
dest_x,dest_y = 1072,980
GRAB = pygame.image.load(os.path.join("images","grab.png"))
POINT = pygame.image.load(os.path.join("images","point.png"))
ARROW = pygame.image.load(os.path.join("images","arrow.png"))

def start(surface,hasLog=False,notBeginning=False):
    global running,dest_x,dest_y
    running = True
    background = Level.Level(pygame.image.load(os.path.join("images","forest_1.jpg")))
    player = Sprite.Sprite(pygame.image.load(os.path.join("images","frank.png")))
    fire = Sprite.Sprite(pygame.image.load(os.path.join("images","fire.gif")))
    cursor = POINT
    TEXT = ""
    isEnd = False
    initializeSprites(player,fire)
    addObjects(background)
    if(notBeginning):
        player_x,player_y = 647,640
        dest_x,dest_y = 647,720
    else:
        player_x,player_y = 1050,900
    fire_thread = threading.Thread(target=changeFire,args=(fire,))
    frank_thread = threading.Thread(target=changeFrank,args=(player,))
    fire_thread.start()
    frank_thread.start()
    while(running):
        m_x,m_y = pygame.mouse.get_pos()
        handleEvents((m_x,m_y))
        player_x,player_y = move(player_x,player_y,player,background)
        if(background.doors["door"].collidepoint((m_x,m_y))):
            cursor = ARROW
        elif(background.grabs["fire"].collidepoint((m_x,m_y))):
            cursor = GRAB
            TEXT = "\"...I was in the greatest fear lest my fire should be extinguished.\""
        else:
            cursor = POINT
            TEXT = ""
        p_rect = pygame.Rect(player_x,player_y,player.width,player.height)
        if(hasLog and p_rect.colliderect(background.grabs["fire"]) and background.grabs["fire"].collidepoint((dest_x,dest_y))):
            fire.setY(100)
            end_thread = threading.Thread(target=end)
            end_thread.start()
        if(p_rect.colliderect(background.doors["door"]) and background.doors["door"].collidepoint((dest_x,dest_y))):
            running = False
            return False
        bottom_text = smallFont(TEXT,(255,255,255))
        surface.blit(background.image,(0,0))
        if(player_y+player.height-player.y <= 825+fire.height):
            surface.blit(player.image,(player_x,player_y),(player.crop()))
            surface.blit(fire.image,(300,825),(fire.crop()))
        else:
            surface.blit(fire.image,(300,825),(fire.crop()))
            surface.blit(player.image,(player_x,player_y),(player.crop()))
        surface.blit(bottom_text,((1280-bottom_text.get_width()),(960-bottom_text.get_height())))
        surface.blit(cursor, (m_x+(cursor.get_width()/2),m_y+(cursor.get_height()/2)))
        pygame.display.flip()
    return True

def end():
    global running
    time.sleep(5)
    running = False

def handleEvents(pos):
    global dest_x,dest_y,running
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            dest_x,dest_y = pos
        if(event.type == pygame.QUIT):
            running = False
            pygame.quit()

def changeFire(fire):
    while(running):
        time.sleep(0.1)
        if(fire.x < 285):
            fire.setX(fire.x+95)
        else:
            fire.setX(0)

def changeFrank(frank):
    while(running):
        time.sleep(0.1)
        if(moving):
            if(frank.x < 220):
                frank.setX(frank.x+55)
            else:
                frank.setX(0)

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
        if((y+player.height-player.y) > dest_y):
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


def addObjects(bg):
    door = pygame.Rect(580,500,135,140)
    bg.loadDoor(door,"door")
    fire = pygame.Rect(300,825,100,100)
    bg.loadGrab(fire,"fire")
    top_left = pygame.Rect(0,0,500,725)
    bg.loadBlock(top_left)
    mid = pygame.Rect(500,0,385,500)
    bg.loadBlock(mid)
    mid_left = pygame.Rect(500,500,75,80)
    bg.loadBlock(mid_left)
    mid_right = pygame.Rect(715,500,170,115)
    bg.loadBlock(mid_right)
    top_right = pygame.Rect(885,0,395,805)
    bg.loadBlock(top_right)
    bottom_left = pygame.Rect(0,705,240,255)
    bg.loadBlock(bottom_left)


def initializeSprites(player,fire):
    player.setX(0)
    player.setY(15)
    player.setWidth(45)
    player.setHeight(95)
    fire.setX(0)
    fire.setY(0)
    fire.setWidth(40)
    fire.setHeight(50)


def smallFont(text, color):
    f = pygame.font.SysFont("Arial", 15)
    rendered = f.render(text,1,color)
    return rendered
