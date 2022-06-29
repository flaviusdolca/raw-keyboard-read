#!/usr/bin/python
import struct
import sys
from utils import get_keyboard_event, format_key_code, NoKeyboardFound
from keyboard_state import KeyboardState
from key_codes import KeyCodes


def main():
    state = KeyboardState()
    try:
        eventCode = get_keyboard_event()
    except NoKeyboardFound:
        sys.exit("No keyboard found")

    infile_path = "/dev/input/" + eventCode

    FORMAT = "llHHI"
    EVENT_SIZE = struct.calcsize(FORMAT)

    with open(infile_path, "rb") as event_file:
        while event := event_file.read(EVENT_SIZE):
            tv_sec, tv_usec, type, code, value = struct.unpack(FORMAT, event)
            is_separator_event = type == 0 and code == 0 and value == 0
            is_key_pressed = value in [1, 2]
            is_key_released = value == 0
            is_key_event_type = type == 1

            if is_separator_event:
                continue

            key_code = KeyCodes(code)

            # print("Event type %u, code %s, value %u at %d.%d" % \
            #    (type, KeyCodes(code).name, value, tv_sec, tv_usec))
            if is_key_event_type and is_key_pressed:
                # print(KeyCodes(code).name)
                state.manage_state(key_code, True)
                output_key = format_key_code(state, key_code)
                print(output_key, end="", flush=True)
            elif is_key_event_type and is_key_released:
                state.manage_state(key_code, False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.")
