from flask import Blueprint, render_template, url_for, redirect

dashboard = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard.route('/')
def login_dashboard():
    return render_template('dashboard/index.html', title='Dashboard' )

@dashboard.route('/logout')
def logout():
    return redirect(url_for('index'))           # это функция index из run.py(app.route('/))
