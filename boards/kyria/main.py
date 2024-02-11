from kyria_v3 import KMKKeyboard
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers as _Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.capsword import CapsWord
from kmk.modules.split import Split, SplitType
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.sticky_mod import StickyMod
from storage import getmount
from macros import CommonMacros

keyboard = KMKKeyboard()
keyboard.debug_enabled = False

# rgb doesnt talk between sides, disable the right side LEDs to avoid confusion
lside = str(getmount('/').label)[-1] == 'L'
if lside:
    rgb = RGB(
        pixel_pin=keyboard.rgb_pixel_pin,
        num_pixels=6,
        hue_default=120,
        sat_default=255,
        val_default=255
    )

    class Layers(_Layers):
        last_top_layer = 0
        hues = (120, 60, 100, 160, 240, 0, 280, 320, 300)
	    
        def after_hid_send(self, keyboard):
            if keyboard.active_layers[0] != self.last_top_layer:
                self.last_top_layer = keyboard.active_layers[0]
                rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)
else:
	rgb = RGB(
	    pixel_pin=keyboard.rgb_pixel_pin,
	    num_pixels=6,
	    hue_default=0,
	    sat_default=0,
	    val_default=0
	)
	class Layers(_Layers):
		pass

keyboard.extensions.append(rgb)
combos = Combos()
keyboard.modules.append(combos)
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules.append(tapdance)
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(OneShot())
capsword = CapsWord()
capsword.keys_ignored.append(KC.DOT)
capsword.timeout = 2000
keyboard.modules.append(capsword)
keyboard.modules.append(MouseKeys())
split = Split(split_type=SplitType.UART, use_pio=True, split_flip=True, uart_flip=True)
keyboard.modules.append(split)
sticky_mod = StickyMod()
keyboard.modules.append(sticky_mod)
m = CommonMacros(KC)

# General macros
SFTOS = KC.OS(KC.LSHIFT, tap_time=1500)
CTLOS = KC.OS(KC.LCTL, tap_time=None)
ALTOS = KC.OS(KC.LALT, tap_time=None)
OS_LCTL_LSFT = KC.OS(KC.LCTL(SFTOS), tap_time=None)
OS_LCTL_LALT = KC.OS(KC.LCTL(ALTOS), tap_time=None)
OS_LSFT_LALT = KC.OS(KC.LSFT(ALTOS), tap_time=None)
OS_LCTL_LSFT_LALT = KC.OS(KC.LCTL(KC.LSFT(ALTOS)), tap_time=None)
combos.combos = [
	Chord((CTLOS, SFTOS), OS_LCTL_LSFT, timeout=1000),
    Chord((CTLOS, ALTOS), OS_LCTL_LALT, timeout=1000),
    Chord((SFTOS, ALTOS), OS_LSFT_LALT, timeout=1000),
    Chord((CTLOS, SFTOS, ALTOS), OS_LCTL_LSFT_LALT, timeout=1000),
]
keyboard.keymap = [
    # 0 - base
    [
        ALTOS, KC.B,  KC.Y, KC.O,    KC.U,   m.QUOTS,                                                  m.COLON,   KC.L,   KC.D,   KC.W, KC.V, KC.Z,
        CTLOS, KC.C,  KC.I, KC.E,    m.a,      m.comm,                                                   m.dot,     m.h,      KC.T,   KC.S, KC.N, KC.Q,
        m.GUIOS, KC.G,  KC.X, KC.J,    KC.K,   m.lpbk,    KC.OS(KC.MO(2)), KC.TG(1),  SFTOS,    KC.MINS, m.rpbk,    KC.R,   KC.M,   KC.F, KC.P, KC.CW,
                            m.curly,   m.EQLADD, KC.BSPC, KC.ESC,          KC.TAB,    KC.OS(KC.MO(3)), KC.ENT,  KC.SPC,  KC.DEL, m.slash 
    ],
    # 1 - keypad/function
    [
        KC.TRNS,  KC.F1, KC.F2,  KC.F3,   KC.F4,   KC.PGDN,                                        KC.PSLS, KC.N7,   KC.N8, KC.N9, KC.PMNS, KC.PSCR,
        KC.TRNS,  KC.F5, KC.F6,  KC.F7,   KC.F8,   KC.PGUP,                                         KC.PAST, KC.N4,   KC.N5, KC.N6, KC.PPLS, KC.PGUP,
        KC.TRNS,  KC.F9, KC.F10, KC.F11,  KC.F12,  KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.PEQL, KC.N1,   KC.N2, KC.N3, KC.NC,   KC.PGDN,
                                 KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.P0,   KC.TRNS, KC.PDOT
    ],
    # 2 - symbols
    [
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,   KC.PERC,                                        KC.CIRC, KC.AMPR,  KC.ASTR,  KC.LPRN, KC.RPRN,  KC.EQL,  
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,    KC.N5,                                          KC.N6,   KC.N7,    KC.N8,    KC.N9,   KC.N0,    KC.PLUS,  
        KC.PIPE, KC.BSLS, KC.COLN, KC.SCLN, KC.MINUS, KC.LBRC,  KC.NO,   KC.TRNS,   KC.TRNS, KC.CW,   KC.RBRC, KC.UNDS,  KC.COMMA, KC.DOT,  KC.SLASH, KC.QUES,  
                                   KC.TRNS, KC.TRNS,  KC.TRNS,  KC.DOWN, KC.UP,     KC.LCBR, KC.RCBR, KC.LEFT, KC.RIGHT, KC.PSCR
    ],
    # 3 - navigation
    [
        KC.LCTL(KC.L), KC.NO,   KC.NO,         KC.NO,         KC.NO,         m.newtab,                                         KC.TRNS, KC.LSFT(KC.LGUI(KC.UP)), KC.LSFT(KC.LGUI(KC.DOWN)), KC.LSFT(KC.LGUI(KC.RGHT)), KC.LSFT(KC.LGUI(KC.LEFT)), KC.LCTL(KC.L),  
        KC.LCTL(KC.Z), KC.EFT, KC.RGHT,       KC.DOWN,       KC.UP,         m.rename,                                         KC.TRNS, KC.LCTL(KC.C),           KC.NO,                     KC.F4,                     KC.NO,                     KC.LALT(KC.TAB),  
        KC.TRNS,       m.undo,    KC.LCTL(KC.X), KC.LCTL(KC.C), m.paste,         m.pastee,  KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, m.maximize,                KC.LGUI(KC.DOWN),          KC.LGUI(KC.RGHT),          KC.LGUI(KC.LEFT),          KC.LCTL(KC.Z),  
                                               m.undtab,        KC.LCTL(KC.V), KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                 KC.TRNS  
    ],
]

if __name__ == '__main__':
    keyboard.go()
