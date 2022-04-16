"""
2048game core
"""

import numpy as np
import random


class Game2048:
    def __init__(self, x_size: int, y_size: int, endnum: int) -> None:
        self.gamestatus = None
        self.x_size = x_size
        self.y_size = y_size
        self.endnum = endnum
        self.twoprob = 0.9
        self.fourprob = 0.1

    def start_game(self) -> None:
        self.gamestatus = np.zeros((self.y_size, self.x_size), dtype=np.int8)
        self.make_num(2)

    def make_num(self, amount: int = 1) -> None:
        zeros_y, zeros_x = np.where(self.gamestatus == 0)

        makenums_y = random.sample(list(zeros_y), amount)
        makenums_x = random.sample(list(zeros_x), amount)

        for y, x in zip(makenums_y, makenums_x):
            num = random.choices((2, 4), (self.twoprob, self.fourprob))[0]
            self.gamestatus[y, x] = num

    # I think there is better algorithm for moving numbers. (my brain is not working)
    def move(self, direction: str) -> None:
        direction_num = {'left': 0, 'up': 1, 'right': 2, 'down': 3}

        gamestatus_rot = np.rot90(self.gamestatus, direction_num[direction])
        gamestatus_rot = self.push_num(gamestatus_rot)
        gamestatus_rot = self.sum_num(gamestatus_rot)
        gamestatus_rot = self.push_num(gamestatus_rot)
        self.gamestatus = np.rot90(gamestatus_rot, -direction_num[direction])

        self.make_num(1)

    def push_num(self, gamestatus: np.ndarray) -> np.ndarray:
        size_y, size_x = gamestatus.shape
        gamestatus_pushed = np.zeros((size_y, size_x), dtype=np.int8)

        for index_y in range(size_y):
            index = 0

            for index_x in range(size_x):
                if gamestatus[index_y, index_x] != 0:
                    nonzero_num = gamestatus[index_y, index_x]
                    gamestatus_pushed[index_y, index] = nonzero_num
                    index += 1

        return gamestatus_pushed

    def sum_num(self, gamestatus: np.ndarray) -> np.ndarray:
        size_y, size_x = gamestatus.shape
        for index_y in range(size_y):
            for index_x in range(size_x - 1):
                num = gamestatus[index_y, index_x]
                num_next = gamestatus[index_y, index_x + 1]

                if num != 0 and num == num_next:
                    gamestatus[index_y, index_x] *= 2
                    gamestatus[index_y, index_x + 1] = 0

        return gamestatus

    def show_status(self) -> np.ndarray:
        return self.gamestatus
