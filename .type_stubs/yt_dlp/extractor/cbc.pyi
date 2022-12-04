"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class CBCIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class CBCPlayerIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class CBCGemIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    _GEO_COUNTRIES = ...
    _TOKEN_API_KEY = ...
    _NETRC_MACHINE = ...
    _claims_token = ...
    def claims_token_expired(self): # -> bool:
        ...
    
    def claims_token_valid(self): # -> bool:
        ...
    


class CBCGemPlaylistIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    _API_BASE = ...


class CBCGemLiveIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...
    _API_URLS = ...


