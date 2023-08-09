import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
from  PIL import Image

# import tensorflow
# import tensorflow.keras

# # Imports
# # Cite Lesson 804 - Convolutional Neural Nets
# import numpy as np

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.utils import image_dataset_from_directory
# import tensorflow as tf

# # Image Pre-processing and Augmentation
# from tensorflow.keras.layers import Resizing, Rescaling, CenterCrop
# from tensorflow.keras.layers import RandomCrop, RandomFlip, RandomTranslation, RandomRotation, RandomZoom, RandomContrast

# import os





st.set_page_config(
    page_icon=':hotdog:',
    initial_sidebar_state='expanded'
)

st.title('Hotdog... or not hotdog?')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'Hotdog prediction')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
This Streamlit app hosts my Hotdog model.
We used a convolutional neural network to decipher between 
images of hotdogs and non-hotdogs.
    ''')

elif page == 'Hotdog prediction':
    st.title('Test our model!')

    # Open your model!
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Add file uploader to allow users to upload photos
    uploaded_photo = st.file_uploader("", type='jpg')

    # Create model prediction for uploaded photo
    # hotdog_pred = model.predict([uploaded_photo])[0]

    # Create button
    if st.button('Submit'):

            # if hotdog_pred == 'hotdog':
            #     st.write('This is a hotdog!')
                st.balloons()

            # else:
            #     st.write('This is NOT a hotdog! :-1:')