from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import Length, Required, Email

class contactform(FlaskForm):
    name = TextField('Name',validators = [Length(max = 30),Required()])
    email = TextField('Email',validators = [Length(max = 120),Email()])
    subject = TextField('Subject',validators = [Length(max =100),Required()])
    message = TextAreaField('Message',validators = [Length(max = 1000),Required()])
    submit1 = SubmitField('Send')


class autocompleteform(FlaskForm):
    autocomplete_list = TextField('autocomplete_list')
