from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class GenerateForm(FlaskForm):
    length = IntegerField(
        "Length",
        validators=[
            Optional(),
            NumberRange(min=6, max=36, message="Invalid password length"),
        ],
    )
    # TODO: may use on custom password generation
    # uppercase = BooleanField("Uppercase Characters")
    # punctuation = BooleanField("Punctuation")
    submit = SubmitField("Generate")


class RecordForm(FlaskForm):
    name = StringField(
        "Record Name",
        validators=[DataRequired(), Length(max=100, message="Invalid record name")],
    )
    login = StringField(
        "Login",
        validators=[DataRequired(), Length(max=100, message="Invalid login names")],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, max=128, message="Invalid password length"),
        ],
    )
    comment = StringField(
        "Comment",
        validators=[Optional(), Length(max=200, message="Invalid comment length")],
    )
    submit = SubmitField("Save")
