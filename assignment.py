# The number of possible bit strings without consecutive 0s can be visualized as (n+2)th fibonacci number where
# n is length of bit string
# So (n+2)th fibonacci number is the solution for the given problem
# To find fibonacci number, Matrix power method is used so that it can be obtained in O(log N) time
# In Matrix method where template matrix is used (T = [[1, 1], [1, 0]] ) and
# after power(T,n)
# T[0][0] gives (n+1)th fibonacci number


# Matrix multiplication function
def mul(temp1, temp2):
    prime = 1000000007
    x = temp1[0][0] * temp2[0][0] + temp1[0][1] * temp2[1][0]
    y = temp1[0][0] * temp2[0][1] + temp1[0][1] * temp2[1][1]
    z = temp1[1][0] * temp2[0][0] + temp1[1][1] * temp2[1][0]
    w = temp1[1][0] * temp2[0][1] + temp1[1][1] * temp2[1][1]
    temp1[0][0] = x % prime
    temp1[0][1] = y % prime
    temp1[1][0] = z % prime
    temp1[1][1] = w % prime


# Iterative power function on Matrix
def power(temp1, n):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            mul(res, temp1)
        n = n // 2
        mul(temp1, temp1)
    return res


# Fibonacci number function by Matrix multiplication method
def fib(n):
    template = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    template = power(template, n - 1)
    return template[0][0]


tCases = int(input())
data = [int(input()) for i in range(tCases)]
res = []
for n in data:
    res.append(fib(n + 2))
for i in res:
    print(i)
