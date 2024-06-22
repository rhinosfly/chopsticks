import chopsticks
import init
import files
import play

X=123
position_list = init.Fill_list()

print(len(position_list))
init.Link_list(position_list)
print(str(position_list[X].index) + "\t" + str(position_list[X]))
for x in position_list[X].flinks:
    print(str(x))
#files.write(position_list)
play.play()
