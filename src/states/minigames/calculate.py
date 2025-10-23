import os
import random

import pygame as pg

from src.states.minigames.minigame import Minigame
from src.constants import ENTER_KEYS

class Calculate(Minigame):
    """A minigame to test your math skills."""

    def __init__(self):
        instructions = (
            "The goal for this miniGame is to calculate the correct answer. "
            "A math problem will show up on the screen and you have to solve "
            "it and put the correct answer in the text box in order to win "
            "this minigame."
        )

        img = "calculate.png"

        super().__init__(
            instructions,
            img=os.path.join("minigames", img)
        )

        # Minigame specific attributes
        self.generated_string = ""
        self.input_string = ""
        self.input_rect = pg.Rect(300, 282, 200, 36)  # Adjusted position to center vertically
        self.input_active = False
        self.font = pg.font.SysFont(None, 36)
        self.generated_text_surf = None
        self.display_time = 10
        self.display_timer = 0
        self.is_string_currently_displayed = False
        self.was_string_displayed_yet = False
        self.clock = pg.time.Clock()
        self.firstNum = 0
        self.secondNum = 0
        self.sign = ''

    def handle_events(self, events):
        super().handle_events(events)  # To enable pause menu access
        for event in events:
            if event.type == pg.KEYDOWN and self.input_active:
                if event.key in ENTER_KEYS:
                    self.check_win_condition()
                elif event.key == pg.K_BACKSPACE:
                    self.input_string = self.input_string[:-1]
                else:
                    self.input_string += event.unicode

    def update(self, events):
        super().update(events)
        if not self.was_string_displayed_yet:
            self.generated_string = self.generate_random_question()
            self.generated_text_surf = self.font.render(self.generated_string, True, (255, 255, 255))
            self.was_string_displayed_yet = True
            self.is_string_currently_displayed = True
            self.display_timer = self.display_time * 1000  # Convert seconds to milliseconds
            self.input_active = True

    def draw(self):
        super().draw()  # Draw minigame background
        if self.timer.get_time_milliseconds() > 0:
            if self.generated_text_surf:
                self.screen.blit(self.generated_text_surf,
                                 ((self.screen.get_width() - self.generated_text_surf.get_width()) / 2 + 30, 200))

                pg.draw.rect(self.screen, (255, 255, 255), self.input_rect, 2)
                input_text_surf = self.font.render(self.input_string, True, (255, 255, 255))
                self.screen.blit(input_text_surf, (self.input_rect.x + 5, self.input_rect.y + 5))

    def generate_random_question(self):
        """Generates a random math question.

        Returns:
            str: The math question to answer.
        """

        self.firstNum = random.randint(1, 20)
        self.secondNum = random.randint(1, 20)
        self.sign = random.choice(["+", "-", "x"])
        question = '{}{}{}='.format(self.firstNum, self.sign, self.secondNum)
        return question

    def check_win_condition(self):
        """Sets the win condition depending on what the user inputted."""

        # check the player enter the correct answer
        if (self.sign == '+'):
            if (self.firstNum + self.secondNum == int(self.input_string)):
                self.won = True
                self.win_text = "\\o/"
            else:
                self.won = False
        if (self.sign == '-'):
            if (self.firstNum - self.secondNum == int(self.input_string)):
                self.won = True
                self.win_text = "\\o/"
            else:
                self.won = False
        if (self.sign == 'x'):
            if (self.firstNum * self.secondNum == int(self.input_string)):
                self.won = True
                self.win_text = "\\o/"
            else:
                self.won = False
