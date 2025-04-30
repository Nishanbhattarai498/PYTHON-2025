#*args:: paramter that will pack all arguments into a tuple
#**kwargs:: parameter that will pack all keyword arguments into a dictionary


def add (*args):
    sum=0
    args=list(args) # convert tuple to list because tuples are immutable and list can be changed 
    

    args[0]=0 # change first element of list to 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5)) # 15