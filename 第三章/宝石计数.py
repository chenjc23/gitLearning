

 

class Hashtable:
    def __init__(self, size = 10):
        self.size = size
        self.data = [None] * self.size
        self.record = []
    def modfunc(self,data):
        return data % self.size
    def append(self, data):
        pos = self.modfunc(data)
        while self.data[pos] != None:
            pos = (pos + 1) % self.size
        self.data[pos] = data
    def search(self, rock):
        count = 0
        for i in rock:
            if i in self.data:
                count += 1
        print(count)
       
       

gem = list(map(ord, input()))
rock = list(map(ord, input()))
mytable = Hashtable()
for i in gem:
    mytable.append(i)
mytable.search(rock)

            
                
        

        
    