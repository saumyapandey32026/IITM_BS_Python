# if statement 

birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year

if(age < 13):
    print("You are a child.")
elif(age >= 13 and age < 20):
    print("You are a teenager.")
else:
    print("You are an adult.")