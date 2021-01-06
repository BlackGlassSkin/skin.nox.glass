import xbmc, time
 
xbmc.executebuiltin('ActivateWindow(10700)')

xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "pvr.iptvsimple", "enabled": true }, "id":1}')

time.sleep(12)
xbmc.executebuiltin('ReloadSkin()')