import json
import cv2
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from PIL import Image
import tempfile
import os
from sklearn.decomposition import PCA
import warnings
from sklearn.model_selection import train_test_split
#from Bio_Epidemiology_NER.bio_recognizer import pdf_annotate

main = Flask(__name__)
CORS(main)

main.config['SECRET_KEY'] = 'rnsit'

@main.route('/braintumor',methods=['POST'])
def braintumor():
    image_file = request.files['image']
    model = SVC()  
    image = Image.open(image_file)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')
    path = os.listdir('C:/Users/kambo/Downloads/datasets all/datasets all/brain-tumor-detection-master/brain-tumor-detection-master/brain_tumor/Training/')
    classes = {'no_tumor':0, 'pituitary_tumor':1}
    X = []
    Y = []
    for cls in classes:
        pth = 'C:/Users/kambo/Downloads/datasets all/datasets all/brain-tumor-detection-master/brain-tumor-detection-master/brain_tumor/Training/'+cls
        for j in os.listdir(pth):
            img = cv2.imread(pth+'/'+j, 0)
            img = cv2.resize(img, (200,200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated=X.reshape(len(X),-1)
    xtrain,xtest,ytrain,ytest=train_test_split(X_updated,Y,random_state=10,test_size=.20)
    xtrain = xtrain/255
    xtest = xtest/255
    pca = PCA(.98)
    # pca_train = pca.fit_transform(xtrain)
    # pca_test = pca.transform(xtest)
    pca_train = xtrain
    pca_test = xtest
    
    warnings.filterwarnings('ignore')
    sv = SVC()
    sv.fit(pca_train, ytrain)
    image.save(temp_path)
    img = cv2.imread(temp_path, 0)
    img = cv2.resize(img, (200, 200))
    img = img.reshape(1, -1) / 255
    
    # Perform brain tumor detection
    prediction = sv.predict(img)
    
    # Return the result
    result = {
        'prediction': int(prediction),
        'label': 'Positive Tumor' if prediction == 1 else 'No Tumor'
    }
    print(result)
    return jsonify(result)

@main.route('/breastcancer',methods=['POST'])
def breastcancer():
    image_file = request.files['image']
    model = SVC()  
    image = Image.open(image_file)
    image = image.convert('RGB')
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')
    path = os.listdir('C:/Users/kambo/Downloads/datasets all/datasets all/chest-cancer/Data/train/')
    classes = {'normal':0, 'abnormal':1}
    X = []
    Y = []
    for cls in classes:
        pth = 'C:/Users/kambo/Downloads/datasets all/datasets all/chest-cancer/Data/train/'+cls
        for j in os.listdir(pth):
            img = cv2.imread(pth+'/'+j, 0)
            img = cv2.resize(img, (200,200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated=X.reshape(len(X),-1)
    xtrain,xtest,ytrain,ytest=train_test_split(X_updated,Y,random_state=10,test_size=.20)
    xtrain = xtrain/255
    xtest = xtest/255
    pca = PCA(.98)
    # pca_train = pca.fit_transform(xtrain)
    # pca_test = pca.transform(xtest)
    pca_train = xtrain
    pca_test = xtest
    
    warnings.filterwarnings('ignore')
    sv = SVC()
    sv.fit(pca_train, ytrain)
    image.save(temp_path)
    img = cv2.imread(temp_path, 0)
    img = cv2.resize(img, (200, 200))
    img = img.reshape(1, -1) / 255
    
    # Perform brain tumor detection
    prediction = sv.predict(img)
    
    # Return the result
    result = {
        'prediction': int(prediction),
        'label': 'Abnormal' if prediction == 1 else 'Normal'
    }
    print(result)
    return jsonify(result)

@main.route('/skindisease',methods=['POST'])
def skindisease():
    image_file = request.files['image']
    model = SVC()  
    image = Image.open(image_file)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')
    path = os.listdir('C:/Users/kambo/Downloads/datasets all/datasets all/skin-disease/skin_disease/train/')
    classes = {'vascular_lesion':0, 'squamous_cell_carcinoma':1,'seborrheic_keratosis':2,'pigmented_benign_keratosis':3,'melanoma':4 }
    X = []
    Y = []
    for cls in classes:
        pth = 'C:/Users/kambo/Downloads/datasets all/datasets all/skin-disease/skin_disease/train/'+cls
        for j in os.listdir(pth):
            img = cv2.imread(pth+'/'+j, 0)
            img = cv2.resize(img, (200,200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated=X.reshape(len(X),-1)
    xtrain,xtest,ytrain,ytest=train_test_split(X_updated,Y,random_state=10,test_size=.20)
    xtrain = xtrain/255
    xtest = xtest/255
    pca = PCA(.98)
    # pca_train = pca.fit_transform(xtrain)
    # pca_test = pca.transform(xtest)
    pca_train = xtrain
    pca_test = xtest
    
    warnings.filterwarnings('ignore')
    sv = SVC()
    sv.fit(pca_train, ytrain)
    image.save(temp_path)
    img = cv2.imread(temp_path, 0)
    img = cv2.resize(img, (200, 200))
    img = img.reshape(1, -1) / 255
    
    # Perform brain tumor detection
    prediction = sv.predict(img)

    if(prediction==0):
        d="vascular_lesion"
    elif(prediction==1):
        d="squamous_cell_carcinoma"
    elif(prediction==2):
        d="seborrheic_keratosis"
    elif(rediction==3):
        d="pigmented_benign_keratosis"
    else:
        d="melanoma"
    
    # Return the result
    result = {
        'prediction': int(prediction),
        'label': d
            
    }
    print(result)
    return jsonify(result)

@main.route('/eyedisease',methods=['POST'])
def eyedisease():
    image_file = request.files['image']
    model = SVC()  
    image = Image.open(image_file)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')
    path = os.listdir('C:/Users/kambo/Downloads/datasets all/datasets all/eye-disease/train/')
    print('running')
    classes = {'normal':0, 'cataract':1}
    X = []
    Y = []
    for cls in classes:
        pth = 'C:/Users/kambo/Downloads/datasets all/datasets all/eye-disease/train/'+cls
        for j in os.listdir(pth):
            img = cv2.imread(pth+'/'+j, 0)
            img = cv2.resize(img, (200,200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated=X.reshape(len(X),-1)
    xtrain,xtest,ytrain,ytest=train_test_split(X_updated,Y,random_state=10,test_size=.20)
    xtrain = xtrain/255
    xtest = xtest/255
    pca = PCA(.98)
    # pca_train = pca.fit_transform(xtrain)
    # pca_test = pca.transform(xtest)
    pca_train = xtrain
    pca_test = xtest
    print("running2")
    
    warnings.filterwarnings('ignore')
    sv = SVC()
    sv.fit(pca_train, ytrain)
    image.save(temp_path)
    img = cv2.imread(temp_path, 0)
    img = cv2.resize(img, (200, 200))
    img = img.reshape(1, -1) / 255
    print("running3")
    # Perform brain tumor detection
    prediction = sv.predict(img)
    print('running4')
    
    # Return the result
    result = {
        'prediction': int(prediction),
        'label': 'Catract' if prediction == 0 else 'Normal'
    }
    print(result)
    return jsonify(result)

@main.route('/covid',methods=['POST'])
def covid():
    image_file = request.files['image']
    model = SVC()  
    image = Image.open(image_file)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')
    path = os.listdir('C:/Users/kambo/Downloads/archive/Covid19-dataset/train/')
    classes = {'Normal':0, 'Covid':1}
    X = []
    Y = []
    for cls in classes:
        pth = 'C:/Users/kambo/Downloads/archive/Covid19-dataset/train/'+cls
        for j in os.listdir(pth):
            img = cv2.imread(pth+'/'+j, 0)
            img = cv2.resize(img, (200,200))
            X.append(img)
            Y.append(classes[cls])
    X = np.array(X)
    Y = np.array(Y)
    X_updated=X.reshape(len(X),-1)
    xtrain,xtest,ytrain,ytest=train_test_split(X_updated,Y,random_state=10,test_size=.20)
    xtrain = xtrain/255
    xtest = xtest/255
    pca = PCA(.98)
    # pca_train = pca.fit_transform(xtrain)
    # pca_test = pca.transform(xtest)
    pca_train = xtrain
    pca_test = xtest
    
    warnings.filterwarnings('ignore')
    sv = SVC()
    sv.fit(pca_train, ytrain)
    image.save(temp_path)
    img = cv2.imread(temp_path, 0)
    img = cv2.resize(img, (200, 200))
    img = img.reshape(1, -1) / 255
    
    # Perform brain tumor detection
    prediction = sv.predict(img)
    
    # Return the result
    result = {
        'prediction': int(prediction),
        'label': 'Covid' if prediction == 1 else 'Normal'
    }
    print(result)
    return jsonify(result)

# @main.route('/report',methods=['POST'])
# def report():
#     # pdf_file = request.files['pdf']

#     # # Save the PDF to a temporary file
#     # temp_dir = tempfile.gettempdir()
#     # temp_path = os.path.join(temp_dir, 'temp.pdf')
#     # pdf_file.save(temp_path)

#     # # Open the PDF using PyMuPDF
#     # doc = fitz.open(temp_path)
#     # pdfout=pdf_annotate(doc,compute='cpu',output_format='pdf')
#     return true

if __name__ == "__main__":
    main.run()



