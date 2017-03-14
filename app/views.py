"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask import jsonify, session
from flask_wtf import form
from forms import ProfileForm
from models import UserProfile



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
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            fname = request.form['fname']
            lname = request.form['lname']
            user = request.form['user']
            age = request.form['age']
            gen = request.form['gen']
            bio = request.form['bio']
            img = request.form['img']
            date = datetime.datetime.now()
            #newprofile = (fname, lname, user, age, gen, bio, img, date)
            #db.session.add(newprofile)
            #db.session.commit()
        return redirect(url_for('profile.html'))
    return render_template('profile.html')

@app.route('/profiles')
def profiles():
    return render_template('profiles.html')
    
@app.route('/profile/<userid>')
def getprofile():
    return render_template('profilebase.html')


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
