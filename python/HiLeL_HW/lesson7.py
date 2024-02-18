list_s = [10, 4, 2, 6, 8, 1]
print("The given list is:", list_s)
res_ = 0
for list_ in list_s:
    res_ = res_ + list_
print("Sum of all the elements in the list is:", res_)

list_s = [10, 4, 2, 6, 8, 1, 10, 10, 10]
res_ = 10
count = 0
for list_ in list_s:
    if list_ == res_:
        count = count + 1
print(count)

list_s=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]
res_ = int(input("Enter number: "))
for list_ in list_s:
    if list_ == res_:
        print (f"number {res_} in list")
        break
else:
    print(f"number {res_} not in list")

