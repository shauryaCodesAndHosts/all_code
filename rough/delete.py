def min_soldiers_to_distract(N, A):
    soldiers_to_distract = 0  # Number of soldiers to distract
    count = 0  # Number of soldiers looking toward the left

    # Count the number of soldiers looking toward the left
    for i in range(N):
        if A[i] == 0:
            count += 1

    # Iterate through the soldiers and distract the required number of soldiers
    for i in range(N):
        if A[i] == 1:
            soldiers_to_distract += 1
        else:
            break

    # Return the minimum number of soldiers to distract
    return min(soldiers_to_distract, count)

# Read the values for N and A
A=[]
N = int(input())
for i in range(N):
    A.append(int(input()))
#A = list(map(int, input().split()))

# Calculate the minimum number of soldiers to distract
result = min_soldiers_to_distract(N, A)

# Print the result
print(result)
