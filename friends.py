class Friend:
    def __init__(self, n, a):
        self.name = n
        self.address = a
        self.symbol = n[0]

apartments = [
    [Friend("Test Friend",101),None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None]
]

def showapts(alist):
    blist = [room for roomlist in reversed(alist) for room in roomlist]
    for i in range(len(blist)):
        if blist[i] == None:
            blist[i] = " "
        if type(blist[i]) == Friend:
            blist[i] = blist[i].symbol
    print("""
        |===============================================|
        |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
        |===============================================|
        |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
        |===============================================|
        |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
        |===============================================|
        |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
        |===============================================|
    """.format(*blist))

def addressify(loc):
    try:
        loc = str(loc)
        l = [int(loc[:-2])-1,int(loc[-1])-1]
        apartments[l[0]][l[1]]
    except:
        l = ("ERR")
    return(l)

def createfriend():
    name = input("What are you naming this friend?\n")
    areq = input("What room did you want to put them in?\n")
    afind = addressify(areq)
    try:
        add = apartments[afind[0]][afind[1]]
    except:
        return("Error: Room does not exist.")
    if add == "ERR":
        return("Error: Room does not exist.")
    if add != None:
        c = input(f"Room already in use by [{add.name}]. Would you like to replace them? y/n.\n").lower()
        if c == "y":
            print(f"Sure. Replaced [{add.name}].") 
        elif c == "n":
            return("Error: Room already in use.")
        else:
            return("Error: Choice was not valid.")
    apartments[afind[0]][afind[1]] = Friend(name, areq)
    return(f"Friend [{name}] added successfully to room {areq}.")

while True:
    print(createfriend())
    showapts(apartments)