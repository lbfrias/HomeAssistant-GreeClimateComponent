from voluptuous import Schema, Invalid

from voluptuous import Schema, Invalid

def is_subset_of(superset):
    def validator(value):
        if not isinstance(value, list):
            raise Invalid("Expected a list")
        if not set(value).issubset(set(superset)):
            raise Invalid(f"{value} is not a subset of {superset}")
        return value
    return validator