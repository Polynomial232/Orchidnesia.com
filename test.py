from classList import readFile

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

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


if __name__ == '__main__':
    app.run()