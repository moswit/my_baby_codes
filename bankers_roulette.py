import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

count_names=len(names)
select_random_name = random.randint(0,count_names-1)
who_will_pay = names[select_random_name]
print(f"{who_will_pay} is going to buy the meal today!$")
