def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n   # Default result with all 0s
    stack = []         # Will store indices of temperatures in decreasing order

    for i, temp in enumerate(temperatures):
        # Check if the current temperature is warmer than the one at stack's top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index   # Distance between days
        stack.append(i)  # Push current day's index

    return answer
        
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))