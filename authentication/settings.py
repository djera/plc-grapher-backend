default_settings = {
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'SET_PASSWORD_RETYPE': False,
    'SET_USERNAME_RETYPE': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': False,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': False,
    'ROOT_VIEW_URLS_MAPPING': {},
    'PASSWORD_VALIDATORS': [],
    'SERIALIZERS': {
        'activation': 'authentication.serializers.ActivationSerializer',
        'login': 'authentication.serializers.LoginSerializer',
        'password_reset': 'authentication.serializers.PasswordResetSerializer',
        'password_reset_confirm': 'authentication.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'authentication.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'authentication.serializers.SetPasswordSerializer',
        'set_password_retype': 'authentication.serializers.SetPasswordRetypeSerializer',
        'set_username': 'authentication.serializers.SetUsernameSerializer',
        'set_username_retype': 'authentication.serializers.SetUsernameRetypeSerializer',
        'user_registration': 'authentication.serializers.UserRegistrationSerializer',
        'user': 'authentication.serializers.UserSerializer',
        'token': 'authentication.serializers.TokenSerializer',
    },
    'LOGOUT_ON_PASSWORD_CHANGE': False,
}

def get(key):
    return default_settings[key]

def merge_settings_dicts(a, b, path=None, overwrite_conflicts=True):
    """merges b into a, modify a in place

    Found at http://stackoverflow.com/a/7205107/1472229
    """
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_settings_dicts(
                    a[key], b[key], path + [str(key)],
                    overwrite_conflicts=overwrite_conflicts)
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                if overwrite_conflicts:
                    a[key] = b[key]
                else:
                    conflict_path = '.'.join(path + [str(key)])
                    raise Exception('Conflict at %s' % conflict_path)
        else:
            a[key] = b[key]
    # Don't let this fool you that a is not modified in place
    return a
