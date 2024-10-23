"""Tests for helpers.py."""

import ckanext.customapi.helpers as helpers


def test_customapi_hello():
    assert helpers.customapi_hello() == "Hello, customapi!"
