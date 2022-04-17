import pyxel

def game2048(self, x:int, y:int, w:int, h:int, color:int) -> None:
    pyxel.rect(x, y, w, h, color)
    pyxel.text(x, y, '2048', 0)