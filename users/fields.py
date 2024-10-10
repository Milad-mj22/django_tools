from django.db import models
from jdatetime import datetime as jdatetime

class JalaliDateField(models.DateField):
    def to_python(self, value):
        if value:
            if isinstance(value, jdatetime):
                return value
            return jdatetime.fromgregorian(date=value)
        return value

    def get_prep_value(self, value):
        if value:
            return value.togregorian()
        return value
