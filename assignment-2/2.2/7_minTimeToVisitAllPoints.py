def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(len(points) - 1):
        x_diff = abs(points[i+1][0] - points[i][0])
        y_diff = abs(points[i+1][1] - points[i][1])
        time += max(x_diff, y_diff)
    return time

points_input = [[1, 1], [3, 4], [-1, 0]]
result = minTimeToVisitAllPoints(points_input)
print(result)  