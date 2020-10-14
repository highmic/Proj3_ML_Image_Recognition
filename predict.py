# Dependencies
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input


#load model
model = load_model('saved_models/keras_cifar10_trained_model.h5')

#define global variables
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
image_size = (32, 32)

#define predict function with variables that changes for new input
def predict_new(image_new):
    #Preprocess image for scaling and normalization for h5
    img = image.load_img(image_new, target_size=image_size) 
    x = image.img_to_array(img)   
    x = preprocess_input(x)
    img = np.reshape(img,[1,32,32,3])
    #np.argmax return array value with the highest probability
    classes = np.argmax(model.predict(img), axis = 1)
    names = [class_names[i] for i in classes]
    return names

