import xbmc, time, xbmcaddon

time.sleep(4)

xbmc.executebuiltin('UpdateAddonRepos()')

xbmc.executebuiltin('UpdateLocalAddons()')