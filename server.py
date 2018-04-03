from bottle import get, run, template, view

@get('/index')
def index():
    return "Welcome to CMPS 183!"

@get('/greet/<name>')
def greet(name):
    return template('greet_template', name=name)

@view('greet_template')
@get('/sayhi/<name>')
def greet(name):
    return dict(name=name)

run(reloader=True, host='localhost', port=8080)

