from typing import Any
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
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
    rgb_pixel_pin = board.GP0

    def __init__(self) -> None:
        self.matrix = MatrixScanner(column_pins=self.col_pins,
                                    row_pins=self.row_pins,
                                    columns_to_anodes=DiodeOrientation.COL2ROW)
