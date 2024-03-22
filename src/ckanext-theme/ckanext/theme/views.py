from flask import Blueprint


theme = Blueprint(
    "theme", __name__)


def page():
    return "Hello, theme!"


theme.add_url_rule(
    "/theme/page", view_func=page)


def get_blueprints():
    return [theme]
