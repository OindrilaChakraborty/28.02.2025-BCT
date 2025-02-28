x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
try:
    z=x/y
    print("Division Result: ", z)

except ZeroDivisionError:
    print("Invalid attempt of division")
    
# except Exception as a:
#     print(a)
print("Hello this line is last line")

