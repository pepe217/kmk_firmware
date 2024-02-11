# disables the usb storage on startup

import storage, usb_cdc
storage.disable_usb_drive()
usb_cdc.disable()
