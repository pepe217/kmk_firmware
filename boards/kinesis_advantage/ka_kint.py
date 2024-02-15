from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
import board


class KMKeyboard(_KMKKeyboard):
    row_pins = [
        board.GP18, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
        board.GP28_A2, board.GP27_A1, board.GP26_A0, board.GP22, board.GP19,
        board.GP5, board.GP12, board.GP13, board.GP24
    ]
    col_pins = [
        board.GP11, board.GP4, board.GP3, board.GP2, board.GP1, board.GP20,
        board.GP21
    ]
    diode_orientation = DiodeOrientation.COL2ROW
    rgb_pixel_pin = board.GP0
