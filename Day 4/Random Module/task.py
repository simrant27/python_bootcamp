import random
from secrets import choice

# import my_module
#
# random_integer = random.randint(5,20)
# print(random_integer)

# print(my_module.my_fav_number)

# random_num_0_1 = random.random() *10
# print(random_num_0_1)

# random_float = random.uniform(1,10)
# print((random_float))

ran_num = random.randint(0,1)
if ran_num == 0 :
    print("Heads")
else:
    print("Tails")