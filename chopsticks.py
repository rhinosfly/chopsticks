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

    def correct(self):
        self.gl %= FINGER_NUMBER
        self.gr %= FINGER_NUMBER
        self.rl %= FINGER_NUMBER
        self.rr %= FINGER_NUMBER
        if self.gr > self.gl:
            tmp = self.gr
            self.gr = self.gl
            self.gl = tmp
        if self.rr > self.rl:
            tmp = self.rr
            self.rr = self.rl
            self.rl = tmp

    def flip(self):
        tmpl = self.gl
        tmpr = self.gr
        self.gl = self.rl
        self.gr = self.rr
        self.rl = tmpl
        self.rr = tmpr
        return self


def roundup(x):
    xint = int(x)
    if xint < x:
        return xint + 1
    else:
        return xint


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
