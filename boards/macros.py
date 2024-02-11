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
        self.pastee = simple_key_sequence(
            (
                KC.LCTL(KC.V),
                KC.ENT,
            )
        ) 
        self.PASTE = KC.LCTL(KC.V)
        self.UNDO = KC.LCTL(KC.Z)
        # open new tab, paste and enter
        self.NEWTAB = simple_key_sequence(
            (
                KC.LCTL(KC.T),
                KC.LCTL(KC.V),
                KC.ENT,
            )
        )
        self.MAXWIN = KC.LGUI(KC.UP)
        self.RHTWIN = KC.LGUI(KC.UP)
        self.LFTWIN = KC.LGUI(KC.UP)
        self.LPBK = KC.TD(KC.LPRN, KC.LBRC)
        self.RPBK = KC.TD(KC.RPRN, KC.RBRC)
        self.CURLY = KC.TD(KC.LCBR, KC.RCBR)
        self.COMM = KC.TD(KC.COMM, KC.LABK)
        self.DOT = KC.TD(KC.DOT, KC.RABK)
        self.SLASH = KC.TD(KC.SLSH, KC.QUES)
        self.A = KC.HT(KC.A, KC.LSHIFT)
        self.H = KC.HT(KC.H, KC.LSHIFT)