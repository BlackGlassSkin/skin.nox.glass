import xbmc, time

time.sleep(10)
xbmc.executebuiltin('ActivateWindow(Videos,plugin://plugin.video.canalplusvod/?mode=login&url=&page=0&moviescount=0&movie=True&name=Zaloguj,True)')

time.sleep(15)
xbmc.executebuiltin('ActivateWindow(10702)')

time.sleep(18)
xbmc.executebuiltin('ReloadSkin()')