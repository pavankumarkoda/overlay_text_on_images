from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# Replace these paths and variables with your own
input_folder = "images"
output_folder = "savedimages"
new_number = "XXXXXXXXXX01" #todays date
font_path = "Roboto-Bold.ttf"  # Replace with the path to your .ttf font file
font_size = 24
text_color = (0, 0, 0)  # Black color for text
background_color = (210, 210, 210)  # White color for background

def overlay_number(image_path):
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        # Load custom TrueType font
        font = ImageFont.truetype(font_path, font_size)
        
        # Get bounding box of the main number text
        text_width, text_height = draw.textbbox((10, 10), new_number, font=font)[2:]
        
        # Draw background rectangle for the main number text
        draw.rectangle((10, 10, 10 + text_width, 10 + text_height), fill=background_color)
        
        # Draw the main number text on image
        draw.text((10, 10), new_number, font=font, fill=text_color)
        
        # Get the current date and time in the desired format
        current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Get bounding box for the current date and time text
        date_time_width, date_time_height = draw.textbbox((10, 10), current_datetime, font=font)[2:]
        
        # Position for the date/time text, below the main number
        date_time_position = (10, 10 + text_height + 5)
        
        # Draw background rectangle for the date/time text
        draw.rectangle((10, date_time_position[1], 10 + date_time_width, date_time_position[1] + date_time_height), fill=background_color)
        
        # Draw the current date and time text on the image
        draw.text(date_time_position, current_datetime, font=font, fill=text_color)
        
        # Save modified image
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        img.save(output_path)
        
        print(f"Processed: {os.path.basename(image_path)}")
        
    except Exception as e:
        print(f"Error processing {os.path.basename(image_path)}: {str(e)}")
    
    finally:
        # Close image
        img.close()

# List all image files in the input folder
try:
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
except NotADirectoryError:
    image_files = [os.path.basename(input_folder)]

# Process each image
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    overlay_number(image_path)

print("Processing complete.")
