from datetime import *
#for first section
print('Hello world!, My first program')
pet_name = "Cody"
pet_type = "Dog"
print(f"I have a {pet_type} his name is {pet_name}")

# for second section
name = input("What is your name? ")
age = input("What is your age? ")
savings = input("What is your yearly savings? ")
age10 = int(age) + 10
savings5 = int(savings) * 5
savings_month = int(savings)/ 12
print(f"Hello {name}! You are {age} years old")
print(f"In 10 years, your age will be {age10}")
print(f"In 5 years, your savings will be: {savings5}")
print(f"You save on average {savings_month} a month")

#for third section
current_month = date.today().month
if current_month == 1 or current_month == 3 or current_month == 5 or current_month == 7 or current_month == 8 or current_month == 10 or current_month == 11 or current_month == 12:
    num_days = current_month * 31
elif current_month == 4 or current_month == 6 or current_month == 9:
    num_days = current_month * 30
elif current_month == 2:
    num_days = current_month * 28
else:
    print("Python date time is broken, this error isn't my fault")
num_seconds = num_days * 86400
print(f"The number of seconds in this month is {num_seconds}")
#for fourth section
num_eggs = input("How many eggs do you have? ")
num_dozens = int(num_eggs) / 12
num_leftovers = int(num_eggs) % 12
num_dozens = int(num_dozens)
print(f'You have {num_dozens} dozen(s) of eggs with {num_leftovers} eggs leftover')