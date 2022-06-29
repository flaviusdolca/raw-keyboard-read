from dataclasses import dataclass
from key_codes import KeyCodes


@dataclass
class Modifier:
    left: bool = False
    right: bool = False

    def __bool__(self):
        return self.left or self.right


@dataclass
class KeyboardState:

    is_shift_pressed: Modifier = Modifier()
    is_control_pressed: Modifier = Modifier()
    is_alt_pressed: Modifier = Modifier()
    is_capslock: bool = False

    def manage_state(self, key_code, is_pressed):
        if key_code == KeyCodes.KEY_RIGHTSHIFT:
            self.is_shift_pressed.right = is_pressed
        if key_code == KeyCodes.KEY_LEFTSHIFT:
            self.is_shift_pressed.left = is_pressed

        if key_code == KeyCodes.KEY_RIGHTCTRL:
            self.is_control_pressed.right = is_pressed
        if key_code == KeyCodes.KEY_LEFTCTRL:
            self.is_control_pressed.left = is_pressed

        if key_code == KeyCodes.KEY_RIGHTALT:
            self.is_alt_pressed.right = is_pressed
        if key_code == KeyCodes.KEY_LEFTALT:
            self.is_alt_pressed.left = is_pressed

        if key_code == KeyCodes.KEY_CAPSLOCK and is_pressed:
            self.is_capslock = not state.is_capslock
