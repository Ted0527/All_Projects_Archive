import re

from django.core.exceptions import ValidationError

def validate_check(user_email, user_password):
    REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

    if not re.match(REGEX_EMAIL, user_email) or user_email is None:
        raise ValidationError(
            '[Email] ValidationError'
        )

    if not re.match(REGEX_PASSWORD, user_password) or user_password is None:
        raise ValidationError(
            '[Password] ValidationError'
        )