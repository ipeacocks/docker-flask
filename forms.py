from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    message = StringField(
        'message',
        validators=[DataRequired()]
    )
