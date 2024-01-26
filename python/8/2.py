k = 1
l = 1
m = 0
n = 0
print(bool((not k or m) or (not l or m or n)))


print(bool(0 or 1 and not(0 or 1)))
print(bool(1 or 0 and 1 and 1 and 0 or 1))
print(bool((1 or 0) and (1 and 1)))

a = 0
b = 0
print(bool(((a or 0) or b and 1) and 0))

x1 = 0
x2 = 1
x3 = 1
x4 = 1
# ¬ - not   ˅ - or    ˄ - and
print("=" * 40)
print(int((x1 or not x2) and (not x3 or x4)))
print(int((not x1 or x3) and x2 or x4))
print(int(x1 and x2 or (not x3 or (x1 or x4))))

