import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

class Fdac:
    
    def __init__(self, image):
        self.image = cv2.imread(image)
        if self.image is None:
             raise ValueError(f"Could not read image file {image}")
        self.face_boxes = face_classifier.detectMultiScale(self.image)

    def cropper(self, min_pixels=75000):
        count = 0       
        for box in self.face_boxes:
            x, y, width, height = box
            x2, y2 = x + width, y + height
            roi = self.image[y:y2, x:x2]
            
            # define skin mask
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            lower_skin = np.array([0, 20, 70], dtype=np.uint8)
            upper_skin = np.array([20, 255, 255], dtype=np.uint8)
            skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
            
            # check if skin area is larger than face area
            if roi.size < min_pixels :
              continue
            if skin_mask.sum() > 0.5 * width * height :
              
              cv2.imwrite(f"cropped_image_{count+1}.png", roi)
              count += 1
                
    def detector(self):
        for box in self.face_boxes:
            x, y, width, height = box
            x2, y2 = x + width, y + height
            cv2.rectangle(self.image, (x, y), (x2, y2), color=(0,0,255), thickness=1) #drawing
        img_to_show = cv2.resize(self.image, (self.image.shape[1], self.image.shape[0]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

image1 = Fdac('/content/sample_data/IMG_0187.JPG')
image1.detector()       
image1.cropper(min_pixels=75000)
