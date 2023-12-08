from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Test App'

@app.route('/process', methods=['POST'])
def index():
    ## Get the data from body of request
    data = request.get_json()
    print(data)
    return "Success"

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
