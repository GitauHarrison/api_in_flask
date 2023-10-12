from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, \
    Regexp, ValidationError
from app.models import User


# -----------------------
# Login
# -----------------------


class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={'autofocus': True, 'placeholder': 'You have access to this email address'})
    password = PasswordField(
        'Password:',
        validators=[DataRequired(), Length(min=8, max=20),
        Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
               message='Password must be at least 8 characters long and '
               'contain at least one letter (Capital) and one number.')],
        render_kw={'placeholder': 'Example: Hard2Gue55'})
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


# -----------------------
# End of user login
# -----------------------

# -----------------------
# User registration
# -----------------------


class RegistrationForm(FlaskForm):
    """General User Data"""
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(1, 64)],
        render_kw={'autofocus': True, 'placeholder': 'harry'})
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'harry@email.com'})
    password = PasswordField(
        'Password:',
        validators=[DataRequired(), Length(min=8, max=20),
        Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
               message='Password must be at least 8 characters long and '
               'contain at least one letter and one number.')],
        render_kw={'placeholder': 'Example: Hard2Gue55'})
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Confirm Your Password Above'})
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Check if username already exists"""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """Check if email already exists"""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# -----------------------
# End of user registration
# -----------------------


# -----------------------
# Post
# -----------------------


class PostForm(FlaskForm):
    """Post Form"""
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=5, max=64)],
        render_kw={'autofocus': True, 'placeholder': 'Learning Flask'})
    body = StringField(
        'Body',
        validators=[DataRequired(), Length(min=5, max=140)],
        render_kw={'placeholder': 'Flask is a micro-framework built using Python ...'})
    submit = SubmitField('Post')


# -----------------------
# End of user post
# -----------------------


# -----------------------
# Start: edit profile
# -----------------------

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

# -----------------------
# End: edit profile
# -----------------------
