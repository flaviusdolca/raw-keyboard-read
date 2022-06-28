#!/usr/bin/python
import struct
import sys
from utils import generate_key_code_dict, get_keyboard_event, NoKeyboardFound


def format_key_code(state, key_code):
    ALPHANUMERIC_KEY_CODE_SIZE = 5
    output_key = ""

    if key_code == "KEY_SPACE":
        output_key = " "
    if key_code == "KEY_BACKSPACE":
        output_key = "\b" + " " + "\b"
    if key_code == "KEY_ENTER":
        output_key = "\n"

    if len(key_code) == ALPHANUMERIC_KEY_CODE_SIZE:
        output_key = key_code[-1].lower()

        if state["isControlPressed"]:
            output_key = f" [CTRL + {output_key} ] "

        if state["isAltPressed"]:
            output_key = f" [ALT + {output_key} ] "

        if state["isShiftPressed"]:
            output_key = output_key.upper()

        if state["isCapsLock"]:
            output_key = output_key.upper()
    return output_key


def manage_state(state, key_code, isPressed):
    if key_code in ["KEY_RIGHTSHIFT", "KEY_LEFTSHIFT"]:
        state["isShiftPressed"] = isPressed

    if key_code in ["KEY_LEFTCTRL", "KEY_RIGHTCTRL"]:
        state["isControlPressed"] = isPressed

    if key_code in ["KEY_LEFTALT", "KEY_RIGHTALT"]:
        state["isAltPressed"] = isPressed

    if key_code == "KEY_CAPSLOCK" and isPressed:
        state["isCapsLock"] = not state["isCapsLock"]


def main():
    state = {
        "isShiftPressed": False,
        "isCapsLock": False,
        "isControlPressed": False,
        "isAltPressed": False,
    }

    codes_dict = generate_key_code_dict()

    try:
        eventCode = get_keyboard_event()
    except NoKeyboardFound:
        print("No keyboard found")
        sys.exit()

    infile_path = "/dev/input/" + eventCode

    FORMAT = "llHHI"
    EVENT_SIZE = struct.calcsize(FORMAT)

    with open(infile_path, "rb") as event_file:
        while event := event_file.read(EVENT_SIZE):
            tv_sec, tv_usec, type, code, value = struct.unpack(FORMAT, event)
            is_key_pressed = True if (value == 1 or value == 2) else False
            is_key_released = True if value == 0 else False
            is_key_event_type = True if type == 1 else False

            # Events with code, type and value == 0 are "separator" events
            if type != 0 or code != 0 or value != 0:
                key_code = codes_dict.get(str(code))
                # print("Event type %u, code %s, value %u at %d.%d" % \
                #    (type, codes_dict.get(str(code)), value, tv_sec, tv_usec))
                if is_key_event_type and is_key_pressed:
                    # print(codes_dict.get(str(code)))
                    manage_state(state, key_code, True)
                    output_key = format_key_code(state, key_code)
                    print(output_key, end="", flush=True)
                elif is_key_event_type and is_key_released:
                    manage_state(state, key_code, False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.")
