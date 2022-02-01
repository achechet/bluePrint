from flask import Flask, render_template
from admin.admin import admin
from chat.chat import chat
from dashboard.dashboard import dashboard
from documents.documents import documents

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(chat, url_prefix='/chat')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(documents, url_prefix='/documents')

@app.route('/')
def index():
    return render_template('index.html', title='Main page')

if __name__ == '__main__':
    app.run(debug=True)
    