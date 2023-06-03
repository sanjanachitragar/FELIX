from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    file.save(file.filename)
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)


@app.route('/')
def view_contents():
    server_path = 'c:\\Users\\Shreyas\\Desktop\\server'
    contents = os.listdir(server_path)
    
    #return render_template('index.html', contents=contents)

if __name__ == '__main__':
    app.run()

