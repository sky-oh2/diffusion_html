from PIL import Image, ImageDraw, ImageFont
import sys

def create_image(font_style, text):
    # Set the font size and create an ImageFont object
    font_size = 30
    font_path = f'fonts/{font_style}-Regular.ttf'
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the width and height based on the text size
    text_width, text_height = font.getsize(text)
    width = text_width + 20  # Add some padding
    height = text_height + 20  # Add some padding

    # Create a blank image
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw text on the image
    x = 10  # Padding
    y = 10  # Padding
    draw.text((x, y), text, font=font, fill='black')

    # Save the image
    image_path = 'font_image_result.png'
    image.save(image_path)

    return image_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python font_to_image.py <font_style> <text>")
        sys.exit(1)

    font_style = sys.argv[1]
    text = sys.argv[2]

    result_image_path = create_image(font_style, text)
    print(f"Result image saved at: {result_image_path}")
