number = int(input("Select the number:\n"))
fact = 1
if number < 0:
    print("The number need to be greater than zero")
elif number == 0:
    print("Factorial of 0 is equal to 1")
else:
    for i in range(1, number+1):
        fact = fact*i
print(f"Factorial of {number} is equal to {fact}.")
