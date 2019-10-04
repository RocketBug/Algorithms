def BFS(start_pos, graph):
    visited = [False] * (len(graph)+1)
    parent = [-1] * (len(graph)+1)
    level = [-1] * (len(graph)+1)
    Q = []
    level[start_pos] = 0
    visited[start_pos] = True
    Q.append(start_pos)

    while (len(Q)):
        head = Q.pop(0)
        edges = graph[head]
        for each in edges:
            if level[each] == -1:
                level[each] = 1 + level[head]
                parent[each] = head
                Q.append(each)

def findBFS(start_pos, graph, find):
    visited = [False] * (len(graph)+1)
    parent = [-1] * (len(graph)+1)
    Q = []
    visited[start_pos] = True
    Q.append(start_pos)
    while(len(Q)):
        head = Q.pop(0)
        edges = graph[head]
        
        if head == find:
            for (i,j) in enumerate(parent):
                print(f"{j}-->{i}")
            return

        for each in edges:
            if visited[each] == False:
                visited[each] = True
                parent[each] = head
                Q.append(each)


        

graphs = {1:{2,3,4},
        2:{1,3},
        3:{1,2},
        4:{1,5,8},
        5:{4,6,7},
        6:{5,7,8,9},
        7:{5,6},
        8:{4,6,9},
        9:{6,8,10},
        10:{9}}

findBFS(1, graphs, 9)
