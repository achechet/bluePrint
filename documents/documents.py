from flask import Blueprint, render_template, url_for, redirect

documents = Blueprint('documents', __name__, template_folder='templates', static_folder='static')

@documents.route('/')
def login_documents():
    return render_template('documents/index.html', title='Documents' )

@documents.route('/logout')
def logout():
    return redirect(url_for('index'))           # это функция index из run.py(app.route('/))
