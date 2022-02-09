import os
import random
import string
import qrcode

# Get users input
user_text = input("Enter your text for generate QR code: \n")
permission = input("Change any styles to your QR code? [y/n]: ").strip()

# Advanced QR code customization
if permission == "y":
    # Exception handling
    try:
        # Get users input
        qr_version = float(input("Enter your QR code version: "))
        qr_size = int(input("Enter your QR code size(px): "))
        qr_border = int(input("Enter your QR code border(px): "))
        qr_fill_color = input("Enter your QR code fill color: ")
        qr_back_color = input("Enter your QR code back color: ")

        # Set customizable QR options
        qr_option = qrcode.QRCode(
            version = qr_version or 1,
            box_size = qr_size or 10,
            border = qr_border or 4,
        )

        # Make image & Change the color of the image
        image = qr_option.make_image(fill_color = qr_fill_color or "black", back_color = qr_back_color or "white")
    # Catch invalid input value erorr
    except ValueError:
        print("You typed invalid value!")
    except: 
        print("Something went wrong!")
else:
    # Make default QR code image
    image = qrcode.make(user_text)

# Exception handling
try: 
    # Directory folder name
    directory_name = ("generated_images")
    # Check directory exists or not
    check_directory = os.path.isdir(directory_name)

    # Make directory if it doesn't exist
    if not check_directory:
        os.makedirs(directory_name)
    
    # Generated lowercase letters & Generate random text
    letters = string.ascii_lowercase
    random_text = "".join(random.choice(letters) for i in range(5))

    # Generate a unique filename & Save the image to the directory
    unique_filename = user_text.lower().replace(" ", "_") + "_" + random_text
    image.save(f"generated_images/{unique_filename}.jpg")
    
    print(f"Your QR code has been generated at: 'generated_images/{unique_filename}.jpg'")
except: 
    print("Something went wrong!")