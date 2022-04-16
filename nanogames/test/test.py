from nanogames.core.game2048 import Game2048
from nanogames.windows.keyinput import search_input
import time
import numpy as np
import sys

a = Game2048(4, 4, 2048)

a.start_game()
a.gamestatus = np.array([[0,4,8,16],[16,8,4,2],[2,4,8,16],[16,8,4,2]])
print(a.show_status())

while True:
    key = search_input()
    if key is not None:
        if a.move(key):
            print('gameover')
            sys.exit()
        print(a.show_status())
        time.sleep(0.5)