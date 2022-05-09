found=False
print("Before",found)
for item in [3,4,5,67,8,6,54,3,4,6,7,8,76,5,5,4]:
    if item==3:
        found=True
    print(found, item)
print("After",found)
