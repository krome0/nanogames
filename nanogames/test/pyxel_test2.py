import py
import pyxel

class pyxel_app():
    def __init__(self) -> None:
        pyxel.init(120, 160, title='2048 Game')
        pyxel.mouse(False)
        pyxel.run(self.update, self.draw)
        
    def draw(self):
        self.clear_screen()
        pyxel.text(50, 50, '2048', 0)

    def clear_screen(self, color:pyxel.colors = 15):
        pyxel.cls(color)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

pyxel_app()