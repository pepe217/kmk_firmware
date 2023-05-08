from kmk.handlers.sequences import simple_key_sequence

# labview specific macros
class LabviewMacros:
    def __init__(self, KC) -> None:
        CTLSFT = KC.LSHIFT(KC.LCTL)
        self.MV10L = KC.LSHIFT(KC.LEFT)
        self.MV10U = KC.LSHIFT(KC.UP)
        self.MV10D = KC.LSHIFT(KC.DOWN)
        self.MV10R = KC.LSHIFT(KC.RIGHT)
        self.EXPNDM = KC.OS(KC.LCTL(KC.MB_LMB), tap_time=10000)
        self.CLPSEM = KC.OS(KC.LCTL(KC.LALT(KC.MB_LMB)), tap_time=10000)
        self.panm = KC.OS(KC.LCTL(KC.LSFT(KC.B_LMB)), tap_time=10000)
        self.EXPND = KC.OS(KC.LCTL)
        self.CLPSE = KC.OS(KC.LCTL(KC.LALT))
        self.QD = KC.LCTL(KC.SPACE)
        start_seq = simple_key_sequence(
                (
                    self.QD,
                    KC.MACRO_SLEEP_MS(200)
                )
            )
        self.qdreq = simple_key_sequence(
                (
                    start_seq,
                    KC.R,
                    KC.E,
                    KC.Q,
                    KC.LCTL(KC.R)
                )
            )
        self.qdreqs = simple_key_sequence(
                (
                    start_seq,
                    KC.R,
                    KC.E,
                    KC.Q,
                    CTLSFT(KC.R)
                )
            )
        self.qdr = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.R)
                )
            )
        self.qdrs = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.R)
                )
            )
        # self.qdd = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.D)
        #   )
        #     )
        # replace close qd with shortcut sequence, its faster
        self.qdd = simple_key_sequence(
                (
                    KC.LCTL(KC.S),
                    KC.LCTL(KC.E),
                    KC.LCTL(KC.W),
                )
            )
        self.qdds = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.D)
                )
            )
        self.qdt = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.T)
                )
            )
        # self.qdts = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.T)
        #         )
        #     )
        self.qdv = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.V)
                )
            )
        # self.qdvs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.V)
        #         )
        #     )
        self.qdg = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.G)
                )
            )
        # self.qdgs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.G)
        #         )
        #     )
        self.qdb = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.B)
                )
            )
        # self.qdbs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.B)
        #         )
        #     )
        self.qdp = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.P)
                )
            )
        self.qdps = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.P)
                )
            )
        # self.qdf = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.F)
        #         )
        #     )
        # self.qdfs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.F)
        #         )
        #     )
        # self.qdc = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.C)
        #         )
        #     )
        # self.qdcs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.C)
        #         )
        #     )
        self.qdw = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.W)
                )
            )
        # self.qdws = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.W)
        #         )
        #     )
        self.qdx = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.X)
                )
            )
        # self.qdxs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.X)
        #         )
        #     )
        self.qdq = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.Q)
                )
            )
        # self.qdqs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.Q)
        #         )
        #     )
        self.qda = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.A)
                )
            )
        self.qdas = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.A)
                )
            )
        self.qdz = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.Z)
                )
            )
        # self.qdzs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.Z)
        #         )
        #     )
        self.qd1 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N1)
                )
            )
        self.qd1s = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.N1)
                )
            )
        self.qd2 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N2)
                )
            )
        # self.qd2s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N2)
        #         )
        #     )
        self.qd3 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N3)
                )
            )
        # self.qd3s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N3)
        #         )
        #     )
        # self.qd4 = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.N4)
        #         )
        #     )
        # self.qd4s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N4)
        #         )
        #     )
        # self.qd5 = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.N5)
        #         )
        #     )
        # self.qd5s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N5)
        #         )
        #     )
        # self.qd6 = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.N6)
        #         )
        #     )
        # self.qd6s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N6)
        #         )
        #     )
        # self.qd7 = simple_key_sequence(
        #         (
        #             start_seq,
        #             KC.LCTL(KC.N7)
        #         )
        #     )
        # self.qd7s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N7)
        #         )
        #     )
        self.qd8 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N8)
                )
            )
        # self.qd8s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N8)
        #         )
        #     )
        self.qd9 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N9)
                )
            )
        # self.qd9s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N9)
        #         )
        #     )
        self.qd0 = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N0)
                )
            )
        # self.qd0s = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N0)
        #         )
        #     )
        self.qdj = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.J)
                )
            )
        # self.qdjs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.J)
        #         )
        #     )
        self.qdm = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.M)
                )
            )
        # self.qdms = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.M)
        #         )
        #     )
        self.qdk = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.K)
                )
            )
        # self.qdks = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.K)
        #         )
        #     )
        self.qdl = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.L)
                )
            )
        # self.qdls = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.L)
        #         )
        #     )
        self.qdn = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.N)
                )
            )
        # self.qdns = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.N)
        #         )
        #     )
        self.qdh = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.H)
                )
            )
        # self.qdhs = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.H)
        #         )
        #     )
        self.qdu = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.U)
                )
            )
        # self.qdus = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.U)
        #         )
        #     )
        self.qde = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.E)
                )
            )
        # self.qdes = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.E)
        #         )
        #     )
        self.qdy = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.Y)
                )
            )
        # self.qdys = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.Y)
        #         )
        #     )
        self.qdi = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.I)
                )
            )
        # self.qdis = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.I)
        #         )
        #     )
        self.qdo = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.O)
                )
            )
        # self.qdos = simple_key_sequence(
        #         (
        #             start_seq,
        #             CTLSFT(KC.O)
        #         )
        #     )
        self.qds = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.S)
                )
            )
        self.qdss = simple_key_sequence(
                (
                    start_seq,
                    CTLSFT(KC.S)
                )
            )
        #bring up quick drop & goto text input layer
        self.qdtxt = simple_key_sequence(
                (
                    self.QD,
                    KC.TG(5)
                )
            )
        #git quick drop & goto macro layer
        self.qdgit = simple_key_sequence(
                (
                    KC.LCTL(KC.N7),
                    KC.TG(5)
                )
            )
        #wire label quick drop & goto macro layer
        self.qdwl = simple_key_sequence(
                (
                    KC.LCTL(KC.N6),
                    KC.TG(5)
                )
            )
        #insert/replace object and goto macro layer
        self.qdins = simple_key_sequence(
                (
                    KC.LCTL(KC.N4),
                    KC.TG(5)
                )
            )
        #escape self.qd and back to macro
        self.escqd = simple_key_sequence(
                (
                    KC.ESC,
                    KC.TG(5)
                )
            )
        #shifted vi server rename
        self.qdvsrs = simple_key_sequence(
                (
                    CTLSFT(KC.N5),
                    KC.TG(5)
                )
            )
        #vi server rename
        self.qdvsr = simple_key_sequence(
                (
                    KC.LCTL(KC.N5),
                    KC.TG(5)
                )
            )
        #mouse 1 to insert object at cursor and goto macro layer
        self.qdm1 = simple_key_sequence(
                (
                    KC.MB_LMB,
                    KC.TG(5)
                )
            )
        #delete object and remove broken wires
        # self.delcln = simple_key_sequence(
        #     (
        #         KC.BSPC,
        #         KC.LCTL(KC.B)
        #     )
        # ) 
        #self.QD alignment and enter text entry 
        self.align = simple_key_sequence(
                (
                    start_seq,
                    KC.LCTL(KC.C),
                )
            )
        #self.QD alignment to left
        self.alignl = simple_key_sequence(
                (
                    start_seq,
                    KC.A,
                    KC.LCTL(KC.C),
                )
            )
        #self.QD alignment to bottom
        self.alignb = simple_key_sequence(
                (
                    start_seq,
                    KC.S,
                    KC.LCTL(KC.C),
                )
            )
        #self.QD alignment to right
        self.alignr = simple_key_sequence(
                (
                    start_seq,
                    KC.D,
                    KC.LCTL(KC.C),
                )
            )
        # create reference from selection
        self.cref = simple_key_sequence(
                (
                    start_seq,
                    KC.R,
                    KC.LCTL(KC.F),
                )
            )
        # create property node from selection
        self.cprop = simple_key_sequence(
                (
                    start_seq,
                    KC.P,
                    KC.LCTL(KC.F),
                )
            )
        # create invoke node from selection
        self.cinv = simple_key_sequence(
                (
                    start_seq,
                    KC.N,
                    KC.V,
                    KC.LCTL(KC.F),
                )
            )