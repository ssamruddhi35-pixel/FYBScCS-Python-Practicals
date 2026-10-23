Question 5. Password Vault with Five Failed Attempts
pin = "123456"
attempts = 0

while attempts < 5:
    entered = input("Enter 6-digit PIN: ")

    if entered == pin:
        print("Access granted")
        break

    attempts += 1
    print("Incorrect PIN")

else:
    print("Access blocked")
