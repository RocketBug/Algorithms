paths = [
    [1,2,5],
    [5,2,6],
    [1,3,8],
    [1,1,6],
    [10,1,6],
    [8,1,11],
    [11,3,6],
    [10,4,8],
    [10,1,11],
    [2, 1, 3]
    ]

graph = {}
weight = {}

for i in paths:
    if i[0] not in graph:
        graph[i[0]] = []

    graph[i[0]].append(i[2])

    if i[2] not in graph:
        graph[i[2]] = []

    graph[i[2]].append(i[0])

for j in paths:
    weight[(j[0], j[2])] = j[1]
    weight[(j[2], j[0])] = j[1]



def min_dist(visited, est):

    min_vertex_cost = 99999
    min_vertex = -1

    for k in est:
        if visited[k] == False and est[k]< min_vertex_cost:
                min_vertex_cost = est[k]
                min_vertex = k

    
    return min_vertex

def printsol(est):
    print(est)


def shorted_path(start):
    visited = {}
    est = {}

    for k in graph:
        visited[k] = False
        est[k] = 99999

    est[start] = 0
    visited[start] = True

    for j in graph[start]:
        est[j] = weight[(start, j)]

    for i in range(len(graph)):
        
        min_vertex = min_dist(visited, est)

        visited[min_vertex] = True

        if min_vertex == -1:
            continue

        min_edge_weight = est[min_vertex]

        for k in graph[min_vertex]:
            if min_edge_weight + weight[(min_vertex, k)] < est[k]:
                est[k] = min_edge_weight + weight[(min_vertex, k)]

        print(est)
        print(visited)



shorted_path(1)