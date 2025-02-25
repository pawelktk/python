a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta=b*b - 4*a*c

if delta == 0:
    print("1")
elif delta>0:
    print("2")
else:
    print("0")

