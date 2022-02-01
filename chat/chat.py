from flask import Blueprint, render_template, url_for, redirect

chat = Blueprint('chat', __name__, template_folder='templates', static_folder='static')

@chat.route('/')
def login_chat():
    return render_template('chat/index.html', title='Chat' )

@chat.route('/logout')
def logout():
    return redirect(url_for('index'))           # это функция index из run.py(app.route('/))
