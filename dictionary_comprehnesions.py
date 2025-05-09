#dictionary comprehnesions = create dictionary  using an expresion can replace for loop and ceratin lambda functions
#dictionary={key:expression for (key,value) in iterable}
#dictionary={key:expression for (key,value) in iterable if condtion}


cities={
    'New York':32,
    'Boston':75,
    'Los Angles':100,
    'Chicago':50,
    'Manhattan':32,
}


cities_in_c={key:
            round ((value-32)*(5/9))for (key,value) in cities.items()
             }
print(cities_in_c)

