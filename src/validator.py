from jsonschema import validate
from jsonschema.exceptions import ValidationError
from src.json_schema import schema

def validate_structure(obj):
    try:
        validate(instance=obj, schema=schema)
        return True
    except ValidationError:
        return False


def validate_semantic(obj):
    return any(len(obj[k]) > 0 for k in obj)
