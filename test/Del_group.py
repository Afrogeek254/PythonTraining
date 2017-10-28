

def test_del_first__group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.log_out()
