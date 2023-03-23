Face Crop 512

Face Crop 512 is a Python script that uses OpenCV, MTCNN and Tensorflow libraries to detect and crop faces from images. The cropped faces are saved as separate 512x512 images with a 1:1 aspect ratio. The script also includes a PyQt5-based graphical user interface for easy usage.
Requirements

    Python 3.6 or higher
    opencv-python
    mtcnn
    PyQt5
    tensorflow

Installation

    Ensure you have Python 3.6 or higher installed.
    Install the required libraries using pip:

bash

pip install opencv-python mtcnn PyQt5 tensorflow

Usage

    Run the face_crop_512.py script:

bash

python face_crop_512.py

    The GUI window will open. Click the "Browse..." button next to "Input Directory" and select the directory containing the images you want to process.
    Set the "Padding" value as desired. This value will determine the additional padding around the detected face bounding box.
    Click the "Browse..." button next to "Output Directory" and select the directory where you want to save the cropped face images.
    Click the "Crop Faces" button to start processing the images. The cropped faces will be saved in the output directory.

How It Works

    The script uses the MTCNN library to detect faces in the input images.
    It then crops the faces, maintaining a 1:1 aspect ratio, and adds padding around the face bounding box as specified by the user.
    The cropped faces are resized to 512x512 pixels and saved as separate JPEG images in the output directory.

License

This project is released under the MIT License.

Save this content as README.md in the same directory as your script. The README file provides an overview of the project, installation instructions, and a description of how the script works.
