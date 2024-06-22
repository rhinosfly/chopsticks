#THE INTERACTIVE SHELL
#simple input output capability

def startup():
    print("Do you want to play a game?")
    while input_string := input("y/n: "):
        if input_string == 'n':
            print("too bad...")
            return 1
        if input_string == 'y':
            print("excellent...")
            return 0
        else:
            continue

def play():
    if startup() == 1:
        return 0
    while input_string := input("> "):
        print(input_string)
    return 0
