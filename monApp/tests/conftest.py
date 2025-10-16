import pytest
from monApp import app,db
from monApp.models import Auteur,Livre, User
from hashlib import sha256
@pytest.fixture
def testapp():
    app.config.update({"TESTING":True,"SQLALCHEMY_DATABASE_URI":
    "sqlite:///:memory:","WTF_CSRF_ENABLED": False})
    with app.app_context():
        db.create_all()
    # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        
        # Ajouter un livre de test
        livre = Livre(Titre="Les Misérables", Prix=10.5, auteur_id=auteur.idA,Url="https://example.com/lesmiserables",Img="https://example.com/lesmiserables.jpg")
        db.session.add(livre)
        # Ajouter un utilisateur de test (mot de passe hashé)
        m = sha256()
        m.update(b"testpassword")
        user = User(Login="testuser", Password=m.hexdigest())
        db.session.add(user)
        m2 = sha256()
        m2.update(b"AIGRE")
        user2 = User(Login="CDAL", Password=m2.hexdigest())
        db.session.add(user2)
        db.session.commit()



    yield app
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()