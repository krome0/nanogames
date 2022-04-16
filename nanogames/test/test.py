from nanogames.core.game2048 import Game2048
from nanogames.windows.keyinput import search_input
import time

a = Game2048(4, 4, 2048)

a.start_game()
print(a.show_status())

while True:
    key = search_input()
    if key is not None:
        a.move(key)
        print(a.show_status())
        time.sleep(0.5)