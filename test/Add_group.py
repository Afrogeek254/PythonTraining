# -*- coding: utf-8 -*-
from model.Clases import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test", header="test_group", footer="Test"))
    app.session.log_out()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.log_out()

