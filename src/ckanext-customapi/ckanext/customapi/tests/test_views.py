"""Tests for views.py."""

import pytest

import ckanext.customapi.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "customapi")
@pytest.mark.usefixtures("with_plugins")
def test_customapi_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("customapi.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, customapi!"
