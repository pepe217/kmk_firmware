from kyria_v3 import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
# from kmk.modules.encoder import EncoderHandler
from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers as _Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.capsword import CapsWord
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from storage import getmount
from kmk.handlers.sequences import simple_key_sequence

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

# Uncomment below if you're using encoder
# encoder_handler = EncoderHandler()
# encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

# General macros
SFTOS = KC.OS(KC.LSHIFT, tap_time=None)
GUIOS = KC.OS(KC.LM(2, KC.LGUI))
CTLOS = KC.OS(KC.LCTL)
ALTOS = KC.OS(KC.LALT)
CTLSFT = KC.LSHIFT(KC.LCTL)
CMDSFT = KC.LSHIFT(KC.LGUI)
COLON = KC.TD(KC.COLON, KC.SCLN, KC.CW)
BRACES = KC.TD(KC.LBRC, KC.RBRC)
CBRACES = KC.TD(KC.LCBR, KC.RCBR)
PRN = KC.TD(KC.LPRN, KC.RPRN)
EQLADD = KC.TD(KC.EQL, KC.PLUS)
MINSU = KC.TD(KC.MINS, KC.UNDS)
QUES = KC.TD(KC.SLSH, KC.QUES)
PERD = KC.TD(KC.DOT, KC.RABK)
COMMA = KC.TD(KC.COMM, KC.LABK)
rename = simple_key_sequence((KC.F2, KC.TG(3)))
undtab = simple_key_sequence((CTLSFT(KC.T)))
#QUOTS = KC.TD(KC.QUOT, KC.DQT)
#labview specific macros
LVLYR = simple_key_sequence((KC.TG(4), KC.TG(5)))
MV10L = KC.LSHIFT(KC.LEFT)
MV10U = KC.LSHIFT(KC.UP)
MV10D = KC.LSHIFT(KC.DOWN)
MV10R = KC.LSHIFT(KC.RIGHT)
CLPSE = KC.OS(KC.LCTL(KC.LALT))
QD = KC.LCTL(KC.SPACE)
qd_start_seq = simple_key_sequence((QD, KC.MACRO_SLEEP_MS(100)
        )
    )
qdreq = simple_key_sequence(
        (
            qd_start_seq,
            KC.R,
            KC.E,
            KC.Q,
            KC.LCTL(KC.R)
        )
    )
qdreqs = simple_key_sequence(
        (
            qd_start_seq,
            KC.R,
            KC.E,
            KC.Q,
            CTLSFT(KC.R)
        )
    )
qdr = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.R)
        )
    )
qdrs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.R)
        )
    )
qdd = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.D)
        )
    )
qdds = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.D)
        )
    )
qdt = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.T)
        )
    )
qdts = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.T)
        )
    )
qdv = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.V)
        )
    )
qdvs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.V)
        )
    )
qdg = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.G)
        )
    )
qdgs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.G)
        )
    )
qdb = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.B)
        )
    )
qdbs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.B)
        )
    )
qdp = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.P)
        )
    )
qdps = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.P)
        )
    )
qdf = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.F)
        )
    )
qdfs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.F)
        )
    )
qdc = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.C)
        )
    )
qdcs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.C)
        )
    )
qdw = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.W)
        )
    )
qdws = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.W)
        )
    )
qdx = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.X)
        )
    )
qdxs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.X)
        )
    )
qdq = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.Q)
        )
    )
qdqs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.Q)
        )
    )
qda = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.A)
        )
    )
qdas = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.A)
        )
    )
qdz = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.Z)
        )
    )
qdzs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.Z)
        )
    )
qd1 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N1)
        )
    )
qd1s = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.N1)
        )
    )
qd2 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N2)
        )
    )
# qd2s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N2)
#         )
#     )
qd3 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N3)
        )
    )
# qd3s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N3)
#         )
#     )
# qd4 = simple_key_sequence(
#         (
#             qd_start_seq,
#             KC.LCTL(KC.N4)
#         )
#     )
# qd4s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N4)
#         )
#     )
# qd5 = simple_key_sequence(
#         (
#             qd_start_seq,
#             KC.LCTL(KC.N5)
#         )
#     )
# qd5s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N5)
#         )
#     )
# qd6 = simple_key_sequence(
#         (
#             qd_start_seq,
#             KC.LCTL(KC.N6)
#         )
#     )
# qd6s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N6)
#         )
#     )
# qd7 = simple_key_sequence(
#         (
#             qd_start_seq,
#             KC.LCTL(KC.N7)
#         )
#     )
# qd7s = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.N7)
#         )
#     )
qd8 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N8)
        )
    )
qd8s = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.N8)
        )
    )
qd9 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N9)
        )
    )
qd9s = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.N9)
        )
    )
qd0 = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N0)
        )
    )
qd0s = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.N0)
        )
    )
qdj = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.J)
        )
    )
qdjs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.J)
        )
    )
qdm = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.M)
        )
    )
qdms = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.M)
        )
    )
qdk = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.K)
        )
    )
qdks = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.K)
        )
    )
qdl = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.L)
        )
    )
qdls = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.L)
        )
    )
qdn = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.N)
        )
    )
qdns = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.N)
        )
    )
qdh = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.H)
        )
    )
qdhs = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.H)
        )
    )
qdu = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.U)
        )
    )
# qdus = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.U)
#         )
#     )
qde = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.E)
        )
    )
qdes = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.E)
        )
    )
qdy = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.Y)
        )
    )
# qdys = simple_key_sequence(
#         (
#             qd_start_seq,
#             CTLSFT(KC.Y)
#         )
#     )
qdi = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.I)
        )
    )
qdis = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.I)
        )
    )
qdo = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.O)
        )
    )
qdos = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.O)
        )
    )
qds = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.S)
        )
    )
qdss = simple_key_sequence(
        (
            qd_start_seq,
            CTLSFT(KC.S)
        )
    )
#bring up quick drop & goto text input layer
qdtxt = simple_key_sequence(
        (
            QD,
            KC.TG(5)
        )
    )
#git quick drop & goto macro layer
qdgit = simple_key_sequence(
        (
            KC.LCTL(KC.N7),
            KC.TG(5)
        )
    )
#wire label quick drop & goto macro layer
qdwl = simple_key_sequence(
        (
            KC.LCTL(KC.N6),
            KC.TG(5)
        )
    )
#insert/replace object and goto macro layer
qdins = simple_key_sequence(
        (
            KC.LCTL(KC.N4),
            KC.TG(5)
        )
    )
#escape qd and back to macro
escqd = simple_key_sequence(
        (
            KC.ESC,
            KC.TG(5)
        )
    )
#shifted vi server rename
qdvsrs = simple_key_sequence(
        (
            CTLSFT(KC.N5),
            KC.TG(5)
        )
    )
#vi server rename
qdvsr = simple_key_sequence(
        (
            KC.LCTL(KC.N5),
            KC.TG(5)
        )
    )
#mouse 1 to insert object at cursor and goto macro layer
qdm1 = simple_key_sequence(
        (
            KC.MB_LMB,
            KC.TG(5)
        )
    )
#delete object and remove broken wires
delcln = simple_key_sequence(
    (
        KC.BSPC,
        KC.LCTL(KC.B)
    )
) 
#open and leave layer
openf = simple_key_sequence(
    (
        KC.LCTL(KC.O),
        KC.TG(3)
    )
) 
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
#save and leave layer
savef = simple_key_sequence(
    (
        KC.LCTL(KC.S),
        KC.TG(3)
    )
) 
#QD alignment and enter text entry 
align = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.C),
            KC.TG(5)
        )
    )
#QD alignment to left
alignl = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.C),
            KC.A,
            KC.ENT,
        )
    )
#QD alignment to bottom
alignb = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.C),
            KC.S,
            KC.ENT,
        )
    )
#QD alignment to right
alignr = simple_key_sequence(
        (
            qd_start_seq,
            KC.LCTL(KC.C),
            KC.D,
            KC.ENT,
        )
    )

keyboard.keymap = [
    # base
    [
        ALTOS,  KC.Q,  KC.W,    KC.F,  KC.P,    KC.B,                                                                  KC.J,   KC.L,   KC.U,    KC.Y,   KC.QUOT,  MINSU,
        CTLOS,  KC.A,  KC.R,    KC.S,  KC.T,    KC.G,                                                                  KC.M,   KC.N,   KC.E,    KC.I,   KC.O,    EQLADD,
        PRN,    KC.Z,  KC.X,    KC.C,  KC.D,    KC.V,    KC.OS(KC.MO(2)), KC.TD(LVLYR, KC.TO(0)),    COLON,    SFTOS,  KC.K,   KC.H,   COMMA,   PERD,   QUES,    BRACES,
                                GUIOS, KC.ESC,  KC.BSPC, KC.TG(3),        KC.TG(1),                  KC.TAB,   KC.ENT, KC.SPC, KC.DEL, CBRACES 
    ],
    # keypad/function
    [
        KC.TRNS,  KC.PMNS, KC.N7, KC.N8,   KC.N9,   KC.PSLS,                                                               KC.HOME, KC.F1,   KC.F2,  KC.F3,  KC.F4,  KC.PGUP,
        KC.TRNS,  KC.PDOT, KC.N4, KC.N5,   KC.N6,   KC.PAST,                                                               KC.END,  KC.F5,   KC.F6,  KC.F7,  KC.F8,  KC.PGDN,
        KC.TRNS,  KC.KPEQ, KC.N1, KC.N2,   KC.N3,   KC.PPLS, KC.TRNS, KC.TD(KC.TG(1), KC.TO(0)),   KC.OS(CTLSFT), KC.TRNS, KC.TRNS, KC.F9,   KC.F10, KC.F11, KC.F12, KC.PSCR,
                                  KC.P0,   KC.PDOT, KC.BSPC, KC.TRNS, KC.TRNS,                     KC.TRNS,       KC.TRNS, KC.LALT, KC.TRNS, KC.TRNS
    ],
    # symbols
    [
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,           KC.N4,    KC.N5,                                                           KC.N6,   KC.N7,    KC.N8,    KC.N9,   KC.N0,    KC.PLUS,  
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH,         KC.DLR,   KC.PERC,                                                         KC.CIRC, KC.AMPR,  KC.ASTR,  KC.LPRN, KC.RPRN,  KC.EQL,  
        KC.PIPE, KC.BSLS, KC.COLN, KC.SCLN,         KC.MINUS, KC.LBRC,  KC.TRNS, KC.TD(KC.TG(2), KC.TO(0)),  KC.TRNS, KC.CW,   KC.RBRC, KC.UNDS,  KC.COMMA, KC.DOT,  KC.SLASH, KC.QUES,  
                                   KC.OS(KC.LGUI),  KC.TRNS,  KC.TRNS,  KC.DOWN, KC.UP,                      KC.LCBR, KC.RCRB, KC.LEFT, KC.RIGHT, KC.PSCR  
    ],
    # navigation
    [
        KC.LCTL(KC.L), MV10L,   MV10R,         MV10D,         MV10U,                undtab,                                                          undtab,  MV10U,   MV10D,         MV10R,         MV10L,   KC.LCTL(KC.L),  
        KC.LCTL(KC.Z), KC.LEFT, KC.RGHT,       KC.DOWN,       KC.UP,                rename,                                                          rename,  KC.UP,   KC.DOWN,       KC.RGHT,       KC.LEFT, KC.LCTL(KC.Z),  
        openf,         undo,    KC.LCTL(KC.X), KC.LCTL(KC.C), KC.TD(paste, pastee), savef,   KC.TRNS, KC.TD(KC.TG(3), KC.TO(0)),   KC.TRNS, KC.TRNS, savef,   paste,   KC.LCTL(KC.C), KC.LCTL(KC.X), undo,    openf,  
                                               KC.TRNS,       KC.LCTL(KC.V),        KC.TRNS, KC.TRNS, KC.TRNS,                     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LCTL(KC.V)  
    ],
    # labview text
    [
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,                                         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.OS(KC.MO(2)),KC.DOWN,  qdvsrs, qdwl, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS,  KC.TRNS,  
                                      KC.UP,   escqd,    KC.TRNS, qdm1,           qdins,    qdvsr,        KC.TRNS, KC.TRNS, KC.TRNS, qdgit 
    ],
    # labview macros
    [
        KC.TD(qdg,qdm,qde), KC.TD(qdq,qd1,qd1s), KC.TD(qdw,qdy,qd9),                   KC.OS(KC.LCTL(KC.LSHIFT)), KC.TD(qdp,qdps,qdu), KC.TD(qds,qdss,qdb),                                                                            KC.LCTL(KC.O), CTLSFT(KC.DOT), CTLSFT(KC.DOWN),  CTLSFT(KC.F),  KC.LCTL(KC.F),   KC.LCTL(KC.L),  
        KC.TD(qdv,qdk,qd0), KC.TD(qda,qdas,qdo), KC.TD(KC.LCTL(KC.U),  KC.LCTL(KC.B)), CTLOS,                     qdtxt,               KC.TD(qdr,qdrs,qdreq,qdreqs),                                                                   CTLSFT(KC.E),  KC.LCTL(KC.N),  CTLSFT(KC.RIGHT), KC.LCTL(KC.I), KC.TRNS,         KC.LCTL(KC.H),  
        KC.TD(qd2,qdj,qdf), KC.TD(qdz,qdl,qdls), KC.TD(qdx,qd3,qd8),                   CLPSE,                     KC.TD(qdd,qdds,qdh), KC.TD(alignr,alignl,alignb),  KC.OS(KC.MO(2)), KC.LCTL(KC.E),     KC.LCTL(KC.ENT),    KC.TO(0), KC.LCTL(KC.M), CTLSFT(KC.S),   CTLSFT(KC.UP),    CTLSFT(KC.W),  KC.LCTL(KC.Z),   KC.LCTL(KC.S),  
                                                                                       KC.LCTL(KC.R),             KC.ESC,              KC.TD(KC.BSPC,delcln),        KC.TG(3),        KC.TG(1),          CTLSFT(KC.G),       KC.TRNS,  KC.LCTL(KC.G), KC.TRNS,        CTLSFT(KC.Z)   
    ],
]


# Uncomment below if using an encoder
# Edit your encoder layout below
# encoder_handler.map = (
#     ((KC.VOLD, KC.VOLU),),
#     ((KC.VOLD, KC.VOLU),),
#     ((KC.VOLD, KC.VOLU),),
#     ((KC.MPRV, KC.MNXT),),
#     ((KC.MPRV, KC.MNXT),),
#     ((KC.MPRV, KC.MNXT),),
#     ((KC.MPRV, KC.MNXT),),
# )
# keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
