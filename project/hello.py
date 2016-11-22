
# Running a web server

from flask import Flask
# import class definition

app = Flask(__name__)
# instance
# creates the web application


@app.route('/hello') # hello = URL
def root_page():
    response = """
    <html>
    <head>
    <title>Hello World</title>
    </head>
    <body>
    <h1>Hello World!</h1>
    </body>
    </html>
    """
    # HTML file
    return response

if __name__ == "__main__":
    app.run() # start Flask
