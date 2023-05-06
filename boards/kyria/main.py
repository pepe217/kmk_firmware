from kyria_v3 import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers as _Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.capsword import CapsWord
from kmk.modules.split import Split, SplitType
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Chord, Combos
from storage import getmount
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.labviewmacros import LabviewMacros

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
        hues = (120, 60, 100, 160, 240, 0)
	    
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
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(OneShot())
capsword = CapsWord()
capsword.keys_ignored.append(KC.DOT)
keyboard.modules.append(capsword)
keyboard.modules.append(MouseKeys())
 
split = Split(split_type=SplitType.UART, use_pio=True, split_flip=True, uart_flip=True)
keyboard.modules.append(split)

# General macros
SFTOS = KC.OS(KC.LSHIFT, tap_time=None)
GUIOS = KC.MT(KC.OS(KC.LM(2, KC.LGUI)), KC.LGUI)
CTLSFT = KC.LSHIFT(KC.LCTL)
CTLOS = KC.OS(KC.LCTL, tap_time=None)
ALTOS = KC.OS(KC.LALT, tap_time=None)
# CTLSFT = KC.LSHIFT(KC.LCTL)
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
COLON = KC.TD(KC.COLON, KC.SCLN, KC.CW)
BRACES = KC.TD(KC.LBRC, KC.RBRC)
CBRACES = KC.TD(KC.LCBR, KC.RCBR)
PRN = KC.TD(KC.LPRN, KC.RPRN)
EQLADD = KC.TD(KC.EQL, KC.PLUS)
MINSU = KC.TD(KC.MINS, KC.UNDS)
QUES = KC.TD(KC.SLSH, KC.QUES)
PERD = KC.TD(KC.DOT, KC.RABK)
COMMA = KC.TD(KC.COMM, KC.LABK)
rename = simple_key_sequence(
	    (
	        KC.F2,
	        KC.TG(3)
	    )
	)
undtab = simple_key_sequence(
	    (
	        CTLSFT(KC.T),
	        KC.TG(3)
	    )
    )
QUOTS = KC.TD(KC.QUOT, KC.DQT)
# move between labview key and macro layers
LVLYR = simple_key_sequence((KC.TG(4), KC.TG(5)))
#paste, enter and leave layer
pastee = simple_key_sequence(
    (
        KC.LCTL(KC.V),
	    KC.ENT,
        KC.TG(3)
    )
) 
#paste and leave layer
paste = simple_key_sequence(
    (
        KC.LCTL(KC.V),
        KC.TG(3)
    )
) 
#undo and leave layer
undo = simple_key_sequence(
    (
        KC.LCTL(KC.Z),
        KC.TG(3)
    )
)
# save and leave layer
savef = simple_key_sequence(
    (
        KC.LCTL(KC.S),
        KC.TG(3)
    )
) 
# open new tab, paste and enter
newtab = simple_key_sequence(
    (
        KC.LCTL(KC.T),
        KC.LCTL(KC.V),
        KC.ENT,
        KC.TG(3)
    )
)
lv = LabviewMacros(KC)

keyboard.keymap = [
    # base
    [
        ALTOS,  lv.test,  KC.W,    KC.F,  KC.P,    KC.B,                                                 KC.J,   KC.L,   KC.U,    KC.Y,   QUOTS,  MINSU,
        CTLOS,  KC.A,  KC.R,    KC.S,  KC.T,    KC.G,                                                 KC.M,   KC.N,   KC.E,    KC.I,   KC.O,    EQLADD,
        PRN,    KC.Z,  KC.X,    KC.C,  KC.D,    KC.V,    KC.OS(KC.MO(2)), LVLYR,    COLON,   SFTOS,   KC.K,   KC.H,   COMMA,   PERD,   QUES,    BRACES,
                                GUIOS, KC.ESC,  KC.BSPC, KC.TG(3),        KC.TG(1), KC.TAB,  KC.ENT,  KC.SPC, KC.DEL, CBRACES 
    ],
    # keypad/function
    [
        KC.TRNS,  KC.PSLS, KC.N7, KC.N8,   KC.N9,   KC.PMNS,                                        KC.HOME, KC.F1,   KC.F2,  KC.F3,  KC.F4,  KC.PGUP,
        KC.TRNS,  KC.PAST, KC.N4, KC.N5,   KC.N6,   KC.PPLS,                                        KC.END,  KC.F5,   KC.F6,  KC.F7,  KC.F8,  KC.PGDN,
        KC.TRNS,  KC.KPEQ, KC.N1, KC.N2,   KC.N3,   KC.ENT,  KC.TRNS, KC.TG(1),   KC.TRNS, KC.TRNS, KC.TRNS, KC.F9,   KC.F10, KC.F11, KC.F12, KC.PSCR,
                                  KC.P0,   KC.PDOT, KC.BSPC, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.LALT, KC.TRNS, KC.TRNS
    ],
    # symbols
    [
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,    KC.N5,                                          KC.N6,   KC.N7,    KC.N8,    KC.N9,   KC.N0,    KC.PLUS,  
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,   KC.PERC,                                        KC.CIRC, KC.AMPR,  KC.ASTR,  KC.LPRN, KC.RPRN,  KC.EQL,  
        KC.PIPE, KC.BSLS, KC.COLN, KC.SCLN, KC.MINUS, KC.LBRC,  KC.TRNS, KC.TG(2),  KC.TRNS, KC.CW,   KC.RBRC, KC.UNDS,  KC.COMMA, KC.DOT,  KC.SLASH, KC.QUES,  
                                   KC.TRNS, KC.TRNS,  KC.TRNS,  KC.DOWN, KC.UP,     KC.LCBR, KC.RCRB, KC.LEFT, KC.RIGHT, KC.PSCR  
    ],
    # navigation
    [
        KC.LCTL(KC.L), lv.MV10L,lv.MV10R,      lv.MV10D,      lv.MV10U,      newtab,                                         KC.TRNS, KC.LSFT(KC.LGUI(KC.UP)), KC.LSFT(KC.LGUI(KC.DOWN)), KC.LSFT(KC.LGUI(KC.RGHT)), KC.LSFT(KC.LGUI(KC.LEFT)), KC.LCTL(KC.L),  
        KC.LCTL(KC.Z), KC.LEFT, KC.RGHT,       KC.DOWN,       KC.UP,         rename,                                         KC.TRNS, KC.LGUI(KC.UP),          KC.LGUI(KC.DOWN),          KC.LGUI(KC.RGHT),          KC.LGUI(KC.LEFT),          KC.LCTL(KC.Z),  
        KC.TRNS,       undo,    KC.LCTL(KC.X), KC.LCTL(KC.C), paste,         pastee,  KC.TRNS, KC.TG(3),   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                 KC.TRNS,                   KC.TRNS,                   KC.TRNS,                   KC.LALT(KC.TAB),  
                                               undtab,        KC.LCTL(KC.V), KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                 KC.TRNS  
    ],
    # labview text
    [
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.DOWN,  lv.qdvsrs, lv.qdwl, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
                                      KC.UP,   lv.escqd, KC.TRNS, lv.qdm1, lv.qdins, lv.qdvsr,  KC.TRNS, KC.TRNS, KC.TRNS, lv.qdgit 
    ],
    # labview macros
    [
        KC.TD(lv.qdg,lv.qdm),        KC.TD(lv.qdq,lv.qd1,lv.qd1s), KC.TD(lv.qdw,lv.qdy,lv.qd9),             KC.TD(lv.cprop, lv.cref, lv.cinv),  KC.TD(lv.qdp,lv.qdps,lv.qdu), KC.TD(lv.qdr,lv.qdrs,lv.qdreq,lv.qdreqs),                                                                        KC.LCTL(KC.W), CTLSFT(KC.DOT), CTLSFT(KC.DOWN),  CTLSFT(KC.F),  KC.LCTL(KC.F),  KC.LCTL(KC.L),  
        KC.TD(lv.qdv,lv.qdk,lv.qd0), KC.TD(lv.qda,lv.qdas,lv.qdo), KC.TD(KC.LCTL(KC.U), KC.LCTL(KC.B)),     lv.EXPND,                           lv.qdtxt,                     KC.TD(lv.qds,lv.qdss,lv.qdb),                                                                                    CTLSFT(KC.E),  KC.LCTL(KC.N),  CTLSFT(KC.RIGHT), KC.LCTL(KC.I), KC.LCTL(KC.O),  KC.LCTL(KC.H),  
        KC.TD(lv.qd2,lv.qdj,lv.qde), KC.TD(lv.qdz,lv.qdl,lv.qdi),  KC.TD(lv.qdx,lv.qd3,lv.qd8),             lv.CLPSE,                           KC.TD(lv.qdd,lv.qdds,lv.qdh), KC.TD(lv.alignr,lv.alignl,lv.alignb,lv.align), KC.OS(KC.MO(2)), KC.LCTL(KC.E),     KC.LCTL(KC.ENT),    KC.TO(0), KC.LCTL(KC.M), CTLSFT(KC.S),   CTLSFT(KC.UP),    CTLSFT(KC.W),  KC.LCTL(KC.Z),  KC.LCTL(KC.S),  
                                                                                                            KC.LCTL(KC.R),                      KC.ESC,                       KC.BSPC,                                       KC.TG(3),        KC.TG(1),          CTLSFT(KC.G),       KC.TRNS,  KC.LCTL(KC.G), KC.TRNS,        CTLSFT(KC.Z)   
    ],
]

if __name__ == '__main__':
    keyboard.go()
