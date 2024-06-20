#write list into .md files for obsidian to display

import chopsticks as cs

def write(position_list):
    for position in position_list:
        newfile = open("/home/linus/documents/obsidian/chopsticks/" + str(position)[2:-2] + ".md", "w")
        newfile.write(str(position.index) + "\n")
        for link in position.flinks:
            newfile.write(str(link) + "\n")
    
