import time

# print(time.ctime(0))


# print(time.time())


# print(time.ctime(time.time()))

# time_object=time.localtime()
# print(time_object)

# local_time=time.strftime("%B %d %Y %H :%M :%S")
# print(local_time)

# time_string="20 april 2023"
# time_object= time.strptime(time_string)
# print(time_object)

time_tuple=(2024, 4 ,20,4 ,20 ,0 ,0,0 ,0 )
time_string=time.asctime(time_tuple)
print(time_string)
