from HTMLParser import HTMLParser
class Move:
    def __init__(self, name, type, power, acc, pp, effect):
        self.name = name
        self.type = type
        self.power = power
        self.acc = acc
        self.pp = pp
        self.effect = effect
    
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Tag: ", tag
        if tag == "tr":
            print data
    #def handle_data(self, data):
        #print "     Data: ", data
        
    #def handle_endtag(self, tag):
        #print "     Ending ", tag

#X = Move("acid", "poison")
#print X.name, X.type

test = """<tr><td class="cell-icon-string"><a class="ent-name" href="/move/absorb" title="View details for Absorb">Absorb</a></td><td class="cell-icon"><a class="type-icon type-grass"  href="/type/grass" >Grass</a></td><td class="cell-icon"><i class="icon-move-cat special" title="Special">Special</i></td> <td class="num">20</td> <td class="num" >100</td> <td class="num">25</td> <td class="long-text">User recovers half the HP inflicted on opponent.</td></tr>"""
parser=MyHTMLParser()
parser.feed(test)