import random

# chars = ['0'...'9']


def encrypt(plain, key):
    encrypted_text = ""

    # 1234 -> 2345 with key of 1

    for char in plain:
        num = int(char)
        shifted_num = (num + key) % 10
        encrypted_text += str(shifted_num)

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)


if __name__ == "__main__":
    pins = [
        "1234",
        "9876",
        "0000",
        "9999",
    ]

    for pin in pins:
        key = random.randint(1, 9)
        print("plain pin", pin)
        encrypted_pin = encrypt(pin, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)
