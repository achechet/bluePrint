from flask import Blueprint, render_template, url_for, redirect

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

@admin.route('/')
def login_admin():
    return render_template('admin/index.html', title='Administrator' )

@admin.route('/logout')
def logout():
    return redirect(url_for('index'))           # это функция index из run.py(app.route('/))
