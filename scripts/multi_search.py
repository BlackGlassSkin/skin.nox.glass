import xbmc
 
xbmc.executebuiltin('ActivateWindow(videos)')
xbmc.executebuiltin('RunPlugin(plugin://plugin.video.united.search/?action=search, return)')