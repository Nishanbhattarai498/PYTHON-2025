#reduce()=apply a function to an iterable  and reduce it to a single cumulative value.
#performs function on first two element and repeat process until  i value remains
#reduce(function,iterable)


import functools
letters=["H","E","L","L","O"]



word=functools.reduce(lambda x,y:x+y,letters)
print(word)


factorial=[5,4,3,2,1] 

fac=functools.reduce(lambda x,y:x*y,factorial)
print(fac)