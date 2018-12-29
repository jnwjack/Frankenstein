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
    obj.loadText("\"By degrees, I remember a stronger light pressed upon my nerves, so that I was obliged to shut my eyes.\"")
    obj.loadText("\"Darkness then came over me and troubled me, but hardly had I felt this when, by opening my eyes, as I now suppose, the light poured in on me again.\"")
    obj.loadText("\"The light became more and more oppressive to me, and the heat wearying me as I walked, I sought a place where I could receive shade.\"")
    obj.loadText("\"This was the forest near Ingolstadt.\"")