import os
import psycopg2
import psycopg2.extras
import re
from models import conn, cur
from flask import Flask
from flask import render_template, redirect, url_for, flash, request, session
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
import datetime, time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'websorong2022!!'
ckeditor = CKEditor(app)
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rahasia@localhost:6543/dbsorong'

@app.route('/')
@app.route('/home')
def index():
    if 'loggedin' in session:
        user_name = session['user_name']
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id;"
        cur.execute(s)
        posts = cur.fetchall()
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        return render_template('index.html', posts=posts, user_name=user_name, users=users[0], title='Home', menu='Menu')
    return redirect(url_for('backend.login'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title='Page Not Found'), 404

if __name__ == "__main__":
    app.run(debug=True)
from backend import bp_backend
app.register_blueprint(bp_backend)