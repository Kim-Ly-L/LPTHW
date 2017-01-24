from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session...
        # What should your code do in response?
        return redirect(url_for('/'))

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input... what should your code do?
            return render_template('missinginput.html')
            return redirect(url_for('/'))
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # what should your code do in response?
                return currentscene
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return redirect(url_for('/'))

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = 'q23er56z'

if __name__ == "__main__":
    app.run()
