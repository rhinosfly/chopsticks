#chopsticks engine; working get_passive_flinks()

FINGER_NUMBER = 5

class Position:
    def __init__(self, gl, gr, rl, rr):
        self.gl = gl
        self.gr = gr
        self.rl = rl
        self.rr = rr
        self.flinks = []
        self.blinks = []
    def __str__(self):
        return "[{}, {}, {}, {}]".format(self.gl, self.gr, self.rl, self.rr)


def Fill_list(position_list):	#checked
    list_len = 0
    for i in range(FINGER_NUMBER):
        for j in range(i+1):
            for k in range(FINGER_NUMBER):
                for l in range(k+1):
                    position_list.append(Position(i,j,k,l))
                    list_len += 1
    return list_len


def roundup(x):
    xint = int(x)
    if xint < x:
        return xint + 1
    else:
        return xint


def Get_passive_flinks(position):	#checked
    links = []
    #FIND LIST
    total = position.gl + position.gr
    for x in range(roundup(total/2.0), total + 1):
        if not position.gl == x%5:
            links.append(Position(x%5, (total - x)%5, position.rl, position.rr))
    return links


def Get_active_flinks(position):
    links = []
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
            pass
        #position.flinks.append(link)
         #   link_count += 1
    return link_count


def Print_list(position_list):	#chekced
    for position in position_list:
        print(str(position))


def Main():
    X=199
    position_list = []
    print(Fill_list(position_list))
    Link_list(position_list)
    print("\t"+str(position_list[X]))
    for x in position_list[X].flinks:
        print(str(x))
                                
Main()
