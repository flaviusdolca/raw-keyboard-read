from dataclasses import dataclass
from key_codes import  KeyCodes

@dataclass
class KeyboardState:
    is_rshift_pressed: bool = False
    is_lshift_pressed: bool = False

    is_rcontrol_pressed:bool= False
    is_lcontrol_pressed:bool= False

    is_ralt_pressed:bool= False
    is_lalt_pressed:bool= False

    is_capslock:bool = False

    @property
    def is_shift_pressed(self):
        return self.is_rshift_pressed or self.is_lshift_pressed

    @property
    def is_control_pressed(self):
        return self.is_rcontrol_pressed or self.is_lcontrol_pressed

    @property
    def is_alt_pressed(self):
        return self.is_ralt_pressed or self.is_lalt_pressed
    
    def manage_state(self, key_code, is_pressed):
        if key_code == KeyCodes.KEY_RIGHTSHIFT :
            self.is_rshift_pressed = is_pressed
        if key_code == KeyCodes.KEY_LEFTSHIFT :
            self.is_lshift_pressed = is_pressed

        if key_code == KeyCodes.KEY_RIGHTCTRL:
            self.is_rcontrol_pressed = is_pressed
        if key_code == KeyCodes.KEY_LEFTCTRL:
            self.is_lcontrol_pressed = is_pressed

        if key_code ==  KeyCodes.KEY_RIGHTALT:
            self.is_ralt_pressed = is_pressed
        if key_code ==  KeyCodes.KEY_LEFTALT:
            self.is_lalt_pressed = is_pressed

        if key_code == KeyCodes.KEY_CAPSLOCK and is_pressed:
            self.is_capslock = not state.is_capslock
