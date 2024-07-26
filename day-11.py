arr = []   
for _ in range(6):
    arr.append(list(map(int, input().split())))

max_sum = -63  # Minimum possible sum
for i in range(4):
    for j in range(4):
        hourglass_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
                        + arr[i+1][j+1]
                        + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        if hourglass_sum > max_sum:
            max_sum = hourglass_sum

print(max_sum)