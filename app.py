from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/example')
def example():
    return "This is an example page."

if __name__ == '__main__':
    app.run(debug=True)