def free_calc(num1, num2):
    product = n1 * n2
    the_sum= n1 + n2
    if product < 1000:
        print(f"Result is {product}")
    else:
        print(f"Result is {the_sum}")

n1 = int(input("Give me a first number:\n "))
n2 = int(input("Give me a second number:\n "))

free_calc(num1=n1, num2=n2)
