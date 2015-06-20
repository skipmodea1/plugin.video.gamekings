import os
import xbmcaddon

#
# Constants
# 
__addon__       = "plugin.video.gamekings"
__settings__    = xbmcaddon.Addon(id=__addon__ )
__language__    = __settings__.getLocalizedString
__images_path__ = os.path.join( xbmcaddon.Addon(id=__addon__ ).getAddonInfo('path'), 'resources', 'images' )
__date__        = "20 June 2015"
__version__     = "1.1.3"