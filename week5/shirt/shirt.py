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

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

# Open the shirt overlay image
shirt = Image.open("shirt.png")

# Resize and crop the input image to match the shirt's dimensions
fitted = ImageOps.fit(input_image, shirt.size)

# Overlay the shirt image on top of the resized image using transparency
fitted.paste(shirt, shirt)

# Save the final image to the output file specified by the user
fitted.save(sys.argv[2])

