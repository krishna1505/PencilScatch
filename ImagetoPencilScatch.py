import cv2  
# Read the input image (Enter your file name with extension)
image = cv2.imread("pic.jpeg")  # Example: 'pic.jpeg'
# Convert the image to grayscale
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Invert the grayscale image
invert = cv2.bitwise_not(grey_img)
# Apply Gaussian Blur to the inverted image
blur = cv2.GaussianBlur(invert, (21, 21), 0)
# Invert the blurred image
invertedblur = cv2.bitwise_not(blur)
# Create the sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
# Save the final sketch image (Enter your output file name with extension)
cv2.imwrite("MyPic.jpeg", sketch)  # Example: 'MyPic.jpeg'
