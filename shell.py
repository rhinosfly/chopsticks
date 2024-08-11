# A GENERAL REUSABLE INTERACTIVE SHELL, THAT CAN CALL COMMANDS FROM CMD_DICT, AND VARIABLES FROM VAR_DICT

EXIT = 0
PROMT_STRING = "> "
    
def Get_arguments(var_dict):
    input_string = input()
    arg_list = input_string.split()
    for i in range(len(arg_list)):  #replace variables with values
        if arg_list[i][0] == "$":
            if arg_list[i][1:] in var_dict:
                arg_list[i] = var_dict[arg_list[i][1:]]
            else:
                print("shell: " + arg_list[i][1:] + ":variable not found")
    return arg_list

def Shell(cmd_dict, var_dict):
    global EXIT
    global PROMT_STRING

    while not EXIT:
        try:
            print(PROMT_STRING, end = "")
            arg_list = Get_arguments(var_dict)
        except EOFError:
            print("")
            break
        if not len(arg_list):       #continue if there's no input
            continue
        if "=" in arg_list[0]:		#add variable if there's an '='
            index = arg_list[0].find('=')
            var_dict[arg_list[0][:index]] = arg_list[0][index+1:]
        elif arg_list[0] in cmd_dict: #run if it's a command
            cmd_dict[arg_list[0]](arg_list, var_dict)
        else:                       #error if unrecognized
            print("shell: " + arg_list[0] + ": command not found")
    return 0
