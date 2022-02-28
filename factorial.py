def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def prost2(n, m):
    if n % m == 0:
        return 'no'
    else:
        prost2(n, m-1)
    return 'yes'
def prost(n):
    prost2(n,n-1)
print('hello')