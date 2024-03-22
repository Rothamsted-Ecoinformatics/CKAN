"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.theme.logic import validators


def test_theme_reauired_with_valid_value():
    assert validators.theme_required("value") == "value"


def test_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.theme_required(None)
