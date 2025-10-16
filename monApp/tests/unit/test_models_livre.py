from monApp.models import Livre, Auteur

def test_livre_init():
    """
    Teste l'initialisation d'un objet Livre.
    """
    livre = Livre(Titre="Les Misérables", Prix=10.5, auteur_id=1, Url="https://example.com/lesmiserables", Img="https://example.com/lesmiserables.jpg")
    assert livre.Titre == "Les Misérables"
    assert livre.Prix == 10.5
    assert livre.auteur_id == 1
    assert livre.Url == "https://example.com/lesmiserables"
    assert livre.Img == "https://example.com/lesmiserables.jpg"
    

def test_livre_repr(testapp):
    """
    Teste la représentation textuelle d'un objet Livre.
    Utilise la fixture 'testapp' pour accéder à la base de données de test.
    """
    with testapp.app_context():
        
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"