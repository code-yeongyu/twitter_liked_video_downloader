"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class ERTFlixBaseIE(InfoExtractor):
    ...


class ERTFlixCodenameIE(ERTFlixBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class ERTFlixIE(ERTFlixBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class ERTWebtvEmbedIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _BASE_PLAYER_URL_RE = ...
    _VALID_URL = ...
    _EMBED_REGEX = ...
    _TESTS = ...


