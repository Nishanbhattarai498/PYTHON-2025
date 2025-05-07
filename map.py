#map() = applies a function  to each item  in an iterable(list,tuples.....etc)

#map(function,iterable)



store=[("shirt",400.00),
       ("pant",200.00),
       ("katttu",46.00),
       ("peti",50.00)]


to_euros=lambda data:(data[0],data[1]*135)


store_euros=list(map(to_euros,store))

for i in store_euros:
    print(i)

