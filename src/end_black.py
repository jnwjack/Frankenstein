import TextScreen
import pygame, time

def start(surface):
    text = TextScreen.TextScreen()
    addText(text)
    x,y = 0,0
    while(not text.isFinished()):
        pygame.event.pump()
        surface.fill((0,0,0))
        if(text.getColorLevel() > 0 and text.getColorLevel() < 255):
            phrase = text.changeColor()
            time.sleep(0.01)
        elif(text.getColorLevel() == 255):
            text.swapFade()
            phrase = text.changeColor()
            time.sleep(0.01)
        else:
            phrase = text.getText()
            text.swapFade()
            y += 200
            x += 100
            time.sleep(2)
        surface.blit(phrase,(x,y))
        pygame.display.flip()

def addText(obj):
    obj.loadText("\"It was dark when I awoke; I felt cold also, and half frightened, as it were, instinctively, finding myself so desolate.\"")
    obj.loadText("\"....I continued my journey.  The labours I endured were no longer to be alleviated by the bright sun or gentle breezes of spring;\"")
    obj.loadText("\"all joy was but a mockery which insulted my desolate state and made me feel more painfully that I was not made for the enjoyement of pleasure.\"")
    obj.loadText("\"But my toils drew near a close, and in two months from this time I reached the environs of Geneva.\"")
    obj.loadText("The end.")