import xbmc, time

xbmc.executebuiltin("ActivateWindow(home,return)")
time.sleep(1)
xbmc.executebuiltin('RunPlugin("plugin://script.ezmaintenanceplus/?url=url&action=clear_packages",return)')
time.sleep(2)
xbmc.executebuiltin('RunPlugin("plugin://script.ezmaintenanceplus/?url=url&action=clear_cache",return)')
time.sleep(3)
xbmc.executebuiltin('RunPlugin("plugin://script.ezmaintenanceplus/?url=url&action=clear_thumbs",return)')
time.sleep(4)
xbmc.executebuiltin("ActivateWindow(1101)")