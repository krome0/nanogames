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

        self.gamestatus = np.rot90(self.gamestatus, direction_num[direction])
        self.push_num()
        self.sum_num()
        self.push_num()
        self.gamestatus = np.rot90(self.gamestatus, -direction_num[direction])

        self.make_num(1)

        if self.check_nozero:
            a = self.check_gameover()
            return a
        else: return False

    def push_num(self) -> None:
        size_y, size_x = self.gamestatus.shape
        gamestatus_pushed = np.zeros((size_y, size_x), dtype=np.int8)

        for index_y in range(size_y):
            index = 0

            for index_x in range(size_x):
                if self.gamestatus[index_y, index_x] != 0:
                    nonzero_num = self.gamestatus[index_y, index_x]
                    gamestatus_pushed[index_y, index] = nonzero_num
                    index += 1
        
        self.gamestatus = gamestatus_pushed

    def sum_num(self) -> None:
        size_y, size_x = self.gamestatus.shape
        for index_y in range(size_y):
            for index_x in range(size_x - 1):
                num = self.gamestatus[index_y, index_x]
                num_next = self.gamestatus[index_y, index_x + 1]

                if num != 0 and num == num_next:
                    self.gamestatus[index_y, index_x] *= 2
                    self.gamestatus[index_y, index_x + 1] = 0

    def check_nozero(self) -> bool:
        zeros_y, zeros_x = np.where(self.gamestatus == 0)

        return len(zeros_y) == 0 and len(zeros_x) == 0

    def check_gameover(self) -> bool:
        size_y, size_x = self.gamestatus.shape
        for index_y in range(size_y-1):
            for index_x in range(size_x-1):
                num = self.gamestatus[index_y, index_x]
                num_down = self.gamestatus[index_y + 1, index_x]
                num_right = self.gamestatus[index_y, index_x + 1]

                if num == num_down: return False
                if num == num_right: return False

        return True

    def show_status(self) -> np.ndarray:
        return self.gamestatus
