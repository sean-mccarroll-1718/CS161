# For part 1
def average_of_3(num1, num2, num3):
    """takes the average of 3 numbers and returns it"""
    return (num1 + num2 + num3) / 3
print(average_of_3(1, 2, 3))
print(average_of_3(40, 30, 17))
# For part 2. No that will not run because the function is not defined before it is called
# For 3 that will cause an error as well because num1 is defined as an argument and that only pertains the
# function and the code within the function not code outside the function
# For Part 4 & 6 I innutively used the return function rather than doing it in the function
def dog_age(dog_age_human):
    return 24 + (dog_age_human - 2) * 4
dog_age_human = int(input("Enter your dog's age in human years: "))
print(f"{dog_age_human} years old in human years which means they are {str(dog_age(dog_age_human))} years old in dog years")

# For Part 5
def car_value_loss(car_age, car_type, car_price):
    if car_type == "Japanese":
        new_value = car_price
        for x in range(car_age):
            new_value = 0.93 * new_value
        print(f"The value of this {car_type} car will be {int(new_value)} after {car_age} years")
    elif car_type == "German":
        new_value = car_price
        for x in range(car_age):
            new_value = 0.95 * new_value
        print(f"The value of this {car_type} car will be {int(new_value)} after {car_age} years")
    elif car_type == "Italian":
        new_value = car_price
        for x in range(car_age):
            new_value = 0.95 * new_value
        print(f"The value of this {car_type} car will be {int(new_value)} after {car_age} years")
    else:
        print("data for type entered is not provided")
car_type = input("Enter your car type German, Italian, or Japanese: ")
car_price = float(input("Enter your car price as an number: "))
car_age = int(input("Enter your car age in years as a integer: "))
car_value_loss(car_age, car_type, car_price)
# For Part 7
def ice_cream_cone_price(number_of_scoops):
    cost = int(number_of_scoops) * 1.15 + 2.25
    print(f'This ice cream cone will ${cost}')

number_of_scoops = int(input("How many scoops do you want? "))
ice_cream_cone_price(number_of_scoops)