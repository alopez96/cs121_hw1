from bottle import get, run

@get('/index')
def index():
    return "Welcome to CMPS 183!"


run(host='localhost', port=8080)

