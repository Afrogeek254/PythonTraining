# -*- coding: utf-8 -*-
import pytest
from Clases import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Test", header="test_group", footer="Test"))
    app.log_out()


def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.log_out()
