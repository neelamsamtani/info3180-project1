"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import datetime, os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask import jsonify, session
from flask_wtf import form
from forms import ProfileForm
from models import UserProfile
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    file_folder = "app/static/uploads"
    if request.method == 'POST':
        if ProfileForm().validate_on_submit():
            fname = request.form['fname']
            lname = request.form['lname']
            user = request.form['user']
            age = request.form['age']
            gen = request.form['gen']
            bio = request.form['bio']
            file = request.form['img']
            date = datetime.datetime.now().strftime("%m-%d-%Y")
            if file :
                filename = secure_filename(file.filename)
                file.save(os.path.join(file_folder, filename))
                img=filename = secure_filename(file.filename)
            userprofile = UserProfile(fname, lname, user, age, gen, bio, img, date)
            db.session.add(userprofile)
            db.session.commit()
        flash("Successfully created user.")
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    profiles = db.session.query(UserProfile).all()
    if request.method == "POST":
        proflist = []
        for prof in profiles:
            proflist.append({'id':prof.id, 'username':prof.user})
            return jsonify(profiles=proflist)
    else:
        return render_template('profiles.html', profiles=profiles)
    
@app.route('/profile/<id>', methods = ['GET','POST'])
def getprofile(id):
    user = UserProfile.query.filter_by(id=id)
    img = user.img
    if request.method == 'POST':
        return jsonify(
            id=user.id,
            userfname=user.fname,
            userlname=user.lname,
            username=user.user,
            usergen=user.gen,
            userage=user.age,
            userbio=user.bio,
            img=user.img,
            userdate=user.date)
    else:
        user = {'id':user.id,
        'imge':img,
        'username':user.username,
        'fname':user.userfname,
        'lname':user.userlname,
        'age':user.userage,
        'gender':user.usergender,
        'bio':user.userbio,
        'date':datetime.datetime.now().strftime("%m-%d-%Y")}
    return render_template('profilebase.html', prof=user)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
