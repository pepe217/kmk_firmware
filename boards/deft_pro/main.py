import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers as _Layers
from kmk.keys import KC
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.rgb import RGB
from kmk.modules.sticky_mod import StickyMod
from kmk.handlers.sequences import simple_key_sequence
from kmk.hid import HIDModes

rgb = RGB(
        pixel_pin=board.D4,
        num_pixels=1,
        hue_default=60,
        sat_default=255,
        val_default=255
    )

class Layers(_Layers):
    last_top_layer = 0
    hues = (60, 0)
    
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            # change led when layer change
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)

# mapping is buttons straight to pins, no matrix
# below matches the silkscreen on the case, not the PCB
# FN1, R, FN2,
# FWD, BACK,
# MIDDLEB, TILEUP, TILEDOWN,
# L, FN3
click_false = [
    board.D0, board.D1, board.D2, board.D3, board.D5,
    board.D6, board.D7, board.D8, board.D9, board.D10
]
# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
                # require argument:
                pins=click_false,
                # optional arguments with defaults:
                value_when_pressed=False,
                pull=True,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64,
            )
    coord_mapping = [9, 8, 7, 6, 4, 5, 2, 3, 0, 1]

keyboard = MyKeyboard()
keyboard.extensions.append(rgb)
keyboard.modules.append(Layers())
keyboard.modules.append(OneShot())
keyboard.modules.append(StickyMod())
keyboard.modules.append(MouseKeys())
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
start_altctl_click = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.LALT(no_release=True),
        KC.MB_LMB(no_release=True),
        KC.LALT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
start_ctl_click = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.MB_LMB(no_release=True),
        KC.LCTL(no_press=True),
    )
)
CTLALT = KC.LCTL(KC.LALT)
CTLSFT = KC.LSHIFT(KC.LCTL)
keyboard.keymap = [
    [
        KC.MB_LMB, KC.MB_RMB, KC.MB_MMB,
        KC.SM(KC.TAB, KC.LALT), KC.MB_BTN4,
        KC.TG(1), KC.LCTL(KC.Z), CTLSFT(KC.Z),
        KC.OS(KC.MB_LMB, tap_time=10000), dbclick,
    ],
    [
        KC.TRNS, KC.TRNS, trclick,
        start_ctl_click, start_altctl_click, 
        KC.TRNS, KC.TRNS, KC.TRNS,
        KC.MB_LMB(no_press=True), KC.TRNS,
    ],
]

if __name__ == '__main__':
    # keyboard.go()
    keyboard.go(hid_type=HIDModes.BLE, ble_name='KMKeyboard')