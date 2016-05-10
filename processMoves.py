from HTMLParser import HTMLParser
class Move:
    def __init__(self, name, type):#, power, acc, pp, effect):
        self.name = name
        self.type = type
        #self.power = power
        #self.acc = acc
        #self.pp = pp
        #self.effect = effect
        
        print "Making move ", self.name, "!"
    
class MyHTMLParser(HTMLParser):
    inTableBody = False
    currentTag = ""
    moveName = ""
    foundName = False
    moveType = ""
    foundType = False
    moveCat = ""
    foundCat = False
    movePower = 0
    foundPower = False
    moveAcc = 0
    foundAcc = False
    movePP = 0
    foundPP = False
    moveEff = ""
    foundEff = False
    
    
    #def initTrackers(self):
    #    self.inTableBody = False
    #    self.currentTag = ""
    #    self.moveName = ""
    #    self.moveType = ""

    def initMoveTrack(self):
        self.foundName = False
        self.foundType = False
        self.foundCat = False
        self.foundPower = False
        self.foundAcc = False
        self.foundPP = False
        self.foundEff = False
        print "RESET"
                
    def handle_starttag(self, tag, attrs):
        #print "Tag: ", tag
        self.currentTag = tag
        if tag == "tbody":
            print "START TABLE"
            self.inTableBody = True
        if tag == "a" and self.inTableBody:
            if len(attrs) == 3:
                self.foundName = True
                #self.moveName = attrs[1][1][6:]
                #print len(attrs)
                #print "Name: ", self.moveName
                
            if len(attrs) == 2:
                self.foundType = True
                #self.moveType = attrs[1][1][6:]
                #print "Type: ", self.moveType
                
        if tag == "i" and self.inTableBody:
            print "FOUND I"
            self.foundCat = True                                
                
        if tag == "td":
            print "found TD"
            if not self.foundPower and not self.foundAcc and not self.foundPP and not self.foundEff:
                self.foundPower = True
            elif self.foundPower and not self.foundAcc and not self.foundPP and not self.foundEff:
                self.foundAcc = True
            elif self.foundPower and self.foundAcc and not self.foundPP and not self.foundEff:
                self.foundPP = True
            elif self.foundPower and self.foundAcc and self.foundPP and not self.foundEff:
                self.foundEff = True
           #for attr in attrs:
           #    print attr[0], ":", attr[1]
    def handle_data(self, data):
        #print data
        if self.inTableBody:
            if self.currentTag == "a":
                if self.foundName and not self.foundType:
                    self.moveName = data
                    print "    ", self.moveName
                    
                if self.foundType and self.foundName:
                    self.moveType = data
                    print "    ", self.moveType
                    
            if self.currentTag == "i" and self.foundCat:
                self.moveCat = data
                print "    ", self.moveCat
                
            if self.currentTag == "td":
                if self.foundPower and not self.foundAcc and not self.foundPP and not self.foundEff:
                    self.movePower = data
                    print "    ", self.movePower
                elif self.foundPower and self.foundAcc and not self.foundPP and not self.foundEff:
                    self.moveAcc = data
                    print "    ", self.moveAcc
                elif self.foundPower and self.foundAcc and self.foundPP and not self.foundEff:
                    self.movePP = data
                    print "    ", self.movePP
                elif self.foundPower and self.foundAcc and self.foundPP and self.foundEff:
                    self.moveEff = data
                    print "    ", self.moveEff   
                    self.initMoveTrack()
        
    def handle_endtag(self, tag):
        if tag == "tbody":
            inTableBody = False
            print "END TABLE"
        if tag == "td":
            print "close td"
        #print "     Ending ", tag

#X = Move("acid", "poison")
#print X.name, X.type

#test = """<tr><td class="cell-icon-string"><a class="ent-name" href="/move/absorb" title="View details for Absorb">Absorb</a></td><td class="cell-icon"><a class="type-icon type-grass"  href="/type/grass" >Grass</a></td><td class="cell-icon"><i class="icon-move-cat special" title="Special">Special</i></td> <td class="num">20</td> <td class="num" >100</td> <td class="num">25</td> <td class="long-text">User recovers half the HP inflicted on opponent.</td></tr>"""
parser=MyHTMLParser()
##parser.initTrackers()
parser.initMoveTrack()
#parser.feed(test)

HTML = open("moves.txt")
movesText = HTML.read().decode('utf-8', 'ignore')
parser.feed(movesText)