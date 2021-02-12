from flask import Flask, render_template


app = Flask(__name__)

#loading the model
#model = load_model('mnist_model.h5')

@app.route('/')
def index():
    return "<h1>Hello, world!</h1>"


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

