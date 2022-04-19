from pyxel import Image

class Colors:
    def __init__(self, file:str) -> None:
        self.color_img = Image(5, 5)
        self.load_colors(file)

    def load_colors(self, file:str) -> None:
        self.color_img.load(0, 0, file)
    
    def color(self, num:int) -> int:
        return self.color_img.pget(num%5, num//5)