import uuid


def get_random_code():
    code = str(uuid.uuid4())[:8].raplace('-','').lower()
    return code
    