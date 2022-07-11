from classList import readFile

from flask import Flask, render_template, request
from tensorflow import keras
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import socket

hostname = socket.gethostname()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

MODEL = keras.models.load_model('model.h5')
CLASS = readFile()

def pred(FILE):
    SHAPE = (224, 224)
    IMG = plt.imread(FILE)
    IMG = cv2.resize(IMG,(224,224))
    IMG = IMG.reshape(1,224,224,3)

    PRED = MODEL.predict(np.array(IMG))

    return CLASS[np.argmax(PRED)]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/prediction', methods=['GET', 'POST']) 
def prediction():
    FILE = request.files['file1']
    FILE.save('static/temp_file_'+hostname+'.jpg')
    PRED = pred(FILE)
    DATA = {
        'hostname': hostname,
        'pred': PRED
    }

    return render_template('predict.html', data = DATA)

if __name__ == '__main__':
    app.run()