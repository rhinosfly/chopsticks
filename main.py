import init
import files

X=224
position_list = init.Fill_list()

print(len(position_list))
init.Link_list(position_list)
print("\t"+str(position_list[X]))
for x in position_list[X].flinks:
    print(str(x))
files.write(position_list)
