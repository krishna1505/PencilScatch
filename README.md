# PencilScatch
PencilScatch ✏️🎨
A Python project that converts an input image into a pencil sketch using OpenCV.

Table of Contents 📜
Description

Installation

Usage

Contributing

License

Description 📝
This project takes an input image and applies a series of transformations to convert it into a pencil sketch using OpenCV's image processing techniques. It supports various image formats, and the final output is saved as a sketch in your desired format. 🎨

Installation 💻
To run this project, follow these steps:

Clone the Repository:

bash
Copy
Edit
git clone https://github.com/krishna1505/PencilScatch.git
Install Dependencies: You'll need to install OpenCV for this project. You can install it using pip:

bash
Copy
Edit
pip install opencv-python
Usage 🖼️
Place your image file in the project directory and name it pic.jpeg (or change the filename in the code accordingly).

Run the Python script to generate the sketch:

bash
Copy
Edit
python pencil_sketch.py
The script will process the image and create a pencil sketch as an output (MyPic.jpeg).

Code Explanation 📚
python
Copy
Edit
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
Contributing 🤝
Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to your fork (git push origin feature-branch).

Open a pull request.

