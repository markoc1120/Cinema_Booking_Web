from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    card_type = StringField('Card Type', validators=[DataRequired()])
    card_number = StringField('Card Number', validators=[DataRequired()])
    card_cvc = StringField('Card CVC', validators=[DataRequired()])
    card_holder_name = StringField('Card Holder Name', validators=[DataRequired()])
    submit = SubmitField("Book me!")
