Overview:
The Optical Character Recognition (OCR) project converts images of text into machine-readable text format. This allows users to take scanned documents or images containing text and convert them into editable and searchable text documents.

Technologies Used:

    Python: The primary programming language used for the project.
    TensorFlow and Keras: Used for building and training the Convolutional Neural Network (CNN) for character recognition.
    OpenCV: Utilized for image processing tasks such as converting images to grayscale, blurring, and edge detection.
    PyTesseract: A Python wrapper for Google's Tesseract-OCR Engine, used for extracting text from images.
    PyQt5: Used for building the graphical user interface (GUI) of the application.

Project Structure:

    model.h5: Pre-trained model file for the CNN.
    OCR.py: Main Python script containing the implementation for loading the model, preprocessing the images, and recognizing text.
    README.md: Documentation file providing an overview and setup instructions.
    sample_image: Directory containing sample images used for testing the OCR.

Implementation Details:

    Model Training:
        Dataset: Extended MNIST dataset (EMNIST) is used, which includes handwritten digits and alphabets.
        Preprocessing: The images are resized, normalized, and split into training and testing sets.
        CNN Architecture: A Sequential CNN model is built using Keras, which includes layers such as Convolutional, MaxPooling, and Dense layers.
        Training: The model is trained on the EMNIST dataset, and the training performance is visualized using matplotlib.

    Image Recognition:
        Image Loading and Preprocessing: The input image is converted to grayscale and blurred to reduce noise.
        Edge Detection: Canny edge detection is used to highlight the edges of the characters in the image.
        Contour Detection: Contours of the characters are identified and filtered based on size.
        Character Extraction: Each contour is extracted, thresholded, and resized to match the input size expected by the CNN.
        Prediction: The pre-trained CNN model predicts the character for each contour, and the results are displayed on the image.

Setup Instructions:

        Clone the Repository:
        
            git clone https://github.com/Mudit2003/OpticalCharacterRecognition.git
            cd OpticalCharacterRecognition

Install Dependencies:


    pip install tensorflow matplotlib opencv-python pytesseract pyqt5

Run the Application:

    python OCR.py

Usage:

    Modes: The application can operate in two modes: 'image' mode for recognizing text in static images and 'webcam' mode for live video capture and text recognition.
    Pre-trained Model: The pre-trained model (model.h5) can be used to skip the training process and directly perform recognition.
