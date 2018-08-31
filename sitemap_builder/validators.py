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

def valid_change_frequency(changefreq):
    """Checks an allowed value of changefreq is used

    :param str changefreq:
    :return boolean:
    """
    from .models import CHANGE_FREQ
    result = changefreq in CHANGE_FREQ
    return result

def valid_priority_value(priority):
    """Checks for values between 0.0 and 1.0

    :param float priority:
    :return boolean:
    """
    if not isinstance(priority, float):
        return False
    result = 0 <= priority <= 1
    return result

def valid_priority_len(priority):
    """Checks for values with exactly one significant digit

    :param float priority:
    :return boolean:
    """
    result = len(str(priority).rsplit('.')[-1]) == 1
    return result

# def valid_datetime(value):
#     """Checks for valid iso8601 datetime values

#     :param str value:
#     :return boolean:
#     """
#     if match_iso8601(value) is not None:
#         return True
