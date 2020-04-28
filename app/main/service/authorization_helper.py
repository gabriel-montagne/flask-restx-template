API_NAMESPACE_PATH = {
    'user': '/api/user',
    'user_role': '/api/user_role',
    'auth': '/api/auth'
}


def init_role_authorization(role):
    """

    :param role:
    :return:
    """
    granted = role == 'admin'
    return {
        p: {'get': True, 'post': granted, 'put': granted, 'delete': granted}
        for p in API_NAMESPACE_PATH.values()
    }


def get_merged_authorization(roles):
    """

    :param roles:
    :return:
    """
    authorization = init_role_authorization('user')
    for role in roles:
        for path in authorization.keys():
            for key in ['get', 'post', 'put', 'delete']:
                authorization[path][key] = role.authorization[path][key] \
                                           or authorization[path][key]
    return authorization
