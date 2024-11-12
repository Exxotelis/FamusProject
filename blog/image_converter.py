import base64

def convert_image_to_base64(image_path):
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Encode the image as base64
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        # Create the base64 data URL
        mime_type = "image/jpeg" if image_path.endswith(".jpg") or image_path.endswith(".jpeg") else "image/png"
        base64_data_url = f"data:{mime_type};base64,{base64_string}"
        return base64_data_url

# Example usage
image_path = "C:/Users/telis/Python/Images/Atari-50-The-first-console.jpg"
base64_image = convert_image_to_base64(image_path)
print(base64_image)  # This will print the base64 data URL
