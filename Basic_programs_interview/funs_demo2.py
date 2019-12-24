# user define function
def greet(user, msg):
    print(f"Hello,{user} {msg}")


# positional argument
greet('sindhu', 'Good morning')
greet('How are you', 'Naveen')

# keyword argument
greet(msg="How are you", user="Naveen")
