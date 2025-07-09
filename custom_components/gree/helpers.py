from voluptuous import Schema, Invalid

def mode_validator(allowed_values):
    def validator(value):
        if isinstance(value, list):
            parts = value
        elif isinstance(value, str):
            parts = [v.strip() for v in value.split(",") if v.strip()]
        else:
            raise Invalid("Must be a list or comma-delimited string")
        
        invalid = [v for v in parts if v not in allowed_values]
        if invalid:
            raise Invalid(f"Invalid value(s): {', '.join(invalid)}. Allowed: {', '.join(allowed_values)}")
        
        return parts
    return validator

def string_to_list(value):
    if isinstance(value, str):
        return [v.strip() for v in value.split(",") if v.strip()]
    elif isinstance(value, list):
        return value
    return []
