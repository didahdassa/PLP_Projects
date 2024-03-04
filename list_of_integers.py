#LISTS
#accssing inputs from user
List_of_integers = input("Enter five integers: \n")
user_list = List_of_integers.split()
print('String lists: ', user_list)

#converting the string items to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print('User Lists: ', user_list)
#calclucating sum
print('Sum of the list is ', sum(user_list))
