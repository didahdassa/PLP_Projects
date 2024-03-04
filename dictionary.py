#DICTIONARY
person_info = {}

# taking user informations and store them in a dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# printing a dictionary
print("Person's Informations are: \n")
for key, value in person_info.items():
    print(f"{key} : {value}")