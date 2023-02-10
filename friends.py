from messystuff import createfriend, apartments, showapts, makelist, filled
import os
clear = lambda: os.system('cls')

clear()
showapts()

for i in makelist(apartments):
    if i != None:
        filled = True
        break

if filled == False:
    print("It appears you don't have any friends. LOSER! HAHAHHAAHA\n")
    createfriend()

while True:
    clear()
    showapts()
    createfriend()