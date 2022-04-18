from numpy import uint
import nanogames.pyxel.utils as utils
import pyxel

pyxel.init(100, 100, title='test', fps=10)

color_test = utils.Colors('/Users/krome/Documents/Project/nanogames/nanogames/pyxel/colors.png')

col = color_test.color(10)

print(col)