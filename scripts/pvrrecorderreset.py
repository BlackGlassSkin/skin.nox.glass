import xbmc, time, xbmcaddon

xbmc.executebuiltin('ActivateWindow(none)')

xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "plugin.video.iptv.recorder", "enabled": false }, "id":1}')

time.sleep(5)
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "plugin.video.iptv.recorder", "enabled": true }, "id":1}')