from .app import app
from monApp.forms import *
from monApp.models import Auteur,Livre
from .app import db
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user

@app.route ("/login/", methods =("GET","POST",))
def login():
    unForm = LoginForm()
    unUser = None
    if not unForm.is_submitted():
        unForm.next.data = request.args.get('next')
    elif unForm.validate_on_submit():
        unUser = unForm.get_authenticated_user()
        if unUser:
            login_user(unUser)
            next_url = unForm.next.data or url_for("index", name=unUser.Login)
            return redirect(next_url)
    return render_template("login.html", form=unForm)

@app.route ("/logout/")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/about/")
def about() :
 return render_template("about.html",title ="About",about=app.config["ABOUT"])


@app.route("/contact/")
def contact() :
 return render_template("contact.html",title ="Contact",contact=app.config["CONTACT"]) 

@app.route('/')
def index():
# si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livres_list.html', title="R3.01 Dev Web avec Flask", livres=lesLivres)

@app.route('/auteurs/<idA>/update/')
@login_required
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)


@app.route ('/auteur/save/', methods =("POST" ,))
def saveAuteur():
    updatedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à modifier
    idA = int(unForm.idA.data)
    updatedAuteur = Auteur.query.get(idA)
    #si les données saisies sont valides pour la mise à jour
    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        return redirect(url_for('viewAuteur', idA=updatedAuteur.idA))
    return render_template("auteur_update.html",selectedAuteur=updatedAuteur, updateForm=unForm)


@app.route('/auteurs/<idA>/view/')
def viewAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur (idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_view.html",selectedAuteur=unAuteur, viewForm=unForm)

@app.route('/auteur/')
def createAuteur():
    unForm = FormAuteur()
    return render_template("auteur_create.html", createForm=unForm)

@app.route ('/auteur/insert/', methods =("POST" ,))
@login_required
def insertAuteur():
    insertedAuteur = None
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        insertedAuteur = Auteur(Nom=unForm.Nom.data)
        db.session.add(insertedAuteur)
        db.session.commit()
        insertedId = Auteur.query.count()
        return redirect(url_for('viewAuteur', idA=insertedId))
    return render_template("auteur_create.html", createForm=unForm)

@app.route('/auteurs/<idA>/delete/')
@login_required
def deleteAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template("auteur_delete.html",selectedAuteur=unAuteur, deleteForm=unForm)

@app.route ('/auteur/erase/', methods =("POST" ,))
@login_required
def eraseAuteur():
    deletedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à supprimer
    idA = int(unForm.idA.data)
    deletedAuteur = Auteur.query.get(idA)
    #suppression
    db.session.delete(deletedAuteur)
    db.session.commit()
    return redirect(url_for('getAuteurs'))


@app.route('/livres/<idL>/update/')
@login_required
def updateLivre(idL):
    unLivre = Livre.query.get(idL)
    if not unLivre:
        return redirect(url_for('getLivres'))
    unForm = FormLivres(idL=unLivre.idL , Titre=unLivre.Titre, Prix=unLivre.Prix, Url=unLivre.Url, Img=unLivre.Img, auteur_id=unLivre.auteur_id)
    return render_template("livre_update.html",selectedLivre=unLivre, updateForm=unForm)


@app.route('/livres/<idL>/view/')
def viewLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivres(idL=unLivre.idL , titre=unLivre.Titre, prix=unLivre.Prix, url=unLivre.Url, img=unLivre.Img, auteur_id=unLivre.auteur_id)
    return render_template("livre_view.html",selectedLivre=unLivre, viewForm=unForm)

@app.route('/livre/save/', methods=["POST"])
@login_required
def saveLivre():
    unForm = FormLivres()
    if unForm.validate_on_submit():
        idL = int(unForm.idL.data)
        livre = Livre.query.get(idL)
        if livre:
            livre.Titre = unForm.titre.data
            livre.Prix = float(unForm.prix.data) if unForm.prix.data else None
            livre.Url = unForm.url.data
            livre.Img = unForm.img.data
            livre.auteur_id = int(unForm.auteur_id.data) if unForm.auteur_id.data else None
            db.session.commit()
            return redirect(url_for('viewLivre', idL=livre.idL))
    # En cas d'erreur, on recharge le formulaire avec les erreurs
    selectedLivre = Livre.query.get(int(unForm.idL.data))
    return render_template("livre_update.html", selectedLivre=selectedLivre, updateForm=unForm)






if __name__== "__main__" :
 app.run()