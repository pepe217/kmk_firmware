from kmk.handlers.sequences import simple_key_sequence


class CommonMacros:

    def __init__(self, KC):
        self.GUIOS = KC.HT(KC.OS(KC.LM(2, KC.LGUI)), KC.LGUI)
        self.SALTAB = KC.SM(KC.TAB, KC.LALT)
        self.SCTLAB = KC.SM(KC.TAB, KC.LCTL)
        self.COLON = KC.TD(KC.COLON, KC.SCLN, KC.CW)
        self.PRN = KC.TD(KC.LPRN, KC.RPRN)
        self.EQLADD = KC.TD(KC.EQL, KC.PLUS)
        self.MINSU = KC.TD(KC.MINS, KC.UNDS)
        self.COMMA = KC.TD(KC.COMM, KC.LABK)
        self.UNDTAB = KC.LSFT(KC.LCLT(KC.T)),
        self.QUOTS = KC.TD(KC.QUOT, KC.DQT)
        #paste and enter
        self.PASTEE = simple_key_sequence((
            KC.LCTL(KC.V),
            KC.ENT,
        ))
        self.PASTE = KC.LCTL(KC.V)
        self.UNDO = KC.LCTL(KC.Z)
        self.CUT = KC.LCTL(KC.X)
        self.COPY = KC.LCTL(KC.C)
        # open new tab, paste and enter
        self.NWTABP = simple_key_sequence((
            KC.LCTL(KC.T),
            KC.LCTL(KC.V),
            KC.ENT,
        ))
        self.NEWTAB = KC.LCTL(KC.T)
        self.MAXWIN = KC.LGUI(KC.UP)
        self.RHTWIN = KC.LGUI(KC.RGHT)
        self.LFTWIN = KC.LGUI(KC.LEFT)
        self.LPBK = KC.TD(KC.LPRN, KC.LBRC)
        self.RPBK = KC.TD(KC.RPRN, KC.RBRC)
        self.CURLY = KC.TD(KC.LCBR, KC.RCBR)
        self.COMM = KC.TD(KC.COMM, KC.LABK)
        self.DOT = KC.TD(KC.DOT, KC.RABK)
        self.SLASH = KC.TD(KC.SLSH, KC.QUES)
        self.A = KC.HT(KC.A, KC.LSHIFT)
        self.H = KC.HT(KC.H, KC.LSHIFT)
        self.G1 = KC.LGUI(KC.N1)
        self.G2 = KC.LGUI(KC.N2)
        self.G3 = KC.LGUI(KC.N3)
        self.G4 = KC.LGUI(KC.N4)
        self.G5 = KC.LGUI(KC.N5)
        self.G6 = KC.LGUI(KC.N6)
        self.G7 = KC.LGUI(KC.N7)
        self.G8 = KC.LGUI(KC.N8)
        self.G9 = KC.LGUI(KC.N9)
        self.ALTAB = KC.LALT(KC.TAB)
        self.CTLAB = KC.LCTL(KC.TAB)
