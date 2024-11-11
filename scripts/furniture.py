import pygame

BASE_IMAGE_PATH = 'data/images/'

class Desk:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/desk.png')
        self.img_size = [100, 100]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Chair:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/chair.png')
        self.img_size = [62, 100]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Plant:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/plant.png')
        self.img_size = [62, 100]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Desk_Vert:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/desk_vert.png')
        self.img_size = [60, 150]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Chair_Vert:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/chair_vert.png')
        self.img_size = [52, 90]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Chair_Front:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/chair_front.png')
        self.img_size = [52, 90]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Chair_Left:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/chair_left.png')
        self.img_size = [52, 90]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Window:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/window.png')
        self.img_size = [105, 85]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Window_Front:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/window_front.png')
        self.img_size = [100, 75]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Bookshelf:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/bookshelf.png')
        self.img_size = [125, 125]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Breakroom:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/leisure.png')
        self.img_size = [210, 220]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Table:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/table.png')
        self.img_size = [150, 150]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Pad_Front:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/pad_front.png')
        self.img_size = [65, 50]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Pad_Left:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/pad_left.png')
        self.img_size = [50, 65]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Pad_Right:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/pad_right.png')
        self.img_size = [50, 65]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Rug:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/rug.png')
        self.img_size = [200, 150]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Chalkboard:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/chalkboard.png')
        self.img_size = [120, 100]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class End_Table:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/end_table.png')
        self.img_size = [60, 60]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Globe:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/globe.png')
        self.img_size = [40, 50]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Lamp:
    def __init__(self, pos):
        self.img = pygame.image.load(BASE_IMAGE_PATH + 'furniture/lamp.png')
        self.img_size = [100, 100]
        self.pos = list(pos) #position 
        self.img = pygame.transform.scale(self.img, (self.img_size[0], self.img_size[1]))
        self.img.set_colorkey((167, 151, 150))
    
    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))