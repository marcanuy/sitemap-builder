from urllib.parse import urlparse

def valid_uri(uri):
    """Checks for a well formed URI that includes protocol

    :param str uri:
    :return boolean:
    """
    try:
        result = urlparse(uri)
        return result.scheme and result.netloc and result.path
    except:
        return False

def valid_uri_length(uri):
    """Checks that a URI has the expected length (<2048 chars) 
    as required by https://www.sitemaps.org/protocol.html

    :param str uri:
    :return boolean:
    """
    result = len(uri) <= 2048
    return result


# def valid_datetime(value):
#     """Checks for valid iso8601 datetime values

#     :param str value:
#     :return boolean:
#     """
#     if match_iso8601(value) is not None:
#         return True
