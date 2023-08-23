import numpy as np
def floyd_warshal(mat):
    rows = len(mat)
    cols = len(mat[0])
    infinity = float('inf')
    sp=np.zeros(shape=(rows,cols,cols+1))
    for x in range(rows):
        for y in range(cols):
            sp[x][y][0] = infinity

    for x in range(0,rows):
        for y in range(0,cols):
            if mat[x][y][0]==1:
                sp[x][y][0] = mat[x][y][1]

    for k in range(1,cols+1):
        for i in range(rows):
            for j in range(cols):
                sp[i][j][k] = min(sp[i][j][k-1], sp[i][k-1][k-1] + sp[k-1][j][k-1] )
    
    return sp[:,:,cols]

g = [
[(0,0)  ,   (1,10 ) , (1,80 ), (0, 0  )  , (0,0  )   ,(0, 0),(0, 0  ) ],
[(1,10) ,   (0,0 )  , (1,6  ), (0, 0  )  , (1,20  )  ,(0, 0),(0, 0 ) ], 
[(1,80) ,   (1,6)   , (0,0  ), (1, 70 )  , (0,0  )   ,(0, 0),(0, 0  )], 
[(0,0)  ,   (0,0 )  , (1,70 ), (0, 0  )  , (0,0 )    ,(0, 0),(0, 0  )], 
[(0,0)  ,   (1,20 ) , (0,0  ), (0, 0  )  , (0,0  )   ,(1,50),(1, 5  )], 
[(0,0)  ,   (0,0 )  , (0,0  ), (0, 0  )  , (1,50 )   ,(0, 0),(1, 10  )],
[(0,0)  ,   (0,0)   , (0,0  ), (0, 0  )  , (1,5  )   ,(1,10),(0, 0  )]
]


print(floyd_warshal(g))