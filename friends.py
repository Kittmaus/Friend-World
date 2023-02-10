from messystuff import createfriend, apartments, showapts, makelist, filled, tutorial, clear

clear()

for i in makelist(apartments):
    if i != None:
        filled = True
        break
tutorial(filled)

while True:
    showapts()
    createfriend()