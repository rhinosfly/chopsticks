import chopsticks as cs

X=224
position_list = cs.Fill_list()

print(len(position_list))
cs.Link_list(position_list)
print("\t"+str(position_list[X]))
for x in position_list[X].flinks:
    print(str(x))
