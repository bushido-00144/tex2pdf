from flask import Flask, session, request, redirect, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'The secret key which ciphers the cookie'

import modules.createKey as createKey
import modules.Git as Git
import modules.utils as utils

@app.before_request
def before_request():
    if session.get('sessionid') is not None:
        return
    if request.path == '/login' or request.path == '/createuser':
        return
    if _is_static(request.path):
        return
    return redirect('/login')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if _is_account_valid():
            session['sessionid'] = utils.randomStr(16)
            return redirect(url_for('index'))
        else:
            return render_template('createuser.html', errmessage='Cant find user')
    if request.method == 'GET':
        challenge=utils.randomStr(16)
        return render_template('login.html')

def _is_account_valid():
    if request.form.get('username') is not None:
        username = request.form.get('username')
        if createKey.getPubKey(username) != "ERROR":
            return True
    return False

def _is_static(request_path):
    top_path = request_path.split('/')[1]
    if top_path == 'static':
        return True
    return False

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('sessionid', None)
    return redirect(url_for('login'))

@app.route('/createuser', methods=['GET', 'POST'])
def createUser():
    if request.method == 'POST':
        username = request.form.get('username')
        pub_key = createKey.createKey(username)
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('createuser.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    event_data = request.json
    repository_url = event_data['repository']['git_ssh_url']
    Git.GitPull(repository_url)
    return redirect(url_for('login'))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
