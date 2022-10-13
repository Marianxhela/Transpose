import uuid
import os
from flask import Flask, render_template, request, send_file, session
from flask_dropzone import Dropzone
from controller.transpose import add_optimised_cash_flow
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
upload_folders = os.path.join(basedir, "uploads")
Path(upload_folders).mkdir(parents=True, exist_ok=True)
app = Flask(__name__)
dropzone = Dropzone(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='.xlsx',
    DROPZONE_REDIRECT_VIEW='completed'  # set redirect view
)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], f"{uuid.uuid4()}_{f.filename}")
        f.save(file_path)
        add_optimised_cash_flow(file_path)
        session['file_path'] = file_path
        session['filename'] = f.filename
        return send_file(file_path, as_attachment=True)
    return render_template("index.html")


@app.route('/completed')
def completed():
    file_path = session.get('file_path')
    filename = session.get('filename')
    if not file_path or not filename:
        return '<h1>Please upload Excel file</h1>'

    return send_file(file_path, as_attachment=True, download_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
