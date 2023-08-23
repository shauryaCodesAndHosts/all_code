class Queue:
    def __init__(self) -> None:
        self.queue =[]
    
    def addq(self,v):
        self.queue.append(v)

    def isEmpty(self):
        return (self.queue == [] )

    def delq(self):
        v=None
        if not self.isEmpty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v

def findConnectionLevel(n, Gmat, Px, Py):
    level = {}
    parent = {}
    for i in range(n):
        level[i] = 0
        parent[i] = -1

    level[px]=0
    q.addq(px)
    while(not q.isempty()):
      j= q.delq()
      for k in range(n):
        if (level[k]==0 and Gmat[j][k]==1):
          level[k]=level[j]+1
          parent[k]=j
          q.addq(k)
    return (level[py])