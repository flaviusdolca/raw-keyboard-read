from key_codes import KeyCodes


class NoKeyboardFound(RuntimeError):
    pass


def get_keyboard_event():
    keyboard_code = "EV=120013"
    section = ""
    with open("/proc/bus/input/devices", "r") as fp:
        for line in fp:
            if line.strip() == "":
                if keyboard_code in section:
                    rows = section.split("\n")
                    for section_row in rows:
                        if "Handlers=" in section_row:
                            handlers = section_row.strip().split()
                            return handlers[-1]
                section = ""
            else:
                section += line
    raise NoKeyboardFound()


def format_key_code(state, key_code):
    ALPHANUMERIC_KEY_CODE_SIZE = 5
    output_key = "[UNKNOWN_KEY]"

    if key_code == KeyCodes.KEY_SPACE:
        output_key = " "
    if key_code == KeyCodes.KEY_BACKSPACE:
        output_key = "[\\b]"
    if key_code == KeyCodes.KEY_ENTER:
        output_key = "\n"
    if key_code == KeyCodes.KEY_TAB:
        output_key = "[\\t]"
    if key_code == KeyCodes.KEY_DOT:
        output_key = "." if not state.is_shift_pressed else ":"
    if key_code == KeyCodes.KEY_COMMA:
        output_key = "," if not state.is_shift_pressed else ";"
    if key_code in [KeyCodes.KEY_LEFTSHIFT, KeyCodes.KEY_RIGHTSHIFT, KeyCodes.KEY_LEFTCTRL, KeyCodes.KEY_RIGHTCTRL, KeyCodes.KEY_LEFTALT, KeyCodes.KEY_RIGHTALT]:
        output_key = ""

    if len(key_code.name) == ALPHANUMERIC_KEY_CODE_SIZE:
        output_key = key_code.name[-1].lower()

        if state.is_control_pressed:
            output_key = f" [CTRL + {output_key} ] "

        if state.is_alt_pressed:
            output_key = f" [ALT + {output_key} ] "

        if state.is_shift_pressed:
            output_key = output_key.upper()

        if state.is_capslock:
            output_key = output_key.upper()
    return output_key
