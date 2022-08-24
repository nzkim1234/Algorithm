while True:
    w, h = map(int,input().split())
    
    if w==0 and h==0:
        break
    
    graph = [ [0 for _ in range(h)]for _ in range(w) ]
    hole=[[0]]
    g = int(input())

    for _ in range(g):
        x,y = map(int,input().split())
        graph[x][y] = -1
    
    e = int(input())
    
    for i in range(1,e+1):
        x,y, hx,hy, t = map(int,input().split())    
        graph[x][y] = i
        hole.append([hx,hy,t])

    dist = [ [1e9 for _ in range(h)] for _ in range(w) ]
    dist[0][0]=0

    
    
    def bf():
        for count in range(h*w):
            for x in range(w):
                for y in range(h):
                    
                    if x==w-1 and y==h-1 or graph[x][y]==-1:
                        continue
                    
                    elif graph[x][y] >=1:
                        outX,outY,outTime = hole[ graph[x][y] ]

                        if dist[outX][outY] > dist[x][y] + outTime :
                            dist[outX][outY] = dist[x][y] + outTime 

                            if count == h*w-1 :
                                return -1e9
                          
                    elif graph[x][y]==0:
                        for nx,ny in ([x,y+1], [x,y-1], [x+1,y], [x-1,y]):



                            if 0<=nx<w and 0<=ny<h : 
                                if graph[nx][ny] >=0 :
                                    if dist[nx][ny] > dist[x][y]+1:
                                        dist[nx][ny] = dist[x][y]+1
                                        
                                        if count == h*w-1:
                                            return -1e9
                                            # if check(nx,ny):
                                            #     return False
                                   
        return dist[w-1][h-1]
    
    result = bf()
    if result == float('-inf') :
        print('Never')
    elif result == 1e9:
        print('Impossible')
    else:
        print(result)                  