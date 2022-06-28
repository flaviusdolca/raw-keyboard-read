#!/usr/bin/python

def generate_key_code_dict(event_codes_file_path = "input-event-codes.h"):
    codes = {}
    with open(event_codes_file_path) as fp:
        for line in fp:
            if "#define" in line and "KEY_" in line:
                code, num = line.split()[1:3]
                codes[num] =  code 
    return codes

def get_keyboard_event():
    keyboard_code = "EV=120013"
    section = ""
    with open("/proc/bus/input/devices", "r") as fp:
        for line in fp:
            if line.strip() == "":
                if keyboard_code in section:
                    rows = section.split("\n")
                    for sectionRow in rows:
                        if "Handlers=" in sectionRow:
                            handlers = sectionRow.strip().split(' ')
                            return handlers[-1]
                section=""
            else:
                section +=line
    raise NoKeyboardFound()

class NoKeyboardFound(RuntimeError):
    pass