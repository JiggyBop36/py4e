smallest=0
print("Before")
for value in[3,5677,4455,2345,2,3,-5]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest, value)
print("Ater", smallest)
