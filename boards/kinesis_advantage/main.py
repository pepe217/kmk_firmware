from kmk.handlers.sequences import simple_key_sequence
from kmk.keys import KC
from ka_kint import KMKeyboard
from macros import CommonMacros
from kmk.modules.layers import Layers as _Layers
from kmk.extensions.rgb import RGB
from kmk.extensions.lock_status import LockStatus

keyboard = KMKeyboard()
# rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin,
#           num_pixels=4,
#           hue_default=0,
#           sat_default=0,
#           val_default=0)

# class LEDLockStatus(LockStatus):

#     def set_lock_leds(self):
#         if self.get_caps_lock():
#             rgb.set_rgb((0, 255, 0), 0)
#         else:
#             rgb.set_rgb((0, 0, 0), 0)

#         if self.get_scroll_lock():
#             rgb.set_rgb((0, 255, 0), 1)
#         else:
#             rgb.set_rgb((0, 0, 0), 1)

#         if self.get_num_lock():
#             rgb.set_rgb((0, 255, 0), 2)
#         else:
#             rgb.set_rgb((0, 0, 0), 2)

#     def after_hid_send(self, sandbox):
#         super().after_hid_send(sandbox)  # Critically important. Do not forget
#         if self.report_updated:
#             self.set_lock_leds()

# class Layers(_Layers):
#     last_top_layer = 0
#     rgb_layers = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

#     def after_hid_send(self, keyboard):
#         if keyboard.active_layers[0] != self.last_top_layer:
#             self.last_top_layer = keyboard.active_layers[0]
#             # one pin for active layer, others are caps/scroll/num
#             rgb.set_rgb(self.rgb_layers[self.last_top_layer], 3)
#             # need to manually force a refresh
#             rgb.show()

# keyboard.extensions.append(rgb)
# keyboard.extensions.append(LEDLockStatus)

# *2 for split keyboards, which will typically manage twice the number of keys
# of one side. Having this N too large will have no impact (maybe slower boot..)
N = len(keyboard.col_pins) * len(keyboard.row_pins) * 2

keyboard.coord_mapping = list(range(N))

layer = []

for i in range(N):
    c, r = divmod(i, 100)
    d, u = divmod(r, 10)
    layer.append(
        simple_key_sequence((
            getattr(KC, 'N' + str(c)),
            getattr(KC, 'N' + str(d)),
            getattr(KC, 'N' + str(u)),
            KC.SPC,
        )))
keyboard.keymap = [layer]

if __name__ == '__main__':
    keyboard.go()
