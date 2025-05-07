#higher order function = a function that either :  accepts  a function  as an arguent or  returns  a function ( in python,functions are also treated as objects)



# def loud(text):
#     return text.upper()

# def quite(text):
#     return text.lower()

# def hello(func):
#     text=func("hello")
#     print(text)


# hello(loud)
# hello(quite)



def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide=divisor(2)
print(divide(10))