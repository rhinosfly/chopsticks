#chopsticks engine: split into multiple modules; 

FINGER_NUMBER = 5   #you never know

class Position:
    def __init__(self, gl, gr, rl, rr):
        self.gl = gl    #giver left
        self.gr = gr    #giver right
        self.rl = rl    #reciever left
        self.rr = rr    #reciever right
        self.flinks = []    #forward links
        self.blinks = []    #backward links
        self.index = -1     #index (-1 for uninitialized)
        
    def __str__(self):
        return "[[{}, {}, {}, {}]]".format(self.gl, self.gr, self.rl, self.rr)
    
    def Copy(self):	#CHECKED
        retval = Position(self.gl, self.gr, self.rl, self.rr)
        retval.flinks = self.flinks.copy()
        retval.blinks = self.blinks.copy()
        return retval
    
    def Equals(self, other):	#CHEKED #true if all finger values are the same; false otherwise
        if self.gl == other.gl and self.gr == other.gr and self.rl == other.rl and self.rr == other.rr:
            return True
        else:
            return False

    def Correct(self):  # correct position to be legal
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

    def Flip(self):     #flip giver and reciever (for turn switch)
        tmpl = self.gl
        tmpr = self.gr
        self.gl = self.rl
        self.gr = self.rr
        self.rl = tmpl
        self.rr = tmpr
        return self


def Roundup(x):
    xint = int(x)
    if xint < x:
        return xint + 1
    else:
        return xint


def Clean_list(position, links):    #remove self and duplicate links
    global len
    deletions = []	#links to delete
    retlist = []	#final list
    #get deletions
    for i in links: #remove links to self
        if i.Equals(position):
            deletions.append(i)
    length = len(links)	#remove duplicates
    for i in range(length-1):
        for j in range(i+1,length):
            if links[i].Equals(links[j]):
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
        print(str(position_list[i].index) + ': ' + str(position_list[i]))
        for link in position_list[i].flinks:
            print("\t"+str(link))
