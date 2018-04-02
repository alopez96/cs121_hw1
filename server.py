from bottle import Bottle, run

app = Bottle()

@app.route('/index')
def index():
    return "Welcome to CMPS 183!"

run(app, host='localhost', port=8080)

