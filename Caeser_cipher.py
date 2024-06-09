def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    message = input("Enter your message: ")
    shift_value = int(input("Enter the shift value (positive for encryption, negative for decryption): "))

    encrypted_message = caesar_encrypt(message, shift_value)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = caesar_decrypt(encrypted_message, shift_value)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
