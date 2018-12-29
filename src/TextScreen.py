import pygame.font
import time

pygame.font.init()
class TextScreen:
    def __init__(self):
        self.text = []
        self.red,self.blue,self.green = 1,1,1
        self.iter = 0
        self.fadeValue = 1

    def loadText(self, string):
        self.text.append(string)

    def getText(self):
        self.red,self.blue,self.green = 1,1,1
        temp = medFont(self.text[self.iter],(self.red,self.blue,self.green))
        self.iter += 1
        return temp

    def changeColor(self):
        self.red += self.fadeValue
        self.blue += self.fadeValue
        self.green += self.fadeValue
        temp = medFont(self.text[self.iter],(self.red,self.blue,self.green))
        return temp

    def getColorLevel(self):
        return self.red

    def swapFade(self):
        self.fadeValue *= -1

    def isFinished(self):
        return(self.iter >= len(self.text))

def medFont(text, color):
    f = pygame.font.SysFont("Arial", 20)
    rendered = f.render(text,1,color)
    return rendered