from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from .models import User
from hashlib import sha256


class LoginForm(FlaskForm):
    Login = StringField('Identifiant', validators=[DataRequired()])
    Password = PasswordField('Mot de passe', validators=[DataRequired()])
    next = HiddenField()

    def get_authenticated_user(self):
        unUser = User.query.get(self.Login.data)
        if unUser is None:
            return None
        m = sha256()
        m.update(self.Password.data.encode())
        passwd = m.hexdigest()
        return unUser if passwd == unUser.Password else None
    


    




class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])



class FormLivres(FlaskForm):
    idL=HiddenField('idL')
    prix = FloatField('Prix', validators=[DataRequired()])
    titre = StringField('Titre', validators =[DataRequired()])
    url = StringField('Url', validators =[DataRequired()])
    img = StringField('Img', validators =[DataRequired()])
    auteur = StringField('Auteur', validators =[DataRequired()])
