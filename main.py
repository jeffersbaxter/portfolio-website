from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from links import links

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html', links=links)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
