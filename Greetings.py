def greet(name):
    print(f"Hello {name}. Welcome to my program")

# greet("Thina")
# greet("Darth Vader")
# greet("Guido van Rossum")

def name_input():
    prompt = input("Hello, what is your name? ")
    return prompt
#     # print(f"Hello {prompt}, Welcome to my program")

def language_input():
    print("In what language should I greet you in?")
    print("1. Khmer, 2. Mandarin, 3. Japanese")
    userChoice = int(input())
    if userChoice == 1:
        print(f"Chuom reap suor {name_input()}")
    if userChoice == 2:
        print(f"Ni hao {name_input()}")
    if userChoice == 3:
        print(f"Konnichiwa {name_input()}")

language_input()
