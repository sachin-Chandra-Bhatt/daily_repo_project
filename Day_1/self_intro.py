#  create a self introduction program in python 
# in which user can enter his/her name, age, and city , profession , and hobby
# and the program will print a self introduction message

def self_introduction():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    city = input("Enter your city: ").strip()
    profession = input("Enter your profession: ").strip()
    hobby = input("Enter your hobby: ").strip()
    borders = "=" * 80
    self_intro_format = (
        f"{borders}\n"
        f"Hello, my name is {name}, and I am {age} years old, and I live in {city}.\n"
        f"I work as a {profession}, and in my free time, I enjoy {hobby}.\n"
        f"{borders}\n"
    )
    print(f"\n {self_intro_format}")

self_introduction()

