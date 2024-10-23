from flask import Blueprint


customapi = Blueprint(
    "customapi", __name__)


def page():
    return "Hello, customapi!"


customapi.add_url_rule(
    "/customapi/page", view_func=page)


def get_blueprints():
    return [customapi]
