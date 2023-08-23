def dijkstra(mat, s):
    visited={}
    distance={}
    infinity = float('inf')
    rows = len(mat)
    cols = len(mat[0])
    for row in range(rows):
        visited[row] = False
        distance[row] = infinity
    
    distance[s]= 0 
        
    for row in range(rows):
        #nextd_list = []
        #for v in range(rows):
        #    if not visited[v]:
        #        nextd_list.append(v)
        nextd = min([distance[v] for v in range(rows) if not visited[v]])
        print(nextd)
        nextVlist = []
        for v in range(0,rows):
            if distance[v] == nextd and not visited[v]:
                nextVlist.append(v)
        print(nextVlist)
        if nextVlist == [] :
            break
        nextv = min(nextVlist)
        visited[nextv] = True
        
        for c in range(cols):
            if mat[nextv][c][0] == 1 and not visited[c]:
                distance[c] = min(distance[c], distance[nextv] + mat[nextv][c][1]  )
    return distance



g = [
[(0,0)  ,   (1,10 ) , (1,80 ), (0, 0  )  , (0,0  )   ,(0, 0),(0, 0  ) ],
[(1,10) ,   (0,0 )  , (1,6  ), (0, 0  )  , (1,20  )  ,(0, 0),(0, 0 ) ], 
[(1,80) ,   (1,6)   , (0,0  ), (1, 70 )  , (0,0  )   ,(0, 0),(0, 0  )], 
[(0,0)  ,   (0,0 )  , (1,70 ), (0, 0  )  , (0,0 )    ,(0, 0),(0, 0  )], 
[(0,0)  ,   (1,20 ) , (0,0  ), (0, 0  )  , (0,0  )   ,(1,50),(1, 5  )], 
[(0,0)  ,   (0,0 )  , (0,0  ), (0, 0  )  , (1,50 )   ,(0, 0),(1, 10  )],
[(0,0)  ,   (0,0)   , (0,0  ), (0, 0  )  , (1,5  )   ,(1,10),(0, 0  )]
]

print(dijkstra(g,0))
