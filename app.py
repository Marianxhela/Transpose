import uuid
import os
from flask import Flask, render_template, request, send_file
from flask_dropzone import Dropzone
from controller.transpose import add_optimised_cash_flow
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
upload_folders = os.path.join(basedir, "uploads")
Path(upload_folders).mkdir(parents=True, exist_ok=True)
app = Flask(__name__)
dropzone = Dropzone(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], f"{uuid.uuid4()}_{f.filename}")
        f.save(file_path)
        add_optimised_cash_flow(file_path)
        return send_file(file_path, as_attachment=True)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
