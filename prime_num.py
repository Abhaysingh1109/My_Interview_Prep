
def primeNumber(n):
    
    if n <= 1:
        return "This is not Prime Number"
    
    for i in range(2,n):
        if n%i == 0:
            return "This is not Prime Number"
        
    return "Prime Number"

print(primeNumber(4))
        