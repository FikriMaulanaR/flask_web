from ast import Eq, Pass
from crypt import methods
import os
from tokenize import String
from wsgiref.validate import validator
import psycopg2
import psycopg2.extras
import re
from models import conn, cur, index_posts
from datetime import datetime, timedelta, date
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, EmailField, ValidationError, HiddenField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from app import app, ckeditor
from flask_ckeditor import CKEditorField
bp_backend = Blueprint('backend',__name__,template_folder='templates')

@bp_backend.route('/')
@bp_backend.route('/home')
def index():
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('index.html', posts=index_posts, users=users[0], title='Home', menu='Menu')
    return redirect(url_for('backend.login'))

@bp_backend.route('/sejarah')
def backend_sejarah():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=1;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('sejarah.html', posts=posts, users=users[0], menu='Profil', title='Sejarah')
    return redirect(url_for('backend.login'))

@bp_backend.route('/visi-misi')
def backend_visimisi():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=2;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('visimisi.html', posts=posts, users=users[0], menu='Profil', title='Visi & Misi')
    return redirect(url_for('backend.login'))

@bp_backend.route('/tugas-fungsi')
def backend_tugasfungsi():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=3;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('tugasfungsi.html', posts=posts, users=users[0], menu='Profil', title='Tugas & Fungsi')
    return redirect(url_for('backend.login'))

@bp_backend.route('/kontak')
def backend_kontak():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=4;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('kontak.html', posts=posts, users=users[0], menu='Profil', title='Kontak')
    return redirect(url_for('backend.login'))

@bp_backend.route('/gempa')
def backend_gempa():
    if 'loggedin' in session:
        s = "SELECT tbl_post.post_id, tbl_post.post_title, tbl_post.post_type, tbl_category.category_title, tbl_post.post_create, tbl_post.post_admin, tbl_post.post_publish FROM tbl_post INNER JOIN tbl_category ON tbl_post.post_category=tbl_category.category_id"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('gempa.html', posts=posts, users=users[0], menu='Informasi', title='Gempa')
    return redirect(url_for('backend.login'))

@bp_backend.route('/cuaca')
def backend_cuaca():
    if 'loggedin' in session:
        s = "SELECT tbl_post.post_id, tbl_post.post_title, tbl_post.post_type, tbl_category.category_title, tbl_post.post_create, tbl_post.post_admin, tbl_post.post_publish FROM tbl_post INNER JOIN tbl_category ON tbl_post.post_category=tbl_category.category_id"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('cuaca.html', posts=posts, users=users[0], menu='Informasi', title='Cuaca')
    return redirect(url_for('backend.login'))

@bp_backend.route('/iklim')
def backend_iklim():
    if 'loggedin' in session:
        s = "SELECT tbl_post.post_id, tbl_post.post_title, tbl_post.post_type, tbl_category.category_title, tbl_post.post_create, tbl_post.post_admin, tbl_post.post_publish FROM tbl_post INNER JOIN tbl_category ON tbl_post.post_category=tbl_category.category_id"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('iklim.html', posts=posts, users=users[0], menu='Informasi', title='Iklim')
    return redirect(url_for('backend.login'))

@bp_backend.route('/petir')
def backend_petir():
    if 'loggedin' in session:
        s = "SELECT tbl_post.post_id, tbl_post.post_title, tbl_post.post_type, tbl_category.category_title, tbl_post.post_create, tbl_post.post_admin, tbl_post.post_publish FROM tbl_post INNER JOIN tbl_category ON tbl_post.post_category=tbl_category.category_id"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('petir.html', posts=posts, users=users[0], menu='Informasi', title='Petir')
    return redirect(url_for('backend.login'))

@bp_backend.route('/satelit')
def backend_satelit():
    if 'loggedin' in session:
        s = "SELECT tbl_post.post_id, tbl_post.post_title, tbl_post.post_type, tbl_category.category_title, tbl_post.post_create, tbl_post.post_admin, tbl_post.post_publish FROM tbl_post INNER JOIN tbl_category ON tbl_post.post_category=tbl_category.category_id"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('satelit.html', posts=posts, users=users[0], menu='Informasi', title='Satelit')
    return redirect(url_for('backend.login'))

@bp_backend.route('/berita')
def backend_berita():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=5;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('berita.html', posts=posts, users=users[0], menu='Menu', title='Berita')
    return redirect(url_for('backend.login'))

@bp_backend.route('/artikel')
def backend_artikel():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=6;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('artikel.html', posts=posts, users=users[0], menu='Menu', title='Artikel')
    return redirect(url_for('backend.login'))

@bp_backend.route('/buletin')
def backend_buletin():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=7;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('buletin.html', posts=posts, users=users[0], menu='Menu', title='Buletin')
    return redirect(url_for('backend.login'))

@bp_backend.route('/infografis')
def backend_infografis():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=8;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('infografis.html', posts=posts, users=users[0], menu='Menu', title='Inforgrafis')
    return redirect(url_for('backend.login'))

@bp_backend.route('/videografis')
def backend_videografis():
    if 'loggedin' in session:
        s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=9;"
        cur.execute(s)
        posts = cur.fetchall()
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        return render_template('videografis.html', posts=posts, users=users[0], menu='Menu', title='Videografis')
    return redirect(url_for('backend.login'))

@bp_backend.route('/data-1')
def backend_data():
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        data = [
            ("30-08-2022", 1598),
            ("31-08-2022", 1428),
            ("01-09-2022", 1998),
            ("02-09-2022", 598),
            ("03-09-2022", 898),
            ("04-09-2022", 798),
            ("05-09-2022", 1198),
            ("06-09-2022", 1298),
            ("07-09-2022", 498),
            ("08-09-2022", 1098),
        ]
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("chartjs.html", labels=labels, users=users[0], menu='Data 1', values=values, title='ChartJS')

@bp_backend.route('/data-2')
def backend_data2():
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        data_datetime = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        data_jkt = [26.1,26.4,27.0,27.2,26.7,26.4,26.7,27.0,27.2,27.0,26.4,26.7,]
        data_ptk = [26.9,27.9,28.2,28.1,28.0,27.8,27.5,27.8,28.3,27.7,27.3,27.2]
        data_dps = [24.1,24.2,24.0,24.8,24.1,23.5,22.5,22.9,23.0,23.7,23.5,23.5]
        data_sby = [26.8,26.8,27.0,27.3,27.3,26.7,26.2,26.5,27.2,28.2,28.3,27.3]
        data_mdn = [25.6,26.1,26.7,27.2,27.3,27.1,27.0,26.9,26.6,26.1,26.0,25.8]
        data_jyp = [27.1,26.9,27.1,27.3,27.2,26.9,26.4,26.6,26.9,27.2,27.3,27.0]
        labels = [row for row in data_datetime]
        values_jkt = [row for row in data_jkt]
        values_ptk = [row for row in data_ptk]
        values_dps = [row for row in data_dps]
        values_sby = [row for row in data_sby]
        values_mdn = [row for row in data_mdn]
        values_jyp = [row for row in data_jyp]

        return render_template("chartjs2.html", labels=labels, sby=values_sby, mdn=values_mdn, jyp=values_jyp, users=users[0], menu='Data 2', jkt=values_jkt, ptk=values_ptk, dps=values_dps, title='HighChartJS')

@bp_backend.route('/profil/<id>')
def backend_profil_user(id):
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        user = cur.fetchone()
        cur.execute("SELECT * FROM tbl_user WHERE user_id = %s;", (id,))
        users = cur.fetchall()
        print(users[0])
        return render_template('profil_user.html', user_name=user_name, user=user,users=users[0], menu='Users', title='Profil')

@bp_backend.route('/detail-post/<slug>')
def backend_detail_post(slug):
    if 'loggedin' in session:
        cur.execute('SELECT * FROM tbl_post WHERE post_slug = %s;', (slug,))
        posts = cur.fetchall()
        print(posts)
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users)
        return render_template('detail_post.html', posts=posts[0], menu='Posts', users=users[0], title='Details')

@bp_backend.route('/manage-users')
def backend_manage_users():
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        user = cur.fetchall()
        print(user[0])
        if user_name == 'admin' :
            s = 'SELECT * FROM tbl_user;'
            cur.execute(s)
            users = cur.fetchall()
            print(users[0])
            return render_template('manage_users.html', users=users, user=user[0], menu='Users', title='Manage Users')
        else:
            flash("You don't have access to see manage users", "danger")
            return redirect(url_for('index'))

@bp_backend.route('/manage-users/update/<id>', methods=['GET', 'POST'])
def backend_update_user(id):
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute('SELECT * FROM tbl_user WHERE user_id = %s;', (id,))
        users = cur.fetchall()
        print(user_name)
        form = updateUserForm()
        if user_name == 'admin':
            if request.method == 'POST' and form.validate_on_submit():
                if form.user_photo.data is not None:
                    user_photo = form.user_photo.data
                    usr_img_filename = secure_filename(user_photo.filename)
                    user_photo_name = usr_img_filename
                    saver = form.user_photo.data
                    user_photo2 = user_photo_name
                    print(user_photo)

                    cur.execute("""
                        UPDATE tbl_user 
                        SET user_name = %s, 
                            user_email = %s, 
                            user_update = now(), 
                            user_fullname = %s, 
                            user_photo = %s, 
                            user_active = %s, 
                            user_group = %s 
                        WHERE user_id = %s;
                        """, (form.user_name.data, form.user_email.data, form.user_fullname.data, user_photo2, form.user_active.data, form.user_group.data, id))
                    saver.save(os.path.join(app.config['UPLOAD_FOLDER'], user_photo_name))
                    flash('User Updated Successfully!', 'success')
                    conn.commit()
                    return redirect(url_for('backend.backend_manage_users'))
                else:
                    cur.execute("""
                        UPDATE tbl_user 
                        SET user_name = %s, 
                            user_email = %s,                              
                            user_fullname = %s,
                            user_active = %s,
                            user_update = now(), 
                            user_group = %s 
                        WHERE user_id = %s;
                        """, (form.user_name.data, form.user_email.data, form.user_fullname.data, form.user_active.data, form.user_group.data, id))
                    flash('User Updated Successfully!!', 'success')
                    conn.commit()
                    return redirect(url_for('backend.backend_manage_users'))
            else:
                return render_template('update_user.html', form=form, users=users[0], menu='Users', menu1='ManageUsers', title='Update User')
        else:
            if request.method == 'POST' and form.validate_on_submit():
                if form.user_photo.data is not None:
                    user_photo = form.user_photo.data
                    usr_img_filename = secure_filename(user_photo.filename)
                    user_photo_name = usr_img_filename
                    saver = form.user_photo.data
                    user_photo = user_photo_name
                    print(user_photo)
                    try:
                        cur.execute("""
                            UPDATE tbl_user 
                            SET user_name = %s, 
                                user_email = %s, 
                                user_update = now(), 
                                user_fullname = %s, 
                                user_photo = %s
                            WHERE user_id = %s;
                            """, (form.user_name.data, form.user_email.data, form.user_fullname.data, user_photo_name, id))
                        saver.save(os.path.join(app.config['UPLOAD_FOLDER'], user_photo_name))
                        flash('User Updated Successfully!', 'success')
                        conn.commit()
                        return redirect(url_for('index'))
                    except:
                        flash("Error! There was an error!", "warning")
                else:
                    try:
                        cur.execute("""
                            UPDATE tbl_user 
                            SET user_name = %s, 
                                user_email = %s,                              
                                user_fullname = %s,                                
                                user_update = now() 
                            WHERE user_id = %s;
                            """, (form.user_name.data, form.user_email.data, form.user_fullname.data, id))
                        flash('User Updated Successfully!!', 'success')
                        conn.commit()
                        return redirect(url_for('index'))
                    except:
                        flash("Error! There was an error!", "warning")
            else:
                return render_template('update_user.html', form=form, users=users[0], menu='Users', menu1='ManageUsers', title='Update User')

@bp_backend.route('/manage-users/add-new-user', methods=['GET', 'POST'])
def backend_add_user():
    if 'loggedin' in session:
        user_name = None
        form = addUserForm()
        if request.method == 'POST' and form.validate_on_submit():
            users = cur.execute("SELECT * FROM tbl_user WHERE user_name = %s", (form.user_name.data,))
            if users is None:
                if form.user_photo.data is not None:
                    user_photo = form.user_photo.data
                    usr_img_filename = secure_filename(user_photo.filename)
                    user_photo_name = usr_img_filename
                    saver = form.user_photo.data
                    user_photo = user_photo_name
                    print(user_photo)
                    try:
                        cur.execute("INSERT INTO tbl_user (user_name, user_pass, user_email, user_fullname, user_photo, user_active, user_group) VALUES (%s,%s,%s,%s,%s,%s,%s)", (form.user_name.data, form.user_pass.data, form.user_email.data, form.user_fullname.data, user_photo_name, form.user_active.data, form.user_group.data))
                        saver.save(os.path.join(app.config['UPLOAD_FOLDER'], user_photo_name))
                        flash('User Added Successfully!', 'success')
                        conn.commit()
                        return redirect(url_for('backend.backend_manage_users'))
                    except:
                        flash('Error! There was an error!', 'warning')
                else:
                    try:
                        cur.execute("INSERT INTO tbl_user (user_name, user_pass, user_email, user_fullname, user_active, user_group) VALUES (%s,%s,%s,%s,%s,%s)", (form.user_name.data, form.user_pass.data, form.user_email.data, form.user_fullname.data, form.user_active.data, form.user_group.data,))
                        flash('User Added Successfully!!', 'success')
                        conn.commit()
                        return redirect(url_for('backend.backend_manage_users'))
                    except:
                        flash('Errors! There was an error!', 'warning')
            else:
                flash('Username already Exists!', 'warning')
        return render_template('register_user.html', form=form, user_name=user_name, menu='Users', menu1='ManageUsers', title='Add New User')
    return render_template('register_user.html', form=form, user_name=user_name, menu='Users', menu1='ManageUsers', title='Add New User')

@bp_backend.route('/manage-users/delete-user/<string:id>', methods=['GET', 'POST'])
def backend_delete_user(id):
    if 'loggedin' in session:
        cur.execute('DELETE FROM tbl_user WHERE user_id = {0};'.format(id))
        conn.commit()
        flash('User Removed Successfully', 'success')
        return redirect(url_for('backend.backend_manage_users'))

@bp_backend.route('/update-post/<id>', methods=['GET', 'POST'])
def backend_edit_post(id):
    cur.execute('SELECT * FROM tbl_post WHERE post_id = %s;', (id,))
    posts = cur.fetchone()
    form = updatePostForm(obj=posts)
    form.post_body.data = posts[8]
    user_name = session['user_name']
    cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
    users = cur.fetchall()
    if 'loggedin' in session:
        print(posts[8])
        if request.method == 'POST' and form.validate_on_submit():
            posts[1] = form.post_title.data
            posts[2] = form.post_slug.data
            posts[3] = form.post_type.data
            posts[4] = form.post_category.data
            posts[7] = form.post_intro.data
            post_body = request.form['post_body']
            posts[10] = form.post_admin.data
            posts[11] = form.post_publish.data
            if form.post_image.data:
                post_image = form.post_image.data
                img_filename = secure_filename(post_image.filename)
                post_image_name = img_filename
                saver = form.post_image.data
                post_image2 = post_image_name
                print(post_image)
                try:
                    cur.execute("""
                        UPDATE tbl_post
                        SET post_title = %s,
                            post_slug = %s,
                            post_type = %s,
                            post_category = %s,
                            post_intro = %s,
                            post_body = %s,
                            post_image = %s,
                            post_admin = %s,
                            post_publish = %s,
                            post_update = now()
                        WHERE post_id = %s;
                    """, (form.post_title.data, form.post_slug.data, form.post_type.data, form.post_category.data, form.post_intro.data, post_body, post_image2, form.post_admin.data, form.post_publish.data, id))
                    saver.save(os.path.join(app.config['UPLOAD_FOLDER'], post_image_name))
                    flash('Post Updated Successfully', 'success')
                    conn.commit()
                    return redirect(url_for('index'))
                except:
                    flash('Error! There was an error!', 'warning')
                    return render_template('update.html', posts=posts, form=form, users=users[0], menu='Posts', title='Update Post')
            else:
                try:
                    cur.execute("""
                        UPDATE tbl_post
                        SET post_title = %s,
                            post_slug = %s,
                            post_type = %s,
                            post_category = %s,
                            post_intro = %s,
                            post_body = %s,
                            post_admin = %s,
                            post_publish = %s,
                            post_update = now()
                        WHERE post_id = %s;
                    """, (form.post_title.data, form.post_slug.data, form.post_type.data, form.post_category.data, form.post_intro.data, post_body, form.post_admin.data, form.post_publish.data, id))
                    flash('Post Updated Successfully', 'success')
                    conn.commit()
                    return redirect(url_for('index'))
                except:
                    flash('Error! There was an error!', 'warning')
                    return render_template('update.html', posts=posts, form=form, users=users[0], menu='Posts', title='Update Post')
        return render_template('update.html', posts=posts, form=form, users=users[0], menu='Posts', title='Update Post')
    return render_template('update.html', posts=posts, form=form, users=users[0], menu='Posts', title='Update Post')
    

@bp_backend.route('/delete-post/<string:id>', methods=['GET', 'POST'])
def backend_delete_post(id):
    if 'loggedin' in session:
        cur.execute('DELETE FROM tbl_post WHERE post_id = {0};'.format(id))
        conn.commit()
        flash('Post Removed Successfully', 'success')
        return redirect(url_for('index'))

@bp_backend.route('/add-post', methods=['GET', 'POST'])
def backend_add_post():
    form = addPostForm()
    if 'loggedin' in session:
        user_name = session['user_name']
        cur.execute("SELECT * FROM tbl_user WHERE user_name = %s;", (user_name,))
        users = cur.fetchall()
        print(users[0])
        if request.method == 'POST' and form.validate_on_submit():
            post_title = request.form['post_title']
            post_slug = request.form['post_slug']
            post_type = request.form['post_type']
            post_category = request.form['post_category']
            post_intro = request.form['post_intro']
            post_body = request.form['post_body']
            post_admin = request.form['post_admin']
            post_publish = request.form['post_publish']
        
            if request.files['post_image']:
                post_image = request.files['post_image']
                img_filename = secure_filename(post_image.filename)
                post_image_name = img_filename
                saver = request.files['post_image']
                post_image = post_image_name
                print(post_image)
                try:
                    cur.execute("INSERT INTO tbl_post (post_title, post_slug, post_type, post_category, post_intro, post_body, post_image, post_admin, post_publish) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (post_title, post_slug, post_type, post_category, post_intro, post_body, post_image, post_admin, post_publish))
                    saver.save(os.path.join(app.config['UPLOAD_FOLDER'], post_image_name))
                    flash('Post Added Successfully', 'success')
                    conn.commit()
                    return redirect(url_for('index'))
                except:
                    flash('Error! There was an error a!', 'warning')
            else:
                try:
                    cur.execute("INSERT INTO tbl_post (post_title, post_slug, post_type, post_category, post_intro, post_body, post_admin, post_publish) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (post_title, post_slug, post_type, post_category, post_intro, post_body, post_admin, post_publish))
                    flash('Post Added Successfully', 'success')
                    conn.commit()
                    return redirect(url_for('index'))
                except:
                    flash('Error! There was an error!', 'warning')
        return render_template('add_post.html', form=form, users=users[0], menu='Posts', title='Add New Post')
    return render_template('add_post.html', form=form, menu='Posts', users=users[0], title='Add New Post')


@bp_backend.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        # Check username and password POST request exists
        if request.method == 'POST' and 'user_name' in request.form and 'user_pass' in request.form:
            user_name = request.form['user_name']
            user_pass = request.form['user_pass']
            print(user_pass)

            # Check user exists
            cur.execute('SELECT * FROM tbl_user WHERE user_name = %s;', (user_name,))
            # Fetch one record
            user = cur.fetchone()

            if user:
                password_rs = user['user_pass']
                print(password_rs)
                cur.execute('SELECT * FROM tbl_user WHERE user_pass = %s;', (user_pass,))

                userpw = cur.fetchone()
                if userpw:
                    session['loggedin'] = True
                    session['user_id'] = user['user_id']
                    session['user_name'] = user['user_name']
                    flash(f"Login Succesfull!! hello {form.user_name.data}!", "success")
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect Password', 'warning')
            else:
                flash("User Doesn't exists", 'warning')
        return render_template('login.html', form=form, title='Login')

    return render_template('login.html', form=form, title='Login')

@bp_backend.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash("You Have Been Logged Out!", "success")
    return redirect(url_for('backend.login'))

class loginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    user_pass = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LOG IN')

TYPE_CHOICES = [('1', 'Static'), ('2', 'Dynamic')]
PUBLISH_CHOICES = [('1', 'Publish'), ('2', 'Unpublish')]

class updatePostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired(), Length(min=5, max=100)])
    post_slug = StringField('Slug', validators=[DataRequired()])
    post_type = SelectField('Type', validators=[DataRequired()], choices=TYPE_CHOICES)
    post_category = IntegerField('Category', validators=[DataRequired(), NumberRange(min=1, max=9)])
    post_intro = StringField('Intro', validators=[DataRequired()])
    post_body = CKEditorField('Body', validators=[DataRequired()])
    post_image = FileField(u'Image File', validators=[Optional(strip_whitespace=True), FileAllowed(['jpg', 'jpeg', 'png'], 'File extensions format must be .jpg, .jpeg, and .png!')])
    post_admin = StringField('Admin', validators=[DataRequired()])
    post_publish = SelectField('Publish', validators=[DataRequired()], choices=PUBLISH_CHOICES)
    #post_update = DateTimeField('Post Updated', format="%Y-%m-%d", default=datetime.today, validators=[DataRequired()])
    submit = SubmitField('Submit')

class addPostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired(), Length(min=5, max=100)])
    post_slug = StringField('Slug', validators=[DataRequired()])
    post_type = SelectField('Type', validators=[DataRequired()], choices=TYPE_CHOICES)
    post_category = IntegerField('Category', validators=[DataRequired(), NumberRange(min=1, max=9)])
    post_intro = StringField('Intro', validators=[DataRequired()])
    post_body = CKEditorField('Body', validators=[DataRequired()])
    post_image = FileField(u'Image File', validators=[Optional(strip_whitespace=True), FileAllowed(['jpg', 'jpeg', 'png'], 'File extensions format must be .jpg, .jpeg, and .png!')])
    post_admin = StringField('Admin', validators=[DataRequired()])
    post_publish = SelectField('Publish', validators=[DataRequired()], choices=PUBLISH_CHOICES)
    submit = SubmitField('Submit')

ACTIVE_CHOICES = [('1', 'Active'), ('2', 'Inactive')]
GROUP_CHOICES = [('1', 'Admin'), ('2', 'Operator')]

class addUserForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    user_pass = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Field must be equal to Confirm Password')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('user_pass', message='Field must be equal to Password')])
    user_email = EmailField('Email', validators=[DataRequired(), Email()])
    user_fullname = StringField('Full Name', validators=[DataRequired()])
    user_photo = FileField(u'User Photo', validators=[Optional(strip_whitespace=True), FileAllowed(['jpg', 'jpeg', 'png'], 'File extensions format must be .jpg, .jpeg, and .png!')])
    user_active = SelectField('User Active', validators=[DataRequired()], choices=ACTIVE_CHOICES, default='1')
    user_group = SelectField('User Group', validators=[DataRequired()], choices=GROUP_CHOICES, default='2')
    submit = SubmitField('SUBMIT')

class updateUserForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    user_email = EmailField('Email', validators=[DataRequired(), Email()])
    user_fullname = StringField('Full Name', validators=[DataRequired()])
    user_photo = FileField(u'User Photo', validators=[Optional(strip_whitespace=True), FileAllowed(['jpg', 'jpeg', 'png'], 'File extensions format must be .jpg, .jpeg, and .png!')])
    user_active = SelectField('User Active', validators=[DataRequired()], choices=ACTIVE_CHOICES, default='1')
    user_group = SelectField('User Group', validators=[DataRequired()], choices=GROUP_CHOICES, default='2')
    submit = SubmitField('SUBMIT')

class changeUserPassword(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    user_pass = PasswordField('New Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('user_pass', message='Field must be equal to Confirm Password')])
    submit = SubmitField('Change Password')