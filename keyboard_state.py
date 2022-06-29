from dataclasses import dataclass

@dataclass
class KeyboardState:
    is_shift_pressed: bool = False
    is_capslock:bool = False
    is_control_pressed:bool= False
    is_alt_pressed:bool= False

    def manage_state(self, key_code, is_pressed):
        if key_code in ["KEY_RIGHTSHIFT", "KEY_LEFTSHIFT"]:
            self.is_shift_pressed = is_pressed

        if key_code in ["KEY_LEFTCTRL", "KEY_RIGHTCTRL"]:
            self.is_control_pressed = is_pressed

        if key_code in ["KEY_LEFTALT", "KEY_RIGHTALT"]:
            self.is_alt_pressed = is_pressed

        if key_code == "KEY_CAPSLOCK" and is_pressed:
            self.is_capslock = not state.is_capslock
