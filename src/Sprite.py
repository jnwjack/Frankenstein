import pygame

class Sprite:
    def __init__(self,img):
        self.image = img
        self.x,self.y = 0,0
        self.width,self.height = 0,0
        self.flipped = False

    def setX(self,num):
        self.x = num

    def setY(self,num):
        self.y = num

    def setWidth(self,num):
        self.width = num

    def setHeight(self,num):
        self.height = num

    def crop(self):
        if(self.flipped):
            return((self.image.get_width()-self.x-self.width),self.y,self.width,self.height)
        return(self.x,self.y,self.width,self.height)

    def flip(self):
        if(not self.flipped):
            self.flipped = True
        else:
            self.flipped = False
        return(pygame.transform.flip(self.image,True,False))



