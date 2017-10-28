# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.Clases import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test", header="test_group", footer="Test"))
    app.session.log_out()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.log_out()
