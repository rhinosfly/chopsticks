# A GENERAL REUSABLE INTERACTIVE SHELL, THAT CAN CALL COMMANDS FROM CMD_DICT

EXIT = 0

def Exit():
    global EXIT
    EXIT ^= 1

def shell(cmd_dict):
    global EXIT
    PROMT_STRING = "> "
    cmd_dict["exit"] = Exit
    cmd_dict["quit"] = Exit 

    while not EXIT:
        try:
            input_string = input(PROMT_STRING)
        except EOFError:
            print("exit")
            break
        if input_string in cmd_dict:
            cmd_dict[input_string]()
        elif input_string:
            print("\""+input_string+"\" not recognized")
    return 0
