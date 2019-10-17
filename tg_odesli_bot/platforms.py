"""Supported platforms."""
import re
from abc import ABC
from typing import Pattern, Union

#: Supported platforms
PLATFORMS = {}


class PlatformABC(ABC):
    """Platform data holder."""

    # Platform's Odesli name
    key: str
    # RegEx to find platform's URL in a message text
    url_re: Union[str, Pattern]
    # Human readable name which will appear in bot message
    name: str
    # Order of platform link in bot message
    order: int

    def __init_subclass__(cls, **kwargs):
        """Compile regex and add platform to a platform registry."""
        super().__init_subclass__(**kwargs)
        cls.url_re = re.compile(cls.url_re)
        PLATFORMS[cls.key] = cls()


class DeezerPlatform(PlatformABC):
    """Deezer platform."""

    key = 'deezer'
    url_re = r'https?://([a-zA-Z\d-]+\.)*deezer\.com/[^\s.,]*'
    name = 'Deezer'
    order = 0


class GoogleMusicPlatform(PlatformABC):
    """Google Music platform."""

    key = 'google'
    url_re = r'https?://([a-zA-Z\d-]+\.)*play\.google\.com/music/[^\s.,]*'
    name = 'Google Music'
    order = 1


class SoundCloudPlatform(PlatformABC):
    """SoundCloud platform."""

    key = 'soundcloud'
    url_re = r'https?://([a-zA-Z\d-]+\.)*soundcloud\.com/[^\s.,]*'
    name = 'SoundCloud'
    order = 2


class YandexMusicPlatform(PlatformABC):
    """Yandex Music platform."""

    key = 'yandex'
    url_re = r'https?://([a-zA-Z\d-]+\.)*music\.yandex\.(com|ru)/[^\s.,]*'
    name = 'Yandex Music'
    order = 3


class SpotifyPlatform(PlatformABC):
    """Spotify platform."""

    key = 'spotify'
    url_re = r'https?://([a-zA-Z\d-]+\.)*spotify\.com/[^\s.,]*'
    name = 'Spotify'
    order = 4
