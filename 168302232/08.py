def topsort(G):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in  G[u]:
            in_degrees[v] += 1
                                    
    Q = [u for u in G if in_degrees[u] == 0]
                                    
    S = []
    while Q:
        u = Q.pop()
                                   
        S.append(u)
        for v in G[u]:
            count[v] -= 1
                                   
            if count[v] == 0:
                Q.append(v)
    return S
G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'e',
    'e':'f',
    'f':''
}
print(topsort(G))
