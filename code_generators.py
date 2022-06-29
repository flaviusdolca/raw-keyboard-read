def generate_key_code_dict(event_codes_file_path="/usr/include/linux/input-event-codes.h"):
    codes = {}
    with open(event_codes_file_path) as fp:
        for line in fp:
            if "#define" in line and "KEY_" in line:
                code, num = line.split()[1:3]
                codes[code] = num
    return codes


def generate_enum_file():
    codes = generate_key_code_dict()

    file_content = ""
    with open("./key_codes.py", "w") as enum_file:
        file_content += "from enum import Enum\n"
        file_content += "class KeyCodes(Enum):\n"
        for key in codes:
            try:
                file_content += f"\t{key} =  {int(codes[key], base=0)}\n"
            except ValueError:
                if "_MAX" in codes[key]:
                    continue
                file_content += f"\t{key} =  {int(codes[codes[key]], base=0)}\n"
        enum_file.write(file_content)
    return codes
