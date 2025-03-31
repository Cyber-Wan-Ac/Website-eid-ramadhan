from flask import Flask, send_file, render_template_string

app = Flask(__name__)

html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test Suara</title>
</head>
<body style="text-align: center; padding-top: 50px;">
    <h1>Uji Coba Suara Takbir</h1>
    <audio autoplay loop>
        <source src="/takbir.mp3" type="audio/mpeg">
        Browser kamu tidak mendukung audio.
    </audio>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_code)

@app.route('/takbir.mp3')
def takbir():
    return send_file('takbir.mp3', mimetype='audio/mpeg')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
