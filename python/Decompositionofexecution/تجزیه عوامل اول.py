import itertools
def prime_factor(n:int):
    for i in itertools.chain([2],itertools.count(3,2)):
        if n<=1:
            break
        while n % i == 0:
            n//=i
            yield i
a = []
for i in prime_factor(98):
    a.append(i)

if len(a) == 3 or len(a) == 2:
    result = " ^ ".join([str(a[i]) for i in range(len(a)-1)])
    print(result,"*",a[-1])

elif len(a) == 4:
    result = " ^ ".join([str(a[i]) for i in range(len(a)-2)])
    print( result ," * ", a[-2],"^",a[-1])
