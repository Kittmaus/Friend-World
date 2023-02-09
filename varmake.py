class Friend:
    def __init__(self, n, a):
        self.name = n
        self.symbol = n[0]
        self.address = f"{str(a[0])}0{str(a[1])}"

    def getaddress(self):
        return([int(self.address[:-2])-1,int(self.address[-1])-1])

apartments = [
    [Friend("Test Friend",[1,1]),None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None]
]