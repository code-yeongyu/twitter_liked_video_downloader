"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class DPlayBaseIE(InfoExtractor):
    _PATH_REGEX = ...
    _auth_token_cache = ...


class DPlayIE(DPlayBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class HGTVDeIE(DPlayBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class DiscoveryPlusBaseIE(DPlayBaseIE):
    ...


class GoDiscoveryIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class TravelChannelIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class CookingChannelIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class HGTVUsaIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class FoodNetworkIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DestinationAmericaIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class InvestigationDiscoveryIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class AmHistoryChannelIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class ScienceChannelIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DIYNetworkIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DiscoveryLifeIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class AnimalPlanetIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class TLCIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class MotorTrendIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class MotorTrendOnDemandIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DiscoveryPlusIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DiscoveryPlusIndiaIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DiscoveryNetworksDeIE(DPlayBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class DiscoveryPlusShowBaseIE(DPlayBaseIE):
    ...


class DiscoveryPlusItalyIE(DiscoveryPlusBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _PRODUCT = ...
    _DISCO_API_PARAMS = ...


class DiscoveryPlusItalyShowIE(DiscoveryPlusShowBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _BASE_API = ...
    _DOMAIN = ...
    _X_CLIENT = ...
    _REALM = ...
    _SHOW_STR = ...
    _INDEX = ...
    _VIDEO_IE = DPlayIE


class DiscoveryPlusIndiaShowIE(DiscoveryPlusShowBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    _BASE_API = ...
    _DOMAIN = ...
    _X_CLIENT = ...
    _REALM = ...
    _SHOW_STR = ...
    _INDEX = ...
    _VIDEO_IE = DiscoveryPlusIndiaIE


