# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

integers = even_integers_generator(10)

for n in even_integers_generator(10):
    print(n)