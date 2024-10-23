import ckan.plugins.toolkit as tk
import ckanext.customapi.logic.schema as schema


@tk.side_effect_free
def customapi_get_sum(context, data_dict):
    tk.check_access(
        "customapi_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.customapi_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'customapi_get_sum': customapi_get_sum,
    }
