import pyxel
import nanogames.pyxel.games_list as games_list

class Config():
    FPS = 30 
    WIDTH = 200
    HEIGHT = 150
    LIST_SIZE = 40

    INTRO_TIME = 1.6
    TITLE = 'Nano Games'

class Select():
    def __init__(self) -> None:
        pyxel.init(Config.WIDTH, Config.HEIGHT, title=Config.TITLE, fps=Config.FPS)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
        
    def draw(self) -> None:
        self.intro()
        
        if pyxel.frame_count/Config.FPS >= Config.INTRO_TIME:
            self.clear_screen()
        games_list.game2048(Config.WIDTH/4-Config.LIST_SIZE, 
        Config.HEIGHT/4-Config.LIST_SIZE,
        Config.LIST_SIZE,
        Config.LIST_SIZE,
        )

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def intro(self) -> None:
        pyxel.cls(0)
        pyxel.text(Config.WIDTH/2, Config.HEIGHT/2, 'Made by Krome', 7)

    def clear_screen(self, color:pyxel.colors = 0) -> None:
        pyxel.cls(color)

select()