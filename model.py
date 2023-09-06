import cv2
import numpy as np
from PIL import Image, ImageEnhance


class ImageModel:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
        )
        self.smile_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
        )

    def load_image(self, img):
        im = Image.open(img)
        return im

    def detect_faces(self, our_image):
        new_img = np.array(our_image.convert("RGB"))
        img = cv2.cvtColor(new_img, 1)
        gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img, faces

    def detect_eyes(self, our_image):
        new_img = np.array(our_image.convert("RGB"))
        img = cv2.cvtColor(new_img, 1)
        gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, 1.3, 5)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return img

    def detect_smiles(self, our_image):
        new_img = np.array(our_image.convert("RGB"))
        img = cv2.cvtColor(new_img, 1)
        gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        # Detect Smiles
        smiles = self.smile_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the Smiles
        for x, y, w, h in smiles:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img

    def cartonize_image(self, our_image):
        new_img = np.array(our_image.convert("RGB"))
        img = cv2.cvtColor(new_img, 1)
        gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        # Edges
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        # Color
        color = cv2.bilateralFilter(img, 9, 300, 300)
        # Cartoon
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        return cartoon

    def cannize_image(self, our_image):
        new_img = np.array(our_image.convert("RGB"))
        img = cv2.cvtColor(new_img, 1)
        img = cv2.GaussianBlur(img, (11, 11), 0)
        canny = cv2.Canny(img, 100, 150)
        return canny

    def adjust_brightness(self, our_image, brightness):
        enhancer = ImageEnhance.Brightness(our_image)
        return enhancer.enhance(brightness)
