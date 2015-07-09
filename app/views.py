# from flask.ext.login import (LoginManager, current_user, login_required,
#                             login_user, logout_user, UserMixin,
#                             confirm_login, fresh_login_required)
from flask import render_template, flash, redirect, request
from flask import session
from app import app
from .forms import LoginForm
import subprocess, os


# Makes switch statements possible
"""
Thanks to Brian Beck from :http://code.activestate.com/recipes/410692/ for this one!
"""
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

@app.route('/')
@app.route('/index')
def index():
    if 'logged_in' in session:
        user = {'firstName': app.config['USERS'][session['id']]['firstName'], 'id': session['id']}
    else:
        user = {'firstName': 'Unknown'}
    log = [
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'},
        {'user': 'root', 'post': 'Command: "Play Drake"'}
    ]
    return render_template("index.html",
                           title='Console',
                           user=user,
                           logs=log
                           )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userPIN = form.openid.data
        rememberMe = form.remember_me.data
        loginID = loginCheck(userPIN)
        print "User trying to log in with ID: %s" % (loginID)
        if loginID != None:
            session['logged_in'] = True
            session['id'] = loginID
            print 'Logged in successfully!'
            flash('Logged in successfully')
            print 'Username is %s' % (app.config['USERS'][loginID]['firstName'])
            return redirect('/')
        else:
            flash('PIN Incorrect!')
            return redirect('/login')
        
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in')
    session.pop('id')
    flash('Logged out successfully')
    return redirect('/')




@app.route('/commands', methods=['POST'])
def commands():
    command = request.form.get('command')
    user = request.form.get('user')

    if command == 'play':
        os.system('mpc play')
        return 'MPC player starting!'
    elif command == 'stop':
        os.system('mpc stop')
        return 'MPC player stopping!'
    elif command.split(' ', 1)[0] == 'volume':
        value = int(command.split(' ', 1)[1])
        if value <= 100:
            string = 'mpc volume %d' % (value)
            os.system(string)
            return "Changing volume to %s" % (value)
        else: 
            return "Volume out of bounds!"



    else:
        return "I don't know that one bud!"


    """for case in switch(command):
        if case('play'):
            os.system('mpc play')
            return "MPC player playing!"
            break
        if case('stop'):
            os.system('mpc stop')
            return "MPC player stopping!"
            break
        if case()

        if case():
            return "I know nothing"""

    # if command == "play":
    #     os.system("mpc play")
    print command
    return "Complete"




def loginCheck(pin):
    for x in xrange(0, len(app.config['USERS'])):
        if int(pin) == app.config['USERS'][x]['pin']:
            return x

