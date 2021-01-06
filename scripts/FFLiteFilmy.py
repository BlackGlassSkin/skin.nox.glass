import xbmc ,addon

xbmc.executebuiltin("ActivateWindow(10025,return)")
xbmc.executebuiltin('Container.Update("plugin://plugin.video.fanfilm/?action=movieSearchnew",return)')