#Remember import random function here:
import random
my_list = [4,5,734,43,45]

#The magic is here:
for i in range(10):
    num = random.randint(0,100)
    my_list.append(num)
    i += i

print(my_list)