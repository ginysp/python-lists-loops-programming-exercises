my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1] = "Steven"
my_sample_list[-1] = "Pepe"
my_sample_list[0] = my_sample_list[2] + my_sample_list[4]
newlist=[]
for x in reversed(my_sample_list):
    newlist.append(x)
    print(x)

#my_sample_list = newlist
#print(my_sample_list)

#my_new_list = my_sample_list[::-1]
#print(my_new_list)