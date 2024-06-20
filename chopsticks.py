#chopsticks engine: split into multiple modules; 

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
        return "[[{}, {}, {}, {}]]".format(self.gl, self.gr, self.rl, self.rr)
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



def roundup(x):
    xint = int(x)
    if xint < x:
        return xint + 1
    else:
        return xint




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



def Print_list(position_list):	#chekced
    for i in range(len(position_list)):
        print(str(i) + ': ' + str(position_list[i]))
        for link in position_list[i].flinks:
            print("\t"+str(link))
