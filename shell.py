# A GENERAL REUSABLE INTERACTIVE SHELL, THAT CAN CALL COMMANDS FROM CMD_DICT

def shell(cmd_dict):
    PROMT_STRING = "> "
    EXIT = 0
    
    while not EXIT:
        input_string = input(PROMT_STRING)
        if input_string in cmd_dict:
            print("command: ",end = "")
        elif input_string:
            print("\""+input_string+"\" not recognized")
    return 0
