import random
import string

# 1. Random 6 character user ID
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

print(random_user_id())  # e.g. '1ee33d'

# 2. User ID generator by user input
def user_id_gen_by_user():
    length = int(input("Enter number of characters: "))
    count  = int(input("Enter number of IDs: "))
    characters = string.ascii_letters + string.digits
    for _ in range(count):
        user_id = ''.join(random.choice(characters) for _ in range(length))
        print(user_id)

user_id_gen_by_user()

# 3. RGB color generator
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())  # e.g. rgb(125,244,255)
