name = input("What is your name? ")
score = int(input("Enter your score: "))

if score >= 80:
    print(name, "you got an A.")
elif score >= 70:
    print(name, "you got a B.")
elif score >= 60:
    print(name, "you got a C.")
elif score >= 50:
    print(name, "you got a D.")
else:
    print(name, "you failed.")