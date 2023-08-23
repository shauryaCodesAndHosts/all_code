class Queue:
    def __init__(self) -> None:
        self.queue =[]

    def addq(self,val):
        self.queue.append(val)
    
    def delq(self):
        j= None
        if len(self.queue) != 0  :
            j=self.queue[0]
            self.queue = self.queue[1:]
        return j
    
    def isEmpty(self):
        return (self.queue == [])
    

def longest_path(adjList):
    indeg = {}
    l_path = {}
    for k in adjList.keys():
        indeg[k]=0
        l_path[k]= 0
    
    for k in adjList.keys():
        for l in adjList[k]:
            indeg[l] = indeg[l] + 1

    zeroq = Queue()
    for x in indeg.keys():
        if indeg[x] == 0:
            indeg[x]-=1
            zeroq.addq(x)

    while ( not zeroq.isEmpty()):
        j = zeroq.delq()
        #l_path[j] = l_path[j] + 1
        indeg[j]-=1
        for k in adjList[j]:
            indeg[k]-=1
            l_path[k]=max(l_path[k],l_path[j]+1)
            if indeg[k] == 0 :
                zeroq.addq(k)
    print(l_path)

d={
    0:[2,3,4],
    1:[2,7],
    2:[5],
    3:[5,7],
    4:[7],
    5:[6],
    6:[7],
    7:[]
}


longest_path(d)




