from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchBar(FlaskForm):
    text = StringField('search', validators=[DataRequired()])
    search_btn = SubmitField('Search')