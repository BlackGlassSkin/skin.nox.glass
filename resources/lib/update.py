import xbmc, time, xbmcaddon

time.sleep(4)

xbmc.executebuiltin('UpdateAddonRepos()')

time.sleep(5)
xbmc.executebuiltin('UpdateLocalAddons()')