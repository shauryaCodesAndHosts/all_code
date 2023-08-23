import pprint
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
    
    def display(self):
        print(self.queue)
    

def longJourney(Alist):
    indeg = {}
    l_path = {}
    parent = {}
    for k in Alist.keys():
        indeg[k]=0
        l_path[k]= 0 
        parent[k] = None
    
    for  k in Alist.keys():
        for l in Alist[k]:
            indeg[l]+=1
    
    #print(indeg)

    zq = Queue()
    for k in Alist.keys():
        if indeg[k] == 0 :
            indeg[k]-=1
            zq.addq(k)
            parent[k]= None
    zq.display()

    while(not zq.isEmpty()):
        j = zq.delq()
        indeg[j]-=1
        for k in Alist[j]:
            parent[k] = j
            indeg[k] -= 1
            l_path[k] = max(l_path[k],l_path[j]+1)
            if indeg[k] == 0:
                zq.addq(k)
            #pprint.pprint(parent)
    ls=[]
    while not k == None:
        ls.append(k)
        k=parent[k]
    

    pprint.pprint(l_path)
    zq.display()
    print(ls)
    ls.reverse()
    print(ls)





d= {'Madurai': ['Cochin', 'Kanyakumari'],
 'Vaishali': [],
 'Varanasi': ['Khajuraho', 'Bodhgaya'],
 'Thiruvanandhapuram': ['Kanyakumari'],
 'Udaipur': ['Gir', 'Ajanta'],
 'Rishikesh': ['Delhi'],
 'Shimla': ['Rishikesh'],
 'Bangalore': ['Chennai', 'Madurai'],
 'Agra': ['Ranthambore'],
 'Ellora': ['Aurangabad'],
 'Bodhgaya': ['Kolkatta'],
 'Cochin': ['Thiruvanandhapuram'],
 'Pushkar': ['Udaipur', 'Ranthambore'],
 'Ranthambore': ['Khajuraho'],
 'Gir': [],
 'Aurangabad': ['Mumbai'],
 'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
 'Chennai': ['Madurai'],
 'Sravasti': ['Kushinagar'],
 'Leh': ['Shimla'],
 'Sarnath': ['Varanasi'],
 'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
 'Goa': ['Cochin', 'Bangalore'],
 'Kanyakumari': [],
 'Kushinagar': ['Sarnath', 'Vaishali'],
 'Khajuraho': ['Ajanta'],
 'Jaipur': ['Pushkar'],
 'Mumbai': ['Goa'],
 'Ajanta': ['Ellora', 'Aurangabad']}

longJourney(d)