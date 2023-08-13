import random

while True:
    user_confirmation = input('\nThis is a password generator. '
                              'Enter "y" if you want to generate a password or "n" '
                              'if you do not want to.\n')
    if user_confirmation == 'y':
        password = ''
        counter = 0
        for i in range(random.randrange(8, 21)):
            password += random.choice(
                list("""1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZX"""
                     """CVBNM[]{};:""''`\|<>,.?/-=+_!@#$%^&*()~%?""")
            )
            counter += 1
        print(f"Password: {password}\nNumber of symbols: {counter} symbols")
    elif user_confirmation == 'n':
        break
