def minimum_distracted_soldiers(A):
    distracted_soldiers = 0  
    seen_soldiers = 0  

    for soldier in A:
        if soldier == 1:
            seen_soldiers += 1
            distracted_soldiers = 0  
        else:
            distracted_soldiers += 1

    return distracted_soldiers


N = int(input("Enter the number of soldiers: "))
A = []
for i in range(N):
    soldier = int(input(f"Enter the direction of soldier {i+1} (0 for left, 1 for right): "))
    A.append(soldier)

result = minimum_distracted_soldiers(A)
print("Minimum number of soldiers to be distracted:", result)

