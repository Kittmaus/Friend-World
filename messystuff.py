# this is how i ignore my shortcomings
# :)

from varmake import *

    
def showapts():
    blist = [room for roomlist in reversed(apartments) for room in roomlist]
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

def listify(num):
    return([int(num[:-2])-1,int(num[-1])-1])

def checkspace(address):
    try:
        if apartments[address[0]][address[1]] == None:
            return(1)
        else:
            return(2)
    except:
        return(3)

def createfriend():
    name = input("What do you want your friend's name to be?\n")
    try:
        address = listify(input("Where do you want your friend to live?\n"))
    except:
        return("Error: Address is invalid.")
    if checkspace(address) == 1:
        apartments[address[0]][address[1]] = Friend(name,address)
    elif checkspace(address) == 2:
        movefriend(Friend(name,address),apartments[address[0]][address[1]])

def movefriend(usurper,victim):
    try:
        address = listify(input(f"Where do you want {victim.name} to move to?\n"))
    except:
        print("Error: Address is invalid.")
        return()
    apartments[victim.getaddress()[0]][victim.getaddress()[1]] = usurper
    print(usurper.name,victim.name)
    if checkspace(address) == 1:
        pass
    elif checkspace(address) == 2:
        pass
        