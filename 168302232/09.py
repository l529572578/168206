graph = {}
graph["yuepu"] = {}
graph["yuepu"]["haibao"] = 0
graph["yuepu"]["changpian"] = 5
graph["haibao"] = {}
graph["haibao"]["jita"] = 30
graph["haibao"]["jiazigu"] = 35
graph["changpian"] = {}
graph["changpian"]["jita"] = 15
graph["changpian"]["jiazigu"] = 20
graph["jita"] = {}
graph["jita"]["gangqin"] = 20
graph["jiazigu"] = {}
graph["jiazigu"]["gangqin"] = 10
graph["gangqin"] = {}

parents = {}
parents["haibao"] = "yuepu"
parents["changpian"] = "yuepu"
parents["jiazigu"] = "changpian"
parents["jita"] = "changpian"
parents["gangqin"] = None

infinity = float("inf")
costs = {}
costs["changpian"] = 5
costs["haibao"] = 0
costs["jita"] = infinity
costs["jiazigu"] = infinity
costs["gangqin"] = infinity

processed = []

def lowest_cost_node(costs):
    lowcost = float("inf")
    lowcostnode = None
    for node in costs:
        cost = costs[node]
        if cost < lowcost and node not in processed:
            lowcost = cost
            lowcostnode = node
    return lowcostnode

node = lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = lowest_cost_node(costs)


def get_process(factor):
    if factor != "yuepu":
        return get_process(parents[factor]) + " --> " + factor
    else:
        return factor

print(" 过程: ",get_process("gangqin"),'\n',"换钢琴最少花费：",costs[n])
