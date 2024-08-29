from cryptography.fernet import Fernet

"""def write():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write()"""


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
        return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account No: ")
    psw = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(psw.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing password?(add/view) (q) for quit it: "
    ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("-----Invalid action!-----")
