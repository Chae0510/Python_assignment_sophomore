#function_recursion.py

def hello(count):
    if count ==  0:
        return

    print('Hello, pyhon!', count);
    count -= 1;
    hello(count);

hello(5);
