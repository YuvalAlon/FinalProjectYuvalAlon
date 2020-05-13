from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

class ExpandForm(FlaskForm):
	submit1 = SubmitField('Expand')
	name="Expand"
	value="Expand"
 
class CollapseForm(FlaskForm):
	submit2 = SubmitField('Collapse')
	name="Collapse"
	value="Collapse"

class QueryForm(FlaskForm):
	# adds the team choosing option
	team = SelectField("enter team",validators = [DataRequired])
	#adds the position choosing option
	pos = SelectField("enter position", validators = [DataRequired], choices = [("C", "Center"),("PF", "Power Forward"), ("SF", "Small Forward"), ("SG", "Shooting Guard"), ("PG", "Point Guard")])
	submit = SubmitField("sumbit")