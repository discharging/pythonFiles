def dfs(graph, node):
    stack = [node]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                stack.append(neighbor)
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

print(dfs(graph1,'A'))
