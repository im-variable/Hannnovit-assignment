from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_age(value):
    if value not in (range(1, 101)):
        raise ValidationError(
            _('%(value)s is not between 1 to 100'),
            params={'value': value},
        )
