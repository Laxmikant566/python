# N = int(input())
# for i in range(1,N+1):
#   for j in range(1,N+1):
#     if(j%2==0):
#       print("*",end=" ")
#     else:
#       print(j,end=" ")
#   print()



# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")

#     for k in range(i):
#         print("*", end="")

#     print()


N = int(input())
for i in range(1,N+1):
     for j in range (N-i):
        print(" ",end=" ")
     for k in range (i):
        print("*",end=" ")
     print()      