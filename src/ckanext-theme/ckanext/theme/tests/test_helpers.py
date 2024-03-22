"""Tests for helpers.py."""

import ckanext.theme.helpers as helpers


def test_theme_hello():
    assert helpers.theme_hello() == "Hello, theme!"
