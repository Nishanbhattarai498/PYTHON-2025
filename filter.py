#filter()= creates a collection of elements from an iterable for which a function returns true 


#filter(function,iterable)


friends=[("nishan",25),
         ("niraj",16),
         ("nirjala",17),
         ("nisha",28),
]

age = lambda data:data[1] >=18

drinking_buddies=list(filter(age,friends))

for i in drinking_buddies:
    print(i)
