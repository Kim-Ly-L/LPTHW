from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')  # / = routing
def hello_world():
    greeting = "%s, %s!" % (request.args.get('greet'), request.args.get('name'))
    return render_template('index.html', greet=greeting)

if __name__ == "__main__":
    app.run()
