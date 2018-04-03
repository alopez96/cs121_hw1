from bottle import get, route, run, template, view, static_file

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

# Let's add some code to serve jpg images from our static images directory.
@route('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

run(reloader=True, host='localhost', port=8080)

