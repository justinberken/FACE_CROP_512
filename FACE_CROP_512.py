import os
import cv2
import glob
from mtcnn import MTCNN
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QSpinBox, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit

def get_images(directory):
    image_formats = ('*.jpg', '*.jpeg', '*.png', '*.bmp')
    image_paths = []
    for format in image_formats:
        image_paths.extend(glob.glob(os.path.join(directory, format)))
    return image_paths

def crop_and_save_faces(image_path, detector, padding, output_dir):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    faces = detector.detect_faces(image)
    for i, face in enumerate(faces):
        x, y, w, h = face['box']
        x -= padding
        y -= padding
        w += padding * 2
        h += padding * 2

        # Adjust width and height to maintain a 1:1 aspect ratio
        if w > h:
            diff = w - h
            y -= diff // 2
            h = w
        else:
            diff = h - w
            x -= diff // 2
            w = h

        # Ensure the face bounding box stays within the image boundaries
        x = max(0, x)
        y = max(0, y)
        w = min(w, width - x)
        h = min(h, height - y)

        cropped_face = image[y:y+h, x:x+w]
        resized_face = cv2.resize(cropped_face, (512, 512))

        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(image_path))[0]}_face_{i}.jpeg")
        cv2.imwrite(output_path, resized_face)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        label_input_dir = QLabel("Input Directory:")
        self.edit_input_dir = QLineEdit()
        button_input_dir = QPushButton("Browse...")
        button_input_dir.clicked.connect(self.browse_input_dir)
        
        label_padding = QLabel("Padding:")
        self.spin_padding = QSpinBox()
        self.spin_padding.setMinimum(0)
        self.spin_padding.setMaximum(100)
        self.spin_padding.setValue(10)
        
        label_output_dir = QLabel("Output Directory:")
        self.edit_output_dir = QLineEdit()
        button_output_dir = QPushButton("Browse...")
        button_output_dir.clicked.connect(self.browse_output_dir)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        
        button_start = QPushButton("Crop Faces")
        button_start.clicked.connect(self.crop_faces)
        
        input_dir_layout = QHBoxLayout()
        input_dir_layout.addWidget(label_input_dir)
        input_dir_layout.addWidget(self.edit_input_dir)
        input_dir_layout.addWidget(button_input_dir)
        
        padding_layout = QHBoxLayout()
        padding_layout.addWidget(label_padding)
        padding_layout.addWidget(self.spin_padding)
        
        output_dir_layout = QHBoxLayout()
        output_dir_layout.addWidget(label_output_dir)
        output_dir_layout.addWidget(self.edit_output_dir)
        output_dir_layout.addWidget(button_output_dir)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_dir_layout)
        main_layout.addLayout(padding_layout)
        main_layout.addLayout(output_dir_layout)
        main_layout.addWidget(self.log_text)
        main_layout.addWidget(button_start)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Face Crop 512")
        self.setGeometry(100, 100, 500, 500)
    
    def browse_input_dir(self):
        input_dir = QFileDialog.getExistingDirectory(self, "Select Input Directory")
        self.edit_input_dir.setText(input_dir)
        
    def browse_output_dir(self):
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        self.edit_output_dir.setText(output_dir)
        
    def crop_faces(self):
        input_dir = self.edit_input_dir.text()
        padding = self.spin_padding.value()
        output_dir = self.edit_output_dir.text()
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        detector = MTCNN()
        image_paths = get_images(input_dir)
        
        for image_path in image_paths:
            crop_and_save_faces(image_path, detector, padding, output_dir)
            self.log_text.append(f"Cropped faces in {image_path}")
        
        self.log_text.append("Faces cropped and saved successfully.")

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()

