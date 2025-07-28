from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField(name="Email",validators=[DataRequired(),Email()])
    password = PasswordField(name="Password",validators=[DataRequired()])
    name = StringField(name="Name",validators=[DataRequired()])
    submit = SubmitField(name="Sign Me Up!")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(name="Email",validators=[DataRequired(),Email()])
    password = PasswordField(name="Password",validators=[DataRequired()])
    submit = SubmitField(name="Let Me In.")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField("Comments ", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")