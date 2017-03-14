from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FileField
from wtforms.validators import InputRequired

class ProfileForm(FlaskForm):
    fname = StringField('fname', validators=[InputRequired()])
    lname = StringField('lname', validators=[InputRequired()])
    user = StringField('user', validators=[InputRequired()])
    age = IntegerField('age', validators=[InputRequired()])
    gen = SelectField(u'gen', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    bio = StringField('bio', validators=[InputRequired()])
    img = FileField(u'img', validators=[InputRequired()])