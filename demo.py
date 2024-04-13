ll = [1,2,3,4,5,6,7,8,8]

print(type(ll))

print(type(str(ll)))

l2 = [11,22,33]
new = ", ".join(str(num) for num in ll)

print(new)