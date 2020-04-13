import re
from functools import wraps

from flask import request

from app.main.service.authentication_helper import get_logged_in_user


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = get_logged_in_user(request)
        path = re.sub(r'/<.+>', '', request.url_rule.rule)
        is_authorized = data['data']['authorization'][path][request.method.lower()]
        token = data.get('data')

        if not token or not is_authorized:
            return data, 401

        return f(*args, **kwargs)

    return decorated
