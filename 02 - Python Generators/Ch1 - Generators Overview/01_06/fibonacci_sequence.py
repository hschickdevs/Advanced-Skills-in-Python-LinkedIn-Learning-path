# Fibonacci Sequence Generator Challenge

def fibonacci_gen():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead


fib = fibonacci_gen()

for _ in range(10):
    print(fib.__next__())
