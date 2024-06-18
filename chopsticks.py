#chopsticks engine;

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
    def copy(self):	#CHECKED
        retval = Position(self.gl, self.gr, self.rl, self.rr)
        retval.flinks = self.flinks.copy()
        retval.blinks = self.blinks.copy()
        return retval
    def equals(self, other):	#CHEKED
        if self.gl == other.gl and self.gr == other.gr and self.rl == other.rl and self.rr == other.rr:
            return True
        else:
            return False


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



def check_position(p): #p == position; CHECKED
    p.gl %= FINGER_NUMBER
    p.gr %= FINGER_NUMBER
    p.rl %= FINGER_NUMBER
    p.rr %= FINGER_NUMBER
    if p.gr > p.gl:
        tmp = p.gr
        p.gr = p.gl
        p.gl = tmp
    if p.rr > p.rl:
        tmp = p.rr
        p.rr = p.rl
        p.rl = tmp
        

def clean_list(position, links):
    global len
    deletions = []	#links to delete
    retlist = []	#final list
    #get deletions
    for i in links: #remove links to self
        if i.equals(position):
            deletions.append(i)
    length = len(links)	#remove duplicates
    for i in range(length-1):
        for j in range(i+1,length):
            if links[i].equals(links[j]):
                deletions.append(links[j])
    #delete deletions
    for i in links:
        if i not in deletions:
            retlist.append(i)
    links.clear()
    for x in retlist:
        links.append(x)
    return retlist

                
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
            #clean & check
        for x in position.flinks:
            check_position(x)
        clean_list(position, position.flinks)
    return link_count


def Print_list(position_list):	#chekced
    for position in position_list:
        print(str(position))


def Main():
    X=16
    position_list = []
    print(Fill_list(position_list))
    Link_list(position_list)
    print("\t"+str(position_list[X]))
    for x in position_list[X].flinks:
        print(str(x))
                                
Main()
