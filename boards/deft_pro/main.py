import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers as _Layers
from kmk.keys import KC
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import simple_key_sequence
import digitalio
from kmk.hid import HIDModes

class Layers(_Layers):
    last_top_layer = 0
    led_states = [
        [True, True, False],
        [True, False, True],
        [False, True, True],
        [False, True, True],
    ] 
    red = digitalio.DigitalInOut(board.LED_RED)
    red.direction = digitalio.Direction.OUTPUT
    red.value = led_states[0][0]
    blue = digitalio.DigitalInOut(board.LED_BLUE)
    blue.direction = digitalio.Direction.OUTPUT
    blue.value = led_states[0][1]
    green = digitalio.DigitalInOut(board.LED_GREEN)
    green.direction = digitalio.Direction.OUTPUT
    green.value = led_states[0][2]
    led_pins = [red, blue, green]

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            # change led when layer change
            for i in range(len(self.led_pins)):
                self.led_pins[i].value = self.led_states[self.last_top_layer][i]

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
keyboard.debug_enabled = False
keyboard.modules.append(Layers())
keyboard.modules.append(OneShot())
keyboard.modules.append(StickyMod())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(ModTap())
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
start_pan = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.LSFT(no_release=True),
        KC.MB_LMB(no_release=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
        KC.TG(2)
    )
)
start_collapse = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.LALT(no_release=True),
        KC.MB_LMB(no_release=True),
        KC.LALT(no_press=True),
        KC.LCTL(no_press=True),
        KC.TG(2)
    )
)
start_expand = simple_key_sequence(
    (
        KC.LCTL(no_release=True),
        KC.MB_LMB(no_release=True),
        KC.LCTL(no_press=True),
        KC.TG(2)
    )
)
end_click = simple_key_sequence(
    (
        KC.MB_LMB(no_press=True),
        KC.TG(2)
    )
)
CTLALT = KC.LCTL(KC.LALT)
CTLSFT = KC.LSHIFT(KC.LCTL) 
keyboard.keymap = [
    [
        KC.MT(KC.SM(KC.TAB, KC.LALT), KC.ENT), KC.MB_RMB, KC.MB_MMB,
        KC.MB_LMB, KC.MB_BTN4,
        KC.TG(1), KC.LCTL(KC.Z), CTLSFT(KC.Z),
        KC.OS(KC.MB_LMB, tap_time=10000), KC.MT(dbclick, trclick),
    ],
    [
        KC.TRNS, KC.TRNS, start_pan,
        KC.TRNS, start_expand,
        KC.TRNS, KC.TRNS, start_collapse,
        KC.TRNS, KC.TRNS,
    ],
    [
        end_click, end_click, end_click, 
        end_click, end_click,
        end_click, end_click, end_click, 
        end_click, end_click, 
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE)