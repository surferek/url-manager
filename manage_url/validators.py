import validators


def is_url(url: str) -> bool:
    if validators.url(url):
        return True
    return False
