# Document Forgery Detection and File Classification System  

This repository contains a project aimed at **document classification** and **signature forgery detection** using advanced machine learning techniques. The system uses **OCR** to classify documents (like Aadhar and PAN cards) and applies a **Siamese Neural Network** to detect whether a given signature is genuine or forged.  

## Table of Contents  
- [Features](#features)  
- [Tech Stack](#tech-stack)
- [Model Overview](#model-overview)  
- [Results](#results)  

## Features  
- **OCR-Based Document Classification:**  
  - Classifies documents (Aadhar, PAN) using Optical Character Recognition.  
  - Automates identification and organization of different document types.  

- **Signature Forgery Detection:**  
  - Utilizes a Siamese Neural Network to compare two signatures and determine whether they match.  
  - Helps detect forged signatures effectively.  

- **Preprocessing & Visualization:**  
  - Includes preprocessing techniques for OCR and images for better model performance.  
  - Visualizes signature comparisons and classification results with graphs.

---

## Tech Stack  
- **Python**: Core language for development  
- **TensorFlow/Keras**: Building and training the Siamese Neural Network  
- **OpenCV & Tesseract OCR**: For image processing and text extraction  
- **Matplotlib/Seaborn**: Visualization of results  
- **NumPy & Pandas**: Data manipulation and preprocessing  

---
## Model Overview  
### 1. Document Classification  
- **OCR-based approach**:  
  - Uses **Tesseract OCR** to extract text from document images.
  - Classifies documents based on the presence of keywords like "Aadhar" or "PAN".  
- **Preprocessing Steps**:  
  - Converts images to grayscale.
  - Applies adaptive thresholding to enhance text regions.

### 2. Signature Forgery Detection  
- **Siamese Neural Network Architecture**:  
  - The network takes **two input images** (genuine and test signatures).  
  - Each input passes through identical convolutional layers to extract features.
  - Computes a similarity score using **Euclidean distance**.  
  - If the similarity is below a certain threshold, the signature is flagged as **forged**.

## Results  
### 1. Document Classification Results  
- **Accuracy**: ~95%  
- **Precision**: 93%, **Recall**: 96%  
- **Confusion Matrix**:  
