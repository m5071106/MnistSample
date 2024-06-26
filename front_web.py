from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from werkzeug.utils import secure_filename
import os
import socket
import urllib.request

import number_recog

app = Flask(__name__)

UPLOAD_FOLDER = './source'
# extensions.txtから拡張子を取得
with open('extensions.txt', 'r') as file:
    extensions = file.read()
    extensions = extensions.split('\n')
    ALLOWED_EXTENSIONS = set(extensions)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 解析結果一覧用URLを取得
with open('filelisturl.txt', 'r') as file:
    filelist_url = file.read()
    filelist_url = filelist_url.split('\n')[0]

# ファイルの拡張子がextensionsに含まれているか確認
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# localhost以外のIPアドレスを取得
def get_ip_addresses():
    ip_addresses = []
    host_name = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(host_name)[-1]
    ip_addresses = [ip for ip in ip_addresses if ip != '127.0.0.1']
    return ip_addresses

# ファイルアップロード処理
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # ファイルがない場合
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        # ファイルがある場合
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 変換処理
            resultfilename, result = number_recog.predict_number()

            # 変換後のWebページを表示
            with open('front_web_after.html', 'r') as file:
                front_web_after_content = file.read()
            front_web_after_content = front_web_after_content.replace('$FILENAME$', resultfilename)
            front_web_after_content = front_web_after_content.replace('$RESULT$', str(result))
            ip_addresses = get_ip_addresses()
            front_web_after_content = front_web_after_content.replace('$IPADDRESS$', ip_addresses[0])
            front_web_after_content = front_web_after_content.replace('$FILELISTURL$', filelist_url)
            return front_web_after_content

    # 初期Webページを表示
    with open('front_web.html', 'r') as file:
        front_web_content = file.read()
    with open('front_web.js', 'r') as file:
        jscript = file.read()
    front_web_content = front_web_content.replace('$JS$', jscript)
    return front_web_content

if __name__ == '__main__':
    # app.run()
    app.run(debug=False, host='0.0.0.0', port=5001)