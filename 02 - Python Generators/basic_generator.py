# function solution
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


# Replace this function using a generator:
# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# And even more simplistic, we can replace the entire generator function with a generator expression:
n = 1000000
even_integers = (n for n in range(n) if n % 2 == 0)
