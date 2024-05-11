from process_detect import processDetect
from flask import Flask, request 
import os
import uuid
from werkzeug.utils import secure_filename


app=Flask(__name__)

# ROUTING
@app.route('/')
def index():
    return '<h1>Hello world</h1>'

@app.route('/detected-species', methods=['POST'])
def Detected_pecies():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        UPLOAD_FOLDER = r'E:\KERJA\spudniklab\InsecstopProjeck\upload'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        filename = secure_filename(file.filename)  # Secure filename
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]  # Generate unique filename with original file extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        file_info = {'filename': unique_filename, 'filetype': file.content_type}
        result = processDetect(unique_filename)
        print(result)
        return result  # Pastikan hasilnya merupakan JSON
    
    

if __name__ == "__main__":
    app.run()