from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Recommendations Service Backend v1.1.0 running...'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
