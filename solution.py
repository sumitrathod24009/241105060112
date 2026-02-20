print("Matrix Addition Program")
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

i = 0
while i < rows:
    j = 0
    while j < cols:
        a = int(input("Enter value for Matrix A: "))
        b = int(input("Enter value for Matrix B: "))

        result = a + b
        print("Sum:", result)

        if result % 2 == 0:
            print("Even value")
        else:
            print("Odd value")

        j = j + 1  # increment column

    i = i + 1  # increment row

print("Matrix addition completed")

if rows == cols:
    print("Square matrix")
else:
    print("Rectangular matrix")
