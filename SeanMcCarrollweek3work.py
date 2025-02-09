# for part 1
user_name = input("What is your name?")
print(f"Hello {user_name}!")

# For Part 2
# print(user_age + 5) throws an error because it is attempting to concatenate a string data type
# with a non string data type
# working code is below(working in the sense that it won't throw a type error)
user_age = input("What is your age?")
print(user_age + str(5))
# For Part 3
print(f'In 5 years you will {str(int(user_age)+5)} years old.')
# For Part 4
float_hours_worked = input("how many hours have you worked in this week")
float_hourly_wage = input("how much do you make an hour")
float_hours_worked = float(float_hours_worked)
float_hourly_wage = float(float_hourly_wage)
print(f'estimated weekly compensation is {str(float_hours_worked*float_hourly_wage)}')
print(f'estimated annual compensation is {str(float_hourly_wage*float_hours_worked*50)}')
