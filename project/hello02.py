from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def root_page():
    response = render_template('hello.html', greetings="Saludos, Amigos")
    return response
    
    if __name__ == "__main__":
        app.run
