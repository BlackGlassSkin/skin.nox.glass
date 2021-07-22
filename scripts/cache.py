import xbmc, time

xbmc.executebuiltin("ActivateWindow(home,return)")
time.sleep(1)
xbmc.executebuiltin('RunPlugin("plugin://script.ezmaintenanceplus/?url=ur&action=adv_settings",return)')
time.sleep(3)
xbmc.executebuiltin("ActivateWindow(1101)")