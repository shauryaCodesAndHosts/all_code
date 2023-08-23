
g = [
[(0,0)  ,   (1,10 ) , (1,80 ), (0, 0  )  , (0,0  )   ,(0, 0),(0, 0  ) ],
[(1,10) ,   (0,0 )  , (1,6  ), (0, 0  )  , (1,20  )  ,(0, 0),(0, 0 ) ], 
[(1,80) ,   (1,6)   , (0,0  ), (1, 70 )  , (0,0  )   ,(0, 0),(0, 0  )], 
[(0,0)  ,   (0,0 )  , (1,70 ), (0, 0  )  , (0,0 )    ,(0, 0),(0, 0  )], 
[(0,0)  ,   (1,20 ) , (0,0  ), (0, 0  )  , (0,0  )   ,(1,50),(1, 5  )], 
[(0,0)  ,   (0,0 )  , (0,0  ), (0, 0  )  , (1,50 )   ,(0, 0),(1, 10  )],
[(0,0)  ,   (0,0)   , (0,0  ), (0, 0  )  , (1,5  )   ,(1,10),(0, 0  )]
]


def bellmanford(mat, s):
    rows = len(mat)
    cols = len(mat[0])
    infinity = float('inf')
    distance = {}
    for v in range(rows):
        distance[v] = infinity

    distance[s] = 0

    for i in range(0,rows):
        for row in range(rows):
            for col in range(cols):
                if mat[row][col][0] == 1:
                    distance[col] = min(distance[col], distance[row]+mat[row][col][1])
    return distance

print(bellmanford(g,0))
