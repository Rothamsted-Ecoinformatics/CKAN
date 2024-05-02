from pylons import config

import ckan.logic as logic
from ckan.logic.action.create import user_create as ckan_user_create
import ckan.plugins.toolkit as toolkit


def user_create(context, data_dict):
    user = ckan_user_create(context, data_dict)

    org_name = "9763f144-ab0a-464c-b5b8-912d121728d2"
    role = "editor"

    try:
        toolkit.get_action('organization_show')(
            context, {
                'id': org_name,
            }
        )
    except logic.NotFound:
        return user

    toolkit.get_action('organization_member_create')(
        context, {
            'id': org_name,
            'username': user['name'],
            'role': role,
        }
    )

    return user
