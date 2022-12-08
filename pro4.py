our_age = input("what is your age:")
age = int(our_age)
if age >= 18:
    print("your are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")
print("thank you")
