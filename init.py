import chopsticks as cs

def Fill_list(position_list):
    list_len = 0
    for i in range(cs.FINGER_NUMBER):
        for j in range(i+1):
            for k in range(cs.FINGER_NUMBER):
                for l in range(k+1):
                    position_list.append(cs.Position(i,j,k,l))
                    position_list[list_len].index = list_len
                    list_len += 1
    return list_len

def Get_passive_flinks(position):	#checked
    links = []
    #FIND LIST
    total = position.gl + position.gr
    for x in range(cs.roundup(total/2.0), total + 1):
        if not position.gl == x%5:
            links.append(cs.Position(x%5, (total - x)%5, position.rl, position.rr))
    return links
                
def Get_active_flinks(position):
    links = []
    for x in range(4):
        links.append(position.copy())
    links[0].rl += position.gl
    links[1].rr += position.gl
    links[2].rl += position.gr
    links[3].rr += position.gr
    return links



def Link_list(position_list):
    link_count = 0
    for position in position_list:
        #passive moves
        for link in Get_passive_flinks(position):
            position.flinks.append(link)
            link_count += 1
        #active moves
        for link in Get_active_flinks(position):
            position.flinks.append(link)
            link_count += 1
        #correct & clean
        for x in position.flinks:
            x.correct()
        cs.clean_list(position, position.flinks)
        for x in position.flinks:
            x.flip()
    return link_count


def Init_list():
    position_list = []
    Fill_list(position_list)
    Link_list(position_list)
    return position_list
