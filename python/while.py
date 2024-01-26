
while True:
    ask_num_1 = int(input("could you please put num1 "))
    ask_num_2 = int(input("could you please put num2 "))
    print(ask_num_1 / ask_num_2)
    ask_user = input("Do you want continue? ")
    if ask_user == "yes":
        continue
    else:
        break