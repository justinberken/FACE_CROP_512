Face Crop 512 v0.4

Face Crop 512 is a Python script that uses the MTCNN face detector to detect and crop faces from images while maintaining a 1:1 aspect ratio. The cropped faces are resized to 512x512 pixels. The script also provides a simple PyQt5-based graphical user interface (GUI) to select input and output directories and set the padding value.
Requirements

    Python 3.6 or newer
    OpenCV
    MTCNN
    PyQt5
    tensorflow 

To install the required packages, run:

bash

pip install opencv-python mtcnn PyQt5 tensorflow

Usage

    Run the script with python face_crop_512.py.
    In the GUI, click "Browse..." to select an input directory containing the images you want to process.
    Click "Browse..." to select an output directory where the cropped face images will be saved.
    Set the "Padding" value using the spin box. The padding is specified as a percentage of the smallest image dimension. A value of 0% results in the original bounding box, while 100% extends to the full extent of the smallest dimension of the photograph.
    Click "Crop Faces" to start the processing. The script will process each image in the input directory, detect the face with the largest bounding box, crop it with the specified padding, and save the result in the output directory.

Notes

    The script is designed to work with various image formats, including JPEG, PNG, and BMP.
    It will only crop the face with the largest original bounding box in each image.
    The output images will always have a 1:1 aspect ratio and will be resized to 512x512 pixels.
    If the padding value is too high, it may cause the bounding box to extend beyond the image boundaries. The script will automatically ensure that the bounding box stays within the image boundaries.

License

This project is released under the MIT License.