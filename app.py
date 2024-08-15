import os

import tensorflow as tf
import cv2
#import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
#from tensorflow.keras.layers import TFSMLayer



def predict(img):
    model=tf.keras.models.load_model("cat_dog_classifier")
    img=cv2.resize(img,(224,224))
    img=np.resize(img,(1,224,224,3))
    ans=model.predict(img)
    if ans==1:
        return 'Dog'
    else:
        return 'Cat'


#model1=tf.keras.models.load_model("cat_dog_classifier")
#image=cv2.imread('dog.jpg')
#plt.imshow(image)
#ans=predict(image,model1)
#print(ans)

# Lets Start making the streamlit app


file=st.file_uploader("Image to Upload")
if file:
    if st.button('Upload'):
        with open('temp.png','wb') as f:
            data=file.read()
            f.write(data)
        st.image('temp.png')
        with st.spinner("Classifing..."):
            image = cv2.imread('temp.png')
            ans=predict(image)
        st.title(ans)
        os.remove('temp.png')

