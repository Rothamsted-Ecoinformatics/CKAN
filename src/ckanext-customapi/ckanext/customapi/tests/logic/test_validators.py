"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.customapi.logic import validators


def test_customapi_reauired_with_valid_value():
    assert validators.customapi_required("value") == "value"


def test_customapi_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.customapi_required(None)
