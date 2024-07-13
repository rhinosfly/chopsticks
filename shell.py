# A GENERAL REUSABLE INTERACTIVE SHELL, THAT CAN CALL COMMANDS FROM CMD_DICT

EXIT = 0
PROMT_STRING = "> "
    
def Get_arguments():
    input_string = input()
    arg_list = input_string.split()
    return arg_list

def Shell(cmd_dict):
    global EXIT
    global PROMT_STRING

    while not EXIT:
        try:
            print(PROMT_STRING, end = "")
            arg_list = Get_arguments()
        except EOFError:
            break

        if not len(arg_list):
            continue
        elif arg_list[0] in cmd_dict:
            cmd_dict[arg_list[0]](arg_list)
        else:
            print("shell: " + arg_list[0] + ": command not found")
    return 0
