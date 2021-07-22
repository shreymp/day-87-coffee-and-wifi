from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = StringField('Location (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location (City)', validators=[DataRequired()])
    has_sockets = SelectField('Has Sockets?', validators=[DataRequired()], choices=['Choose:', 'True', 'False'])
    has_toilets = SelectField('Has Toilets?', validators=[DataRequired()], choices=['Choose:', 'True', 'False'])
    has_wifi = SelectField('Has Wifi?', validators=[DataRequired()], choices=['Choose:', 'True', 'False'])
    can_take_calls = SelectField('Can Take Calls?', validators=[DataRequired()], choices=['Choose:', 'True', 'False'])
    seats = SelectField('Number of Seats', validators=[DataRequired()], choices=['Choose:', '0 - 20', '20 - 40', '40 - 60', '60 - 80', '80 - 100', '100+'])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])

    submit = SubmitField('Submit')