from PIL import Image

def encrypt_image(input_path, output_path):
    try:
        image = Image.open(input_path)
        pixels = image.load()

        for y in range(image.height):
            for x in range(image.width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)  # Swap R and B channels

        image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path):
    # Decryption is the same as encryption
    encrypt_image(input_path, output_path)

# Example usage:
input_image_path = "input_image.jpg"
encrypted_image_path = "encrypted_image.jpg"
decrypted_image_path = "decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path)
