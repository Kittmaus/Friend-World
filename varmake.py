class Friend:
    def __init__(self, n, a):
        self.name = n
        self.symbol = n[0]
        self.address = f"{int(a[0])+1}0{int(a[1])+1}"

    def getaddress(self):
        return([int(self.address[:-2])-1,int(self.address[-1])-1])

    def getinfo(self):
        return(f"Name: {self.name}\nAddress (Number Form): {self.address}\nAddress (List Form): {self.getaddress()}\n")

apartments = [
    [Friend("Debug",[0,0]),None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None]
]