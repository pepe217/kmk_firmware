import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.rgb import RGB
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers as _Layers
from kmk.scanners.encoder import RotaryioEncoder
from kmk.keys import KC
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.labviewmacros import LabviewMacros
from kmk.handlers.sequences import simple_key_sequence

rgb = RGB(
        pixel_pin=board.NEOPIXEL,
        num_pixels=1,
        hue_default=120,
        sat_default=1,
        val_default=1
    )

class Layers(_Layers):
    last_top_layer = 0
    hues = (120, 60, 100, 160, 240, 0)
    
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)

# mapping is buttons straight to pins, no matrix
# below matches the silkscreen on the buttons
# FN1, R, FN2, FWD, BACK, FN3, L, MIDDLEB, TILEUP, TILEDOWN
click_false = [
    board.GP2, board.GP3, board.GP29, board.GP0, board.GP1,
    board.GP28
]
# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            KeysScanner(
                # require argument:
                pins=click_false,
                # optional arguments with defaults:
                value_when_pressed=False,
                pull=True,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64,
            ),
        ]
    coord_mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

keyboard = MyKeyboard()
keyboard.extensions.append(rgb)
keyboard.extensions.append(OneShot())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Layers())
trclick = simple_key_sequence(
    (
        KC.MB_LMB,
        KC.MB_LMB,
        KC.MB_LMB
    )
)
dbclick = simple_key_sequence(
    (
        KC.MB_LMB,
        KC.MB_LMB
    )
)

lv = LabviewMacros(KC)

keyboard.keymap = [
    [
        KC.MB_LMB, KC.MB_RMB, KC.MB_MMB, KC.MB_BTN5,
        KC.BTN4, KC.TO(1), KC.OS(KC.LCTL), KC.MB_MMB,
        KC.LSFT(KC.MW_UP), KC.LSFT(KC.MW_DN),
    ],
    [
        KC.MB_LMB, KC.MB_RMB, dbclick, lv.EXPNDM,
        lv.CLPSEM, KC.TO(0), trclick, lv.panm,
        lv.EXPND, KC.OS(KC.LSFT),
    ],
]

if __name__ == '__main__':
    keyboard.go()