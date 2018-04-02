from bottle import get, run, template

@get('/index')
def index():
    return "Welcome to CMPS 183!"


@get('/greet/<name>')
def greet(name):
    return template('greet_template', name=name)

run(host='localhost', port=8080)

