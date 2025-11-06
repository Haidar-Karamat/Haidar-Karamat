def pascal_triangle(l):#l->level
    for i in range(l):
        print(" " * (l-i), end=" ") #spacing

        val = 1
        for j in range(i + 1):
            print(val, end= " ")
            val = val * (i - j) // (j + 1)  # binomial coefficient
        print()


pascal_triangle(8)