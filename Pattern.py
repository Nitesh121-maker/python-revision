num = int(input("Enter the Num:"))

for i in range(0,num):
    for j in range(0,num-i):
      print("*",end=" ")
    for j in range(0,i):
      print("#",end=" ")
    print("")
    
for i in range(0,num+1):
    for j in range(0,num-i):
      print("#",end=" ")
    for j in range(0,i):
      print("*",end=" ")
    print()

# Output
# Enter the Num:5
# * * * * * 
# * * * * #
# * * * # #
# * * # # #
# * # # # #
# # # # # #
# # # # # *
# # # # * *
# # # * * *
# # * * * *
# * * * * *