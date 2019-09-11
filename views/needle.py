"""class that will represent the item named Needle"""
from config import NEEDLE
class MacGyver(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add item named NEEDLE on gameboard """

    def __init__(self): #Initializer
        super().__init__()  #Appeller la méthode de  sprit  init elle-même 
        self.image = pg.image.load(settings.HERO).convert() #l'image avec le convert
        self.rect = self.image.get_rect() 