from flask import *

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/m', methods=['POST'])
def response_message():
    m = request.form['m']



    return json.dumps({
        'message': m,
    })

    return json.dumps({
        'message': "Sorry I don't understand"
    })

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(**app_options)
