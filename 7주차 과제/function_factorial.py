#function_factorial.py

def factorial(n):
    if n == 1:
        return 1;

    print('n =', n);
    return n*factorial(n-1);

factorial(5);
