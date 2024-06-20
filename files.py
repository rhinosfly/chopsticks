#write list into .md files for obsidian to display

import chopsticks as cs

def write(position_list):
    for position in position_list:
        newfile = open("/home/linus/documents/obsidian/chopsticks/" + str(position)[1:-1] + ".md", "w")
        for link in position.flinks:
            newfile.write("[" + str(link) + "]")
