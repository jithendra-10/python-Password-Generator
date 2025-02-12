import random
import string
def generate_passwoed(length=12):
    char=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(char)for _ in range(length))
length=int(input("ENTER PASSWORD LENGTH: "))
password=generate_passwoed(length)
print(f"GENERATED PASSWORD: {password}")