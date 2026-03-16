import sys
from PIL import Image, ImageOps

# Ensure the correct number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Validate extensions
elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")
elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

# Ensure extensions match
elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Input and output have different extensions")

# Try to open the file, if it doesn't exist >> Error
try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

# Open the shirt overlay image
shirt = Image.open("shirt.png")

# Resize and crop the input image so it has the same size as the shirt
fitted = ImageOps.fit(input_image, shirt.size)

# Put the shirt image on top of the resized image
fitted.paste(shirt, shirt)

# Save the final image to the output file
fitted.save(sys.argv[2])

