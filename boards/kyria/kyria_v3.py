from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic
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
    data_pin2 = pins[25]
    rgb_pixel_pin = pins[0]
    encoder_pin_0 = pins[19]
    encoder_pin_1 = pins[18]

    coord_mapping = []
    #top row
    coord_mapping.extend(ic(0, x, 7) for x in range(6,0,-1))
    coord_mapping.extend(ic(4, x, 7) for x in range(1,7))
    #second from top
    coord_mapping.extend(ic(1, x, 7) for x in range(6,0,-1))
    coord_mapping.extend(ic(5, x, 7) for x in range(1,7))
    #third from top
    coord_mapping.extend(ic(2, x, 7) for x in range(6,0,-1))
    coord_mapping.extend(ic(3, x, 7) for x in range(3,4))
    coord_mapping.extend(ic(2, x, 7) for x in range(1))
    coord_mapping.extend(ic(6, x, 7) for x in range(1))
    coord_mapping.extend(ic(7, x, 7) for x in range(3,4))
    coord_mapping.extend(ic(6, x, 7) for x in range(1,7))
    #bottom
    coord_mapping.extend(ic(3, x, 7) for x in range(4,5))
    coord_mapping.extend(ic(3, x, 7) for x in range(2,0,-1))
    coord_mapping.extend(ic(3, x, 7) for x in range(5,6))
    coord_mapping.extend(ic(3, x, 7) for x in range(1))
    coord_mapping.extend(ic(7, x, 7) for x in range(1))
    coord_mapping.extend(ic(7, x, 7) for x in range(5,6))
    coord_mapping.extend(ic(7, x, 7) for x in range(1,3))
    coord_mapping.extend(ic(7, x, 7) for x in range(4,5))
