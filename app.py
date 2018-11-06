from datetime import timedelta
from flask import Flask, render_template, request, redirect, session
from content.content import content
from content.registration import Registration
from database.db import db

from api.api import API

app = Flask(__name__)
app.secret_key = b')\x95\xda\x1e\xd8)bo\x94R\xb9_\x04\x8c\xdd&'
app.register_blueprint(API)
app.register_blueprint(content)
app.register_blueprint(Registration)
app.permanent_session_lifetime = timedelta(minutes=3)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://andrij:a@localhost:5432/andrij'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@content.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
