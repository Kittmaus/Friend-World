# this is how i ignore my shortcomings
# :)

from varmake import filled, Friend, apartments, clear


def makelist(lis):
    return([a for b in lis for a in b])

def showapts():
    blist = makelist(reversed(apartments))
    for i in range(len(blist)):
        if blist[i] == None:
            blist[i] = " "
        if type(blist[i]) == Friend:
            blist[i] = blist[i].symbol
    clear()
    print("""
FriendWorld V0.01              
Made by Kittmaus
                                             ( )
                                             ()
                                             O
                                          __o_
               /---\\                      |  |
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
        apartments[address[0]][address[1]]
        movefriend(Friend(name, address), address)
    except:
        showapts()
        print("That address doesn't exist. Floor bounds are 1-4, and room bounds are 1-8.\n")
        createfriend()

def movefriend(newFriend, home):
    if checkspace(home) == 1: #(empty)
        apartments[home[0]][home[1]] = newFriend
        newFriend.address = f"{int(home[0])+1}0{int(home[1])+1}"

    elif checkspace(home) == 2: #(has resident)
        oldFriend = apartments[home[0]][home[1]]
        try:
            d = input(f"Where do you want to move [{oldFriend.name}]? Say \"trash\" if you want to delete them.\n").lower()
            if d == "trash":
                deletefriend(oldFriend)
                apartments[home[0]][home[1]] = newFriend
                newFriend.address = f"{int(home[0])+1}0{int(home[1])+1}"
                return()
            else:
                address = listify(d)
                apartments[address[0]][address[1]]
        except:
            showapts()
            print("That address doesn't exist. Floor bounds are 1-4, and room bounds are 1-8.\n")
            movefriend(newFriend, home)
        apartments[home[0]][home[1]] = newFriend
        newFriend.address = f"{int(home[0])+1}0{int(home[1])+1}"
        movefriend(oldFriend, address)

def deletefriend(friend):
    dec = input(f"Are you sure you want to delete [{friend.name}]? y/n.\n").lower()
    if dec == "y":
        apartments[friend.getaddress()[0]][friend.getaddress()[1]] = None
    elif dec == "n":
        print(f"Okay. [{friend}] will not be deleted.")
        return()
    else:
        deletefriend(friend)

def gethome(address):
    return(apartments[address[0]][address[1]])

def tutorial(verify):
    if not verify:
        print("\nWelcome to Friendworld!\n\n\nIt appears you don't have any friends yet. Let's get you started!\nFirst, your new friend needs a name and an apartment number.\n")
        createfriend()
        verify = True