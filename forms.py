"""forms for adoption"""


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional



class AddPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField(
        "Pet name",
        validators=[InputRequired(), Length(max=20)],
    )
    
    species = SelectField(
        "species",
        choices=[("cat", "Cat"), ("dog", "Dog")],
    )

    photo_url = StringField(
        """URL photo""",

        validators=[Optional(),URL],
    )

    age = IntegerField(
        "age",
        validators=[Optional(), NumberRange(min=0, max=20)],
    )

    notes = TextAreaField(
        """notes, comments""",
        validators=[Optional(), Length(min=5, max=500)],
    )

class EditPetForm(FlaskForm):
    """form for editing existing pet"""


    photo_url = StringField(
        "Photo",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "notes",
        validators=[Optional(), Length(min=5, max=500)],
    )

    available = BooleanField("Available")