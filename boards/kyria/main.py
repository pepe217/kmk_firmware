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
from storage import getmount
from kmk.handlers.sequences import simple_key_sequence
# from labviewmacros import LabviewMacros

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

# General macros
SFTOS = KC.OS(KC.LSHIFT, tap_time=1500)
GUIOS = KC.HT(KC.OS(KC.LM(2, KC.LGUI)), KC.LGUI)
CTLSFT = KC.LSHIFT(KC.LCTL)
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
COLON = KC.TD(KC.COLON, KC.SCLN, KC.CW)
PRN = KC.TD(KC.LPRN, KC.RPRN)
EQLADD = KC.TD(KC.EQL, KC.PLUS)
MINSU = KC.TD(KC.MINS, KC.UNDS)
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
# open new tab, paste and enter
newtab = simple_key_sequence(
    (
        KC.LCTL(KC.T),
        KC.LCTL(KC.V),
        KC.ENT,
        KC.TG(3)
    )
)
maximize = simple_key_sequence(
     (
        KC.LGUI(KC.UP),
        KC.TG(3)
     )
)
paste_gbc = simple_key_sequence(
     (
        KC.F3,
        KC.MACRO_SLEEP_MS(50),
        KC.LCTL(KC.V),
	    KC.ENT,
     )
)
paste_xls = simple_key_sequence(
     (
        KC.LCTL(KC.V),
        KC.DOWN,
        KC.LCTL(KC.C),
     )
)
lpbk = KC.TD(KC.LPRN, KC.LBRC)
rpbk = KC.TD(KC.RPRN, KC.RBRC)
curly = KC.TD(KC.LCBR, KC.RCBR)
# lv = LabviewMacros(KC)
a = KC.HT(KC.A, KC.LSHIFT,)
h = KC.HT(KC.H, KC.LSHIFT,)
keyboard.keymap = [
    # 0 - base
    [
        ALTOS, KC.B,  KC.Y, KC.O,    KC.U,   QUOTS,                                                  COLON,   KC.L,   KC.D,   KC.W, KC.V, KC.Z,
        CTLOS, KC.C,  KC.I, KC.E,    a,      KC.COMM,                                                KC.DOT,  h,      KC.T,   KC.S, KC.N, KC.Q,
        GUIOS, KC.G,  KC.X, KC.J,    KC.K,   lpbk,    KC.OS(KC.MO(2)), KC.TG(1),  SFTOS,    KC.MINS, rpbk,    KC.R,   KC.M,   KC.F, KC.P, KC.CW,
                            curly,   KC.ESC, KC.BSPC, KC.TAB,          EQLADD,    KC.TG(3), KC.ENT,  KC.SPC,  KC.DEL, KC.SLSH 
    ],
    # 1 - keypad/function
    [
        KC.TRNS,  KC.F1, KC.F2,  KC.F3,   KC.F4,   KC.HOME,                                        KC.PSLS, KC.N7,   KC.N8, KC.N9, KC.PMNS, KC.PSCR,
        KC.TRNS,  KC.F5, KC.F6,  KC.F7,   KC.F8,   KC.END,                                         KC.PAST, KC.N4,   KC.N5, KC.N6, KC.PPLS, KC.PGUP,
        KC.TRNS,  KC.F9, KC.F10, KC.F11,  KC.F12,  KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.PEQL, KC.N1,   KC.N2, KC.N3, KC.NC,   KC.PGDN,
                                 KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.P0,   KC.TRNS, KC.PDOT
    ],
    # 2 - symbols
    [
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,   KC.PERC,                                        KC.CIRC, KC.AMPR,  KC.ASTR,  KC.LPRN, KC.RPRN,  KC.EQL,  
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,    KC.N5,                                          KC.N6,   KC.N7,    KC.N8,    KC.N9,   KC.N0,    KC.PLUS,  
        KC.PIPE, KC.BSLS, KC.COLN, KC.SCLN, KC.MINUS, KC.LBRC,  KC.NO,   KC.TG(2),  KC.TRNS, KC.CW,   KC.RBRC, KC.UNDS,  KC.COMMA, KC.DOT,  KC.SLASH, KC.QUES,  
                                   KC.TRNS, KC.TRNS,  KC.TRNS,  KC.DOWN, KC.UP,     KC.LCBR, KC.RCBR, KC.LEFT, KC.RIGHT, KC.PSCR
    ],
    # 3 - navigation
    [
        KC.LCTL(KC.L), KC.NO,   KC.NO,         KC.NO,         KC.NO,         newtab,                                         KC.TRNS, KC.LSFT(KC.LGUI(KC.UP)), KC.LSFT(KC.LGUI(KC.DOWN)), KC.LSFT(KC.LGUI(KC.RGHT)), KC.LSFT(KC.LGUI(KC.LEFT)), KC.LCTL(KC.L),  
        KC.LCTL(KC.Z), KC.LEFT, KC.RGHT,       KC.DOWN,       KC.UP,         rename,                                         KC.TRNS, KC.LCTL(KC.C),           KC.NO,                     KC.F4,                     KC.NO,                     KC.LALT(KC.TAB),  
        KC.TRNS,       undo,    KC.LCTL(KC.X), KC.LCTL(KC.C), paste,         pastee,  KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, maximize,                KC.LGUI(KC.DOWN),          KC.LGUI(KC.RGHT),          KC.LGUI(KC.LEFT),          KC.LCTL(KC.Z),  
                                               undtab,        KC.LCTL(KC.V), KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                 KC.TRNS  
    ],
    # # 4 - labview  quickdrop text input
    # [
    #     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                                           KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  lv.qdkleave,  
    #     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                                           KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  lv.iconTxt,  
    #     KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.DOWN,  KC.HT(lv.qdvsr, lv.qdvsrs),  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  lv.qdwl,  
    #                                   KC.UP,   lv.escqd, KC.TRNS, lv.qdm1, lv.qdins, KC.HT(lv.rnmlbl, lv.rnmcpt), lv.entqd, KC.TRNS, KC.TRNS, lv.qdgit 
    # ],
    # # 5 - labview macros base layer 
    # [
    #     lv.qdrs,   lv.qdr,    lv.qdss, lv.qdas,   KC.LCTL(KC.U), KC.OS(KC.MO(6), tap_time=3000),                                                    KC.LCTL(KC.W), CTLSFT(KC.DOT), CTLSFT(KC.DOWN),  CTLSFT(KC.F),  KC.LCTL(KC.F),   KC.LCTL(KC.L),  
    #     lv.alignb, lv.alignr, lv.qds,  lv.qda,    lv.qdtxt,      KC.OS(KC.MO(7), tap_time=3000),                                                    CTLSFT(KC.E),  KC.LCTL(KC.N),  CTLSFT(KC.RIGHT), KC.LCTL(KC.I), KC.LCTL(KC.O),   KC.LCTL(KC.H),  
    #     lv.alignt, lv.alignl, lv.qdx,  lv.delcln, lv.EXPND,      KC.OS(KC.MO(8), tap_time=3000), KC.OS(KC.MO(2)), KC.LCTL(KC.E), KC.TO(0), KC.TRNS, KC.LCTL(KC.M), CTLSFT(KC.S),   CTLSFT(KC.UP),    CTLSFT(KC.W),  KC.LCTL(KC.Z),   KC.LCTL(KC.S),  
    #                                    GUIOS,     KC.ESC,        KC.BSPC,                        KC.TG(3),        KC.TG(1),      KC.TO(0), KC.ENT,  KC.TRNS,       KC.TRNS,        KC.TRNS, 
    # ],
    # # 6 - labview macro layer
    # [
    #     lv.qdy, lv.qdu, lv.cref, lv.clcl, lv.cinv, lv.cprop,                                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     lv.qdt, lv.qdi, lv.qd3,  lv.qd1,  lv.qdk,  lv.qdz,                                        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     lv.qd8, lv.qdh, lv.qdj,  lv.qd1s, lv.qdb,  lv.qdv,  lv.tools, lv.align, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    #                              KC.TRNS, lv.qdgs, lv.qdi,  lv.qdl,   lv.qdls,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS   
    # ],
    # # 7 - labview macro layer 
    # [
    #     lv.qdreqs, lv.qdreq, lv.qdm,    lv.qdods, lv.qdp,  lv.qdps,                                        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     lv.qdw,    lv.qdg,   lv.qdodps, lv.qdnc,  lv.qdns, lv.qdn,                                         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     lv.qd2,    lv.qd9,   lv.qdodfs, lv.qdd,   lv.qdos, lv.qdo,   lv.qd0,  lv.rnmult, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    #                                     lv.qdks,  lv.qdds, lv.CLPSE, lv.pan,  lv.qdq,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS   
    # ],
    # # 8 - labview macro layer
    # [
    #     KC.LCTL(KC.W), CTLSFT(KC.DOT), CTLSFT(KC.DOWN),  CTLSFT(KC.F),  KC.LCTL(KC.F),   KC.LCTL(KC.L),                                                KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     CTLSFT(KC.E),  KC.LCTL(KC.N),  CTLSFT(KC.RIGHT), KC.LCTL(KC.I), KC.LCTL(KC.R),   KC.LCTL(KC.H),                                                KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  
    #     KC.LCTL(KC.M), KC.LCTL(KC.Z),  CTLSFT(KC.UP),    CTLSFT(KC.W),  CTLSFT(KC.S),    KC.LCTL(KC.S), KC.TRNS,       KC.TRNS,      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    #                                                      CTLSFT(KC.G),  KC.LCTL(KC.ENT), KC.LCTL(KC.G), KC.LCTL(KC.O), CTLSFT(KC.Z), KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    # ],
]

if __name__ == '__main__':
    keyboard.go()
