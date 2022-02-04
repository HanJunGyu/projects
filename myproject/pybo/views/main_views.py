from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
import os

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/upload')
def render_file():

    return render_template('upload.html')

# 파일 업로드 처리
@bp.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save("C:/projects/myproject/pybo/uploads/"+secure_filename(f.filename))
        return '전송완료'

@bp.route('/OS')
def script():
    with open("C:/projects/myproject/pybo/uploads/linux.txt", "r", encoding='utf-8') as file:
        linux = file.read()
    with open("C:/projects/myproject/pybo/uploads/windows.txt", "r", encoding='utf-8') as file:
        windows = file.read()
    return render_template('OS.html', linux=linux, windows=windows)
