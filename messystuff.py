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
    movefriend(Friend(name, address), address)

def movefriend(newFriend, home):
    if checkspace(home) == 1: #(empty)
        apartments[home[0]][home[1]] = newFriend
        newFriend.address = f"{int(home[0])+1}0{int(home[1])+1}"

    elif checkspace(home) == 2: #(has resident)
        oldFriend = apartments[home[0]][home[1]]
        try:
            address = listify(input(f"Where do you want to move [{oldFriend.name}]?\n"))
        except:
            return("Error: Address is invalid.")
        apartments[home[0]][home[1]] = newFriend
        newFriend.address = f"{int(home[0])+1}0{int(home[1])+1}"
        movefriend(oldFriend, address)

def gethome(address):
    return(apartments[address[0]][address[1]])
