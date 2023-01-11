# Plaintext: 1234
# key: 2
# Ciphertext: 3456

# Plaintext: 4789
# key: 2
# Ciphertext: 6901

def encrypt(plaintext, key):
    """
    Takes in a string integers representing the plaintext, and return a new string of integers
    shifted by a key, mod 10 ("number wrap")

    :param plaintext: string of integers
    :param key: integer
    :return: string of integers
    """
    ciphertext = ""

    # looping through a string
    for char in plaintext:
        # "3" -> 3
        num = int(char)
        shift_num = (num + key) % 10  # e.g. 12 % 10 -> 2
        # build up the ciphertext string
        ciphertext += str(shift_num)

    return ciphertext


def decrypt(ciphertext, key):
    """
    Reverse encrypt() operation with original key as an argument.

    :param ciphertext: string of integers
    :param key: integer
    :return: string of integers
    """
    return encrypt(ciphertext, -key)


if __name__ == "__main__":
    phone_number = "8005551234"
    print(f"the phone_number is: {phone_number}")
    encrypted_phone_number = encrypt(phone_number, 2)
    print(f"the encrypted phone number is: {encrypted_phone_number}")
    decrypted_phone_number = decrypt(encrypted_phone_number, 2)
    print(f"the decrypted phone number is: {decrypted_phone_number}")
