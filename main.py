from flask import *

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['POST'])
def response_message():

    image = request.form['m']

    return json.dumps(
        {
            'status': 'OK',
            'filePath': "img/" + filename
        }
    )

if __name__ == '__main__':
    app.run(**app_options)
