from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class ProfileForm(FlaskForm):
    fname = StringField('fname', validators=[InputRequired()])
    lname = StringField('lname', validators=[InputRequired()])
    user = StringField('user', validators=[InputRequired()])
    age = StringField('age', validators=[InputRequired()])
    #gen = SelectField(u'gen', choices=[('male', 'Male'), ('female', 'Female')], validators=[Required()])
    bio = StringField('bio', validators=[InputRequired()])
    #img = FileField('img', validators=[InputRequired()])
