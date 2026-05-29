def findCheapestPrice(n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0

    for _ in range(k + 1):
        tmp_prices = list(prices)
        for u, v, w in flights:
            if prices[u] == float('inf'): continue
            if prices[u] + w < tmp_prices[v]:
                tmp_prices[v] = prices[u] + w
        prices = tmp_prices    
    return prices[dst] if prices[dst] != float('inf') else -1

n_nodes = 4
flights_input = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src_node, dst_node, stops = 0, 3, 1

result = findCheapestPrice(n_nodes, flights_input, src_node, dst_node, stops)
print(result) 