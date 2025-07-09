from voluptuous import Schema, Invalid

def mode_validator(allowed_values):
    def validator(value):
        if not isinstance(value, str):
            raise Invalid("Must be a comma-delimited string")
        
        # Split, strip whitespace, and filter empty strings
        parts = [v.strip() for v in value.split(",") if v.strip()]
        
        # Check for any values not in the allowed list
        invalid = [v for v in parts if v not in allowed_values]
        if invalid:
            raise Invalid(f"Invalid value(s): {', '.join(invalid)}. Allowed values are: {', '.join(allowed_values)}")
        
        return value  # Or return parts if you want the list instead
    return validator