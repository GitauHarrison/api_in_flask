from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User


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
