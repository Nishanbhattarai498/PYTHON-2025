# **kwargs :: parameter that will pack all keyword arguments into a dictionary

def hello(**kwargs):
    # print("Hello", kwargs["First"], kwargs["Last"])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print( value,end=" ")

hello(title="MR",First="Nishan", Last="Bhattarai")