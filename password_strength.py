import getpass


def get_password_strength(password):
    password_strength = 0
    return password_strength


if __name__ == '__main__':
    password = getpass.getpass("Input password: ")
    print("Password strenght is {0}".format(
        get_password_strength(password)))
