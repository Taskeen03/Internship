def gas_station(gas, cost):
    remaining = 0
    prev_remaining = 0
    candidate = 0
    
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:

            candidate = i + 1
            prev_remaining += remaining
            remaining = 0

    if remaining + prev_remaining < 0 or candidate >= len(gas):
        return -1
    
    return candidate 

gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print("Starting gas station index:", gas_station(gas, cost))
