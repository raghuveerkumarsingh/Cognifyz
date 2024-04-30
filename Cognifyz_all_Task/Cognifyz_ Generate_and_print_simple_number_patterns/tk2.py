num= int(input("Enter the number of rows:  "))
def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")
        for k in range(1, i * 1):
            print("*", end=" ")
        print()
print_pyramid(num)
