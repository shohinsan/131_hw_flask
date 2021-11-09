from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class TopCities(FlaskForm):
    """docstring for TopCities  ."""
    city_name = StringField(label="City Name", validators=[DataRequired()])
    city_rank = IntegerField(label="City Rank", validators=[DataRequired()])
    is_visited = BooleanField('Visited')
    submit = SubmitField(label='Submit')

