def encrypt(message,shift):
    result = ""

    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            result += chr((ord(char) +int(shift)-65)%26 + 65)
        else:
            result += chr((ord(char) +int(shift)-97)%26 + 97)

    return result

def decrypt(message,shift):
    result = ""

    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            result += chr((ord(char) -int(shift)-65)%26 + 65)
        else:
            result += chr((ord(char) -int(shift)-97)%26 + 97)

    return result

message = input('enter a message\n')
shift = input('enter shift\n')

print ("Text  : " +message)
print ("Shift : " +str(shift))
print ("Cipher: " +encrypt(message,shift))
print ("Decrypt: "+decrypt(encrypt(message,shift),shift))