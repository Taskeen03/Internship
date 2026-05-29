def largest_rectangle(heights):
    heights = [-1] + heights + [-1]
    max_area = 0
    
    stack = [0] 
    
    for i in range(1, len(heights)):

        while heights[stack[-1]] > heights[i]:
            top_height = heights[stack.pop()]

            width = i - stack[-1] - 1
            
            max_area = max(max_area, top_height * width)
            
        stack.append(i)
        
    return max_area

histogram = [2, 1, 5, 6, 2, 3]
print("Largest Rectangle Area:", largest_rectangle(histogram))