from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
import board


class KMKeyboard(_KMKKeyboard):
    row_pins = [
        board.GPIO18, board.GPIO6, board.GPIO7, board.GPIO8, board.GPIO9,
        board.GPIO10, board.GPIO28, board.GPIO27, board.GPIO26, board.GPIO22,
        board.GPIO19, board.GPIO5, board.GPIO12, board.GPIO13, board.GPIO24
    ]
    col_pins = [
        board.GPIO11, board.GPIO4, board.GPIO3, board.GPIO2, board.GPIO1,
        board.GPIO20, board.GPIO21
    ]
    led_pin = board.GPIO0
    diode_orientation = DiodeOrientation.COL2ROW
