#! /usr/bin/env python3
# coding : utf-8

""" Module for pygame interface"""

import pygame as pg

from config import settings
from macgyver.views.macgyver import MacGyver
from macgyver.views.items import ItemSprite
from macgyver.views.guard import Guard
from macgyver.models.gameboard import GameBoard
from macgyver.models.hero import Hero
from macgyver.models.items import N, E, T
from macgyver.exceptions.gamewon import GameWon
from macgyver.exceptions.gameover import GameOver


class Game:
    """ Class that represents the game for pygame"""

    def __init__(self):  # Constructor
        """ All elements that are needed for the game to be played """

        self.gameboard = GameBoard()
        self.gameboard.load_from_file()
        self.gameboard.add_items(N)
        self.gameboard.add_items(E)
        self.gameboard.add_items(T)
        self.hero = Hero(self.gameboard)
        # putting the hero into the GameBoard

        pg.init()

        # Set the title on screen
        pg.display.set_caption("MacGyver's Mad Escape")

        # 1. Set the size of the screen in pixels
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # 2. Set an attribute for the background, the image is its value
        self.background = pg.image.load(settings.BACKGROUND).convert_alpha()

        # Loading image for loosing game
        self.lost = pg.image.load(settings.LOST).convert_alpha()
        # Loading image for winning game
        self.won = pg.image.load(settings.WON).convert_alpha()

        # Loading image that is wall
        self.wall = pg.image.load(settings.WALL).convert_alpha()
        for wall in self.gameboard.walls:
            # Add images for each wall
            # copie and size of image
            self.background.blit(
                self.wall, (wall.x * settings.SPRITE_WIDTH,
                wall.y * settings.SPRITE_HEIGHT))

        self.passages = pg.image.load(
            settings.PASSAGES).convert_alpha()
        for passages in self.gameboard.passages:
            self.background.blit(
                self.passages, (passages.x * settings.SPRITE_WIDTH,
                passages.y * settings.SPRITE_HEIGHT))

        # Copie the background over the screen. It's called to '.blit()'.
        self.screen.blit(self.background, (0, 0), self.screen.get_rect())

        # Sprites - We use a pygame method to manage updates with sprites
        self.sprites = pg.sprite.RenderUpdates()

        # We add our sprites into the gameboard
        self.sprites.add(MacGyver(self.hero))
        self.sprites.add(Guard())
        self.sprites.add(ItemSprite(settings.TUBE_PATH, T, self.gameboard))
        self.sprites.add(ItemSprite(settings.ETHER_PATH, E, self.gameboard))
        self.sprites.add(ItemSprite(settings.NEEDLE_PATH, N, self.gameboard))

        # Allows the player to keep on pressing down the key and the hero moves
        pg.key.set_repeat(500, 100)

        pg.display.update()

        # The switch ON/OFF (T/F boolean) for the gameloop
        self.running = False

    def start(self):
        """Method that launches the game"""

        clock = pg.time.Clock()
        # Switch On/Off
        self.running = True

        try:

            while self.running:  # loop of the game launch

                # Frame per seconds. In order words, the speed of the loop
                clock.tick(40)

                self._process_quit_events()  # process to close the game window

                # 1. Cover the gamespace with the background, we clear our screen
                # and put our background over it
                self.sprites.clear(self.screen, self.background)

                # 2. Call update() methods from for classes that are from sprites
                self.sprites.update()

                # 3. Draws over what should be drawn, paste or blits all different images on screen
                updated_sprites = self.sprites.draw(self.screen)

                # 4 Returns the list of updated sprites that were modified from last loop lap
                pg.display.update(updated_sprites)

        except GameWon as e:  # if gamer wins
            print(e)
            self.running = True
            self.display_message(self.won)

        except GameOver as e:  # if gamer looses
            print(e)
            self.running = True
            self.display_message(self.lost)

    def _process_quit_events(self):
        """ method that quits the game when the user press the RED CROSS on window"""
        for _ in pg.event.get(pg.QUIT):
            self.running = False

    def display_message(self, image):
        """ method that adds a screen for GameOver or GameWon"""
        self.running = True
        self.background = image
        self.screen.blit(self.background, self.screen.get_rect())
        pg.display.update()
        self.start()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
