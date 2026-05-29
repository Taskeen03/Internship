def timeRequiredToBuy(tickets, k):
    seconds = 0
    for i in range(len(tickets)):
        if i <= k:
            seconds += min(tickets[i], tickets[k])
        else:
            seconds += min(tickets[i], tickets[k] - 1)
    return seconds

tickets_input = [2, 3, 2]
k_input = 2
result = timeRequiredToBuy(tickets_input, k_input)
print(result)  