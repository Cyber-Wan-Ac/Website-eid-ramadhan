from flask import Flask, render_template_string, send_file
import os

app = Flask(__name__)

# HTML Code
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Selamat Hari Raya Idul Fitri</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url('/baiturrahman.jpg');
            background-size: cover;
            color: white;
            text-align: center;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Selamat Hari Raya Idul Fitri</h1>
    <p>Mohon Maaf Lahir dan Batin</p>
    <audio autoplay loop>
        <source src="/takbir.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <button onclick="location.href='/thr'">Klik Di Sini untuk Ambil THR</button>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_code)

@app.route('/baiturrahman.jpg')
def baiturrahman():
    return send_file('baiturrahman.jpg')

@app.route('/takbir.mp3')
def takbir():
    return send_file('takbir.mp3')

@app.route('/thr')
def thr():
    return "<h1>Selamat! THR Kamu Sudah Tersedia. Klik <a href='https://linkthrmu.com'>di sini</a> untuk mengambilnya.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
