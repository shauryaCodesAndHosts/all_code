fact = 1
poww = 1 
def taylor(x,n):
    if n == 0:
        global fact
        global poww
        fact = 1
        poww = 1
        return 1
    else:
        res = taylor(x,n-1)
        fact = fact * n
        poww = poww * x
        return res + (poww/fact)
    
def taylor_series_exponential(x, n):
    if n == 0:
        return 1  # Base case: e^0 = 1
    else:
        # Recursive case: Calculate the (n-1)th term and add it to the sum
        term = x ** n / factorial(n)
        return term + taylor_series_exponential(x, n - 1)

def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k - 1)


print(taylor(2,5),taylor_series_exponential(2,5))