from flask import *

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/m', methods=['POST'])
def response_message():
    m = request.form['m']

    return json.dumps(
        {
            'message': m,
        }
    )

if __name__ == '__main__':
    app.run(**app_options)
