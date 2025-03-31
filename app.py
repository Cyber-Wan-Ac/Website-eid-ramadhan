from flask import Flask, render_template_string, redirect, url_for, send_file

app = Flask(__name__)

thr_link = "https://contoh-link-thr.com"  # Ganti dengan link THR kamu

html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Selamat Hari Raya Idul Fitri</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-image: url('/baiturrahman.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: white;
        }
        h1 {
            color: #FFD700;
            text-shadow: 2px 2px 5px #000;
            animation: fadeIn 3s;
            font-size: 36px;
        }
        p {
            font-size: 20px;
            text-shadow: 1px 1px 2px #000;
            margin-top: 20px;
            animation: fadeIn 5s;
            color: #FFFFE0;
        }
        button {
            padding: 15px 30px;
            background-color: #FF4500;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 10px;
            margin-top: 20px;
            transition: transform 0.3s, background-color 0.3s;
            animation: bounce 2s infinite;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        button:hover {
            background-color: #FF6347;
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <audio autoplay loop>
        <source src="/takbir.mp3" type="audio/mpeg">
    </audio>
    <h1>Selamat Hari Raya Idul Fitri 1446 H</h1>
    <p>Semoga semua amal ibadah kita diterima dan diberkahi oleh Allah SWT.<br>
    <strong>Taqabbalallahu minna wa minkum. Maaf lahir dan batin.</strong></p>
    <form action="/thr" method="POST">
        <button type="submit">Klik di sini untuk Ambil THR</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(html_code)

@app.route('/baiturrahman.jpg')
def baiturrahman():
    return send_file('baiturrahman.jpg')

@app.route('/takbir.mp3')
def takbir():
    return send_file('takbir.mp3')

@app.route('/thr', methods=['POST'])
def thr():
    return redirect(thr_link)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
