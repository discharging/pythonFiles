def bfs(graph,node,path=[],index=0):
    path += [node]
    try:
        while 1:
            for neighbour in graph[path[index]]:
                if neighbour not in path:
                    path += [neighbour]
                index +=1
    except IndexError:
        return path

graph1={
        'A':['B','C'],
        'B':['A','D','E'],
        'C':['A','E','F'],
        'D':['B','G','H'],
        'E':['B','C','I'],
        'F':['C'],
        'G':['D'],
        'H':['D'],
        'I':['E']
        }

print(bfs(graph1,'A'))

