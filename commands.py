#DICTIONARY OF SHELL COMMANDS


from init import Init_list
import chopsticks as cs
import files


def Startup(arg_list):
    print("Do you want to play a game?")
    while True:
        try:
            input_string = input("y/n: ")
        except EOFError:
            break
        if input_string == 'n':
            print("too bad...")
            return 1
        if input_string == 'y':
            print("excellent...")
            return 0
        else:
            print("stoooobid!")
            continue

def Play(arg_list):
    if Startup(None):
        return 1
    position_list = Init_list()
    cs.Print_list(position_list)
        
def Echo(args):
    for x in args[1:]:
        print(x, end=" ")
    print()
    
#dicitonary assigns strings to functions to call from shell
dictionary = {
    "echo" : Echo,
    "play" : Play
}
