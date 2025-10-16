from monApp.models import User ,load_user

def test_user_init():
    """
    Teste l'initialisation d'un objet User.
    """
    user = User(Login="testuser", Password="password")
    assert user.Login == "testuser"
    assert user.Password == "password"

def test_user_repr(testapp):
    """
    Teste la représentation textuelle d'un objet User.
    """
    with testapp.app_context():
        # Récupère l'utilisateur 'testuser' créé dans conftest.py
        user = User.query.get("testuser")
        assert repr(user) == "<User testuser>"
def test_load_user(testapp):
    """
    Teste la fonction de chargement de l'utilisateur.
    """
    with testapp.app_context():
        user = load_user("testuser")
        assert user is not None
        assert user.Login == "testuser"
        assert load_user("nonexistent") is None

def test_get_id():
    """
    Teste la méthode get_id() de l'objet User.
    """
    user = User(Login="testuser", Password="password")
    assert user.get_id() == "testuser"