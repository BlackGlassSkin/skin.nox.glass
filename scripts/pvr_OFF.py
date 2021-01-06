import xbmc, time


xbmc.executebuiltin('ActivateWindow(10700)')
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "pvr.iptvsimple", "enabled": false }, "id":1}')