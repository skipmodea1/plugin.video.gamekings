#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import xbmc
import xbmcaddon
from bs4 import BeautifulSoup


#
# Constants
# 
ADDON = "plugin.video.gamekings"
SETTINGS = xbmcaddon.Addon()
LANGUAGE = SETTINGS.getLocalizedString
IMAGES_PATH = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources')
BASE_URL_GAMEKINGS_TV = "https://www.gamekings.tv/"
TWITCH_URL_GAMEKINGS_TV = "https://player.twitch.tv/?channel=gamekings"
PREMIUM_ONLY_VIDEO_TITLE_PREFIX = '* '
LOGIN_URL = 'https://www.gamekings.tv/wp-login.php'
DATE = "2019-05-25"
VERSION = "1.2.16-SNAPSHOT"


if sys.version_info[0] > 2:
    unicode = str


def convertToUnicodeString(s, encoding='utf-8'):
    """Safe decode byte strings to Unicode"""
    if isinstance(s, bytes):  # This works in Python 2.7 and 3+
        s = s.decode(encoding)
    return s


def convertToByteString(s, encoding='utf-8'):
    """Safe encode Unicode strings to bytes"""
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return s


def log(name_object, object):
    try:
        # Let's try and remove any non-ascii stuff first
        object = object.encode('ascii', 'ignore')
    except:
        pass

    try:
        xbmc.log("[ADDON] %s v%s (%s) debug mode, %s = %s" % (
            ADDON, VERSION, DATE, name_object, convertToUnicodeString(object)), xbmc.LOGDEBUG)
    except:
        xbmc.log("[ADDON] %s v%s (%s) debug mode, %s = %s" % (
            ADDON, VERSION, DATE, name_object, "Unable to log the object due to an error while converting it to an unicode string"), xbmc.LOGDEBUG)


def getSoup(html,default_parser="html5lib"):
    soup = BeautifulSoup(html, default_parser)
    return soup