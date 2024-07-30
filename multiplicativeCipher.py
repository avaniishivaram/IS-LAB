def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a')) * int(key)) % 26 + ord('a'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    key_inverse = pow(int(key), -1, 26)
    for char in cipher_text:
        if char.isalpha():
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a')) * int(key_inverse)) % 26 + ord('a'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text
plain_text = input('enter a message\n')
key = input('enter shift\n')

cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)