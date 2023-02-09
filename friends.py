from messystuff import createfriend, showapts, apartments, gethome,listify

while True:
    createfriend()
    showapts()
    for i in apartments:
        for j in i:
            try:
                print(j.getinfo())
            except:
                continue