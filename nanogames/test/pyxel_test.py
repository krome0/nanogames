import pyxel

class pyxel_app():
    def __init__(self) -> None:
        pyxel.init(120, 160, title='2048 Game')
        pyxel.mouse(False)
        
    def draw(self):
        self.clear_screen()

    def updata(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw_gamebg(self):
        pyxel.rect()


    def clear_screen(self, color:pyxel.colors = 15):
        pyxel.cls(color)