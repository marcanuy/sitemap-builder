from urllib.parse import urlparse

def valid_uri(uri):
    try:
        result = urlparse(uri)
        return result.scheme and result.netloc and result.path
    except:
        return False
