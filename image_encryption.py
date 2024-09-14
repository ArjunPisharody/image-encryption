import os
from PIL import Image
import numpy as np

# Function to swap pixels randomly
def swap_pixels(image_array):
    height, width, channels = image_array.shape  # Handle RGB images
    for i in range(height):
        for j in range(width):
            rand_i = np.random.randint(0, height)
            rand_j = np.random.randint(0, width)
            # Swap RGB values for each color channel
            for c in range(channels):
                image_array[i, j, c], image_array[rand_i, rand_j, c] = image_array[rand_i, rand_j, c], image_array[i, j, c]
    return image_array

# Function to apply a basic mathematical operation (e.g., add a constant)
def modify_pixels(image_array, operation='add', value=50):
    if operation == 'add':
        return np.clip(image_array + value, 0, 255)  # Add a constant
    elif operation == 'multiply':
        return np.clip(image_array * value, 0, 255)  # Multiply by a constant
    return image_array

# Main encryption function
def encrypt_image(input_image_path, output_image_path, method='swap', value=50):
    # Open the image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Apply encryption method
    encrypted_image_array = None  # Initialize to avoid UnboundLocalError

    if method == 'swap':
        encrypted_image_array = swap_pixels(image_array)
    elif method in ['add', 'multiply']:
        encrypted_image_array = modify_pixels(image_array, method, value)
    else:
        print(f"Unknown method: {method}")
        return

    # Ensure the output file has a valid extension, default to '.png'
    if not output_image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        output_image_path += '.png'
    
    # Convert back to image and save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# User Input Section
def main():
    # Asking the user for the input image path
    input_image_path = input("Enter the path of the image you want to encrypt: ")
    
    # Asking the user for the output image path
    output_image_path = input("Enter the output path to save the encrypted image: ")
    
    # Asking the user for the encryption method
    method = input("Choose an encryption method ('swap', 'add', 'multiply'): ").lower()

    # Handling input based on the chosen method
    if method in ['add', 'multiply']:
        value = int(input("Enter the value for the operation (e.g., 50): "))
        encrypt_image(input_image_path, output_image_path, method, value)
    elif method == 'swap':
        encrypt_image(input_image_path, output_image_path, method)
    else:
        print("Invalid method selected. Please choose either 'swap', 'add', or 'multiply'.")

# Run the program
if __name__ == "__main__":
    main()
