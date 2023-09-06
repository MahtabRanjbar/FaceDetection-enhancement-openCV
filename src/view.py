import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageEnhance


class ImageView:
    def __init__(self, processor):
        self.processor = processor

    def run(self):
        st.set_option("deprecation.showfileUploaderEncoding", False)

        st.title("Image Processing App")
        st.text("Built with Streamlit and OpenCV")

        activities = ["Detection", "About"]
        choice = st.sidebar.selectbox("Select Activity", activities)

        if choice == "Detection":
            self.detect_activity()
        else:
            self.about_activity()

    def detect_activity(self):
        st.subheader("Image Detection")

        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        if image_file is not None:
            our_image = self.processor.load_image(image_file)
            st.image(our_image, caption="Original Image", use_column_width=True)

            enhance_type = st.sidebar.radio(
                "Enhance Type",
                ["Original", "Gray-Scale", "Contrast", "Brightness", "Blurring"],
            )

            if enhance_type == "Gray-Scale":
                new_img = np.array(our_image.convert("RGB"))
                img = cv2.cvtColor(new_img, 1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # st.write(new_img)
                st.image(gray)
            elif enhance_type == "Contrast":
                c_rate = st.sidebar.slider("Contrast", 0.5, 3.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == "Brightness":
                c_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == "Blurring":
                new_img = np.array(our_image.convert("RGB"))
                blur_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                img = cv2.cvtColor(new_img, 1)
                blur_img = cv2.GaussianBlur(img, (11, 11), blur_rate)
                st.image(blur_img)
            elif enhance_type == "Original":
                st.image(our_image, width=300)
            else:
                st.image(our_image, width=300)

            # Detect faces
            # Face Detection
            task = ["Faces", "Smiles", "Eyes", "Cannize", "Cartonize"]
            feature_choice = st.sidebar.selectbox("Find Features", task)
            if st.button("Process"):
                if feature_choice == "Faces":
                    result_img, result_faces = self.processor.detect_faces(our_image)
                    st.image(result_img)
                    st.success("Found {} faces".format(len(result_faces)))
                elif feature_choice == "Smiles":
                    result_img = self.processor.detect_smiles(our_image)
                    st.image(result_img)

                elif feature_choice == "Eyes":
                    result_img = self.processor.detect_eyes(our_image)
                    st.image(result_img)

                elif feature_choice == "Cartonize":
                    result_img = self.processor.cartonize_image(our_image)
                    st.image(result_img)

                elif feature_choice == "Cannize":
                    result_canny = self.processor.cannize_image(our_image)
                    st.image(result_canny)

    def about_activity(self):
        st.subheader("About")
        st.write(
            "This is a simple image processing app built with Streamlit and OpenCV by ChatGPT."
        )
        st.write(
            "The app can detect faces, eyes, and smiles in an image. It can also cartoonize the image, perform Canny edge detection and adjust brightness."
        )
