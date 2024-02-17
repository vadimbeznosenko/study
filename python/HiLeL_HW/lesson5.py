even_number = 4
odd_number = 3
if not (even_number % 2 == 0) and (type(odd_number) == int):
    print("number is not odd")  
elif not (odd_number % 2 == 0) and (type(odd_number) == int):
    print(f"number {odd_number} is not odd")
else:
    print("see you")


first_num = 2
second_num = 4
third_num = 1
if second_num < third_num and second_num > first_num:
    print(second_num)
elif second_num > third_num and third_num > first_num:
    print(third_num)
else:
    print(first_num)

first_num = 3
second_num = 1
third_num = 2
if third_num > second_num and third_num > first_num:
    print(third_num)
elif second_num > first_num and second_num > third_num:
    print(second_num)
else:
    print(first_num)

first_num = int(input("Enter first num: "))
second_num = int(input("Enter second num: "))
third_num = int(input("Enter third num: "))
if (first_num == second_num and 
    first_num == third_num) and (second_num == third_num and 
    second_num == first_num) and (third_num == first_num and third_num == second_num):
        print("equilateral triangle")
elif (first_num == third_num) or (first_num == second_num) or (second_num == first_num) or (third_num == second_num):
    print("isosceles triangle")
elif (first_num != third_num) and (first_num != second_num) and (third_num != second_num):
    print("scalene triangle")
else:
    print("triangle not found")

first_num = 2
second_num = 5

if first_num % second_num == 0:
    print("number is divided and remainder")
else:
    print("number is not divided")
    print("remainder", first_num % second_num)