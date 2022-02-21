from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

class SearchForm(FlaskForm):
    search_query = StringField('Search Here:', validators=[InputRequired(), Length(min=1, max=30)])
    submit = SubmitField('Go!')

class MovieReviewForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=50)])
    text = TextAreaField('Review', validators=[InputRequired(), Length(min=1, max=500)])
    submit = SubmitField('Submit Review')