import pygame

class Level:
    def __init__(self, img):
        self.image = img
        self.doors = dict()
        self.grabs = dict()
        self.blocks = []

    def loadDoor(self, rect, key):
        self.doors[key] = rect

    def loadGrab(self, rect, key):
        self.grabs[key] = rect

    def loadBlock(self,rect):
        self.blocks.append(rect)

    def inDoor(self, rect):
        for d in self.doors:
            if(rect.colliderect(d)):
                return True
        return False

    def inGrab(self, rect):
        for g in self.grabs:
            if(rect.colliderect(g)):
                return True
        return False

