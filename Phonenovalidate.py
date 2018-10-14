# Phno=input("Please input your valid ph no.")

def validatePhno(Phonenumber):
    if len(Phonenumber) != 12:
        return print("Phone number does not have 12 chars")

    for i in range(0, 3):
        if not Phonenumber[i].isdecimal():
            return False

    if Phonenumber[3] is not '-':
        return False

    for i in range(4, 7):
        if not Phonenumber[i].isdecimal():
            return False

    if Phonenumber[7] is not '-':
        return False

    for i in range(8, 12):
        if not Phonenumber[i].isdecimal():
            return False

    return True


# print(validatePhno(Phno))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i + 12]
    if validatePhno(chunk):
        print('Phone number found: ' + chunk)
    print('Done')







