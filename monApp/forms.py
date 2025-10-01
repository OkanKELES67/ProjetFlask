from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, DecimalField, IntegerField
from wtforms.validators import Optional
from wtforms.validators import DataRequired, NumberRange


class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])


class FormLivres(FlaskForm):
    idL=HiddenField('idL')
    Titre = StringField ('Titre', validators =[DataRequired()])
    Prix = DecimalField ('Prix', places=2, validators=[DataRequired(), NumberRange(min=0)])
    Url = StringField ('Url', validators =[DataRequired()])
    Img = StringField ('Img', validators =[DataRequired()])
    auteur_id = IntegerField('auteur_id', validators=[Optional()])
