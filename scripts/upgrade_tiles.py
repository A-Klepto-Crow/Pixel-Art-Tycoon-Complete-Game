import pygame

BASE_IMAGE_PATH = 'data/images/'

class Worker_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/worker_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Plant_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/plant_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Computer_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/computer_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Window_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/window_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Bookshelf_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/bookshelf_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Breakroom_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/breakroom_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height
    
class Decor_Upgrade_Tile:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'upgrade_tiles/decor_upgrade.png')
        self.pos = list(pos) #position 
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

    def return_width(self):
        return self.img_width
    
    def return_height(self):
        return self.img_height