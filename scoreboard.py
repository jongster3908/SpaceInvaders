import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scorebord:
    """A class to report scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.ships = Group()

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Stuff
        self.level_image = self.font.render("Round  < " + str(self.stats.level) + " >", True,
                                            self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.high_score = int(round(self.stats.high_score, -1))
        self.high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render("HI-SCORE  " + self.high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)
        self.rounded_score = int(round(self.stats.score, -1))
        self.score_str = "{:,}".format(self.rounded_score)
        self.score_image = self.font.render("SCORE  " + self.score_str, True,
                                            self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """Show how many ships are left."""
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 20 + ship_number * (ship.rect.width + 5)
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("Round  < " + str(self.stats.level) + " >", True,
                                            self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        self.high_score = int(round(self.stats.high_score, -1))
        self.high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render("HI-SCORE  " + self.high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Turn the score into a rendered image"""
        self.rounded_score = int(round(self.stats.score, -1))
        self.score_str = "{:,}".format(self.rounded_score)
        self.score_image = self.font.render("SCORE  " + self.score_str, True,
                                            self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw ships.
        self.ships.draw(self.screen)
