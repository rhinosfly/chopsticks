#DICTIONARY OF SHELL COMMANDS


from init import Init_list
import chopsticks as cs
import files


def Startup():
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

def Play(arg, var):
    if Startup():
        return 1
    position_list = Init_list()
    cs.Print_list(position_list)
        
def Echo(arg, var):
    for x in arg[1:]:
        print(x, end=" ")
    print()
    
#dicitonary assigns strings to functions to call from shell
functions = {
    "echo" : Echo,
    "play" : Play
}

#dicitonary assigns strings to values to use from shell
variables = {
}
