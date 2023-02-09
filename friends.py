class Friend:
    def __init__(self, n, a):
        self.name = n
        self.address = a

apartments = [
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None]
]

def sela(loc):
    loc = str(loc)
    try:
        return(apartments[int(loc[:-2])-1][int(loc[-1])-1])
    except:
        return("this room does not exist IDIOT")
