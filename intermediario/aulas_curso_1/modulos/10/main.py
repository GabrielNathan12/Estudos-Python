from itertools import count


c1 = count(8)
r1= range(2,10, 2)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('C1')

for i in c1:
    if i > 10:
        break

    print(i)

print('R1')

for i in r1:
    print(i)