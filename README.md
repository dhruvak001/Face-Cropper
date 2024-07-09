# Face Cropper

This project utilizes OpenCV (Open Source Computer Vision Library) to perform face detection and cropping on images. It includes a Python class Fdac which encapsulates the functionalities for detecting faces and cropping them based on predefined criteria...
This file detects all the images present in a given inout image with an **Accuracy 83%**

## **Features**<br/>
- **Face Detection:** Utilizes Haar Cascade Classifier to detect frontal faces within input images.<br/>
- **Face Cropping:** Cropping functionality implemented to extract faces from detected regions based on specified conditions.<br/>
- **Skin Masking:** Implements a skin mask algorithm to ensure accurate face detection by filtering out non-skin areas.<br/>
- **Configurability:** Allows customization of minimum face size for cropping to ensure desired image output.<br/>

## **Requirements**<br/>
- Python 3.x<br/>
- OpenCV (cv2)<br/>
- Numpy<br/>

## **Usage**<br/>
- Initialize the Fdac class with the path to the input image.<br/>
- Call the detector() method to detect faces within the image.<br/>
- Call the cropper() method to crop detected faces based on specified conditions.<br/>
- Output images with cropped faces will be saved with filenames prefixed by "cropped_image_".<br/>
