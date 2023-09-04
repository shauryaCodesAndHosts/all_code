def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while n:
        sequence.append(a)
        a, b = b, a + b
        n=n-1
    return sequence

def main():
    n = 100
    result = fibonacci_sequence(n)
    print(f"The first {n} numbers in the Fibonacci sequence are:")
    for num in result:
        print(num, end=" ")

if __name__ == "__main__":
    main()