import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras import backend as K
import numpy as np

# Your existing code for model loading and preprocessing
model_path = 'D:/Signature_model_new/saved_model_new'
K.clear_session()
model = tf.keras.models.load_model(model_path)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((112, 112))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32')
    return image

# Create a simple Tkinter GUI
class SignatureVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature Verification App")

        self.image1_path = ''
        self.image2_path = ''

        # Buttons to select images
        tk.Button(root, text="Select Test Image 1", command=self.load_image1).pack(pady=10)
        tk.Button(root, text="Select Test Image 2", command=self.load_image2).pack(pady=10)

        # Display images
        self.image1_label = tk.Label(root)
        self.image1_label.pack(pady=5)
        self.image2_label = tk.Label(root)
        self.image2_label.pack(pady=5)

        # Button to perform verification
        tk.Button(root, text="Verify Signature", command=self.verify_signature).pack(pady=10)

        # Label to display verification result and similarity score
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def load_image1(self):
        self.image1_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.display_image(self.image1_path, self.image1_label)

    def load_image2(self):
        self.image2_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.display_image(self.image2_path, self.image2_label)

    def display_image(self, image_path, label):
        if image_path:
            image = Image.open(image_path)
            image = ImageTk.PhotoImage(image.resize((200, 200)))
            label.config(image=image)
            label.image = image

    def verify_signature(self):
        if self.image1_path and self.image2_path:
            test_image1 = preprocess_image(self.image1_path)
            test_image2 = preprocess_image(self.image2_path)

            prediction = model.predict([test_image1, test_image2])

            similarity_score = prediction[0][0]
            result = f"Similarity Score: {similarity_score:.4f}\n"
            if similarity_score < 0.99:
                result += "Signature is  FORGED"
            else:
                result += "Signature not FORGED"
            self.result_label.config(text=result)

# Create and run the Tkinter app
root = tk.Tk()
app = SignatureVerificationApp(root)
root.mainloop()
