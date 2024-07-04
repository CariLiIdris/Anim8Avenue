from flask import Flask, render_template # type: ignore
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/hello/<string:name>/<int:age>')
def hello(name, age):
  return f'hello {name * age}'

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port=8000)