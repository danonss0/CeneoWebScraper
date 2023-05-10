from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Łukasz Doniec!"

@app.route('/name/', defaluts={'name: None'})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"