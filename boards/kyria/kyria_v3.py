from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from storage import getmount
    
# Using drive names (KYRIAL, KYRIAR) to recognize sides b/c pinout is not symmetrical or mirrored 
lside = str(getmount('/').label)[-1] == 'L'
class KMKKeyboard(_KMKKeyboard):
    if lside:
        col_pins = (
            pins[10],
            pins[17],
            pins[16],
            pins[15],
            pins[14],
            pins[13],
            pins[12],
        )
        row_pins = (pins[6], pins[7], pins[8], pins[9])
    else:
        col_pins = (
            pins[13],
            pins[6],
            pins[7],
            pins[8],
            pins[9],
            pins[10],
            pins[12],
        )
        row_pins = (pins[17], pins[16], pins[15], pins[14])
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = pins[1]
    rgb_pixel_pin = pins[0]
    encoder_pin_0 = pins[19]
    encoder_pin_1 = pins[18]
    coord_mapping = [6, 5, 4, 3, 2, 1, 29, 30, 31, 32, 33, 34, 13, 12, 11, 10, 9, 8, 36, 37, 38, 39, 40, 41, 20, 19, 18, 17, 16, 15, 24, 14, 42, 52, 43, 44, 45, 46, 47, 48, 25, 23, 22, 26, 21, 49, 54, 50, 51, 53]