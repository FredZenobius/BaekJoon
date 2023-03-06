# num = int(input())
# for i in range(1, num+1) :
#     for j in range(num, 0, -1) :
#         if j > i :
#             print(" ", end='')
#         else:
#             print("*", end='')
#     print()

num = int(input())
for i in range(1, num+1) :
    star_string = ""
    for j in range(1, i+1) :
        star_string += "*"
    print(star_string.rjust(num))