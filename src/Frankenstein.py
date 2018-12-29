import forest_black, forest_level, log_level, end_black
import pygame, os

def main():
    pygame.init()
    pygame.display.set_caption("Frankenstein")
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    pygame.mouse.set_visible(True)
    surface = pygame.display.set_mode((1280,960))
    icon = pygame.image.load(os.path.join("images","f.png"))
    pygame.display.set_icon(icon)

    hasLog = False
    isEnd = False
    forest_black.start(surface)
    isEnd = forest_level.start(surface,hasLog)
    while(not isEnd):
        hasLog = log_level.start(surface)
        isEnd = forest_level.start(surface,hasLog,True)
    end_black.start(surface)



if __name__ == "__main__":
    main()
