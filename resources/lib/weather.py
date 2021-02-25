import xbmc, time, xbmcaddon

xbmc.executebuiltin('ActivateWindow(none)')
time.sleep(5)

xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.weatherbit.io", "enabled": false }, "id":1}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.yahoo", "enabled": false }, "id":1}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.gismeteo", "enabled": false }, "id":1}')

time.sleep(10)

xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.weatherbit.io", "enabled": true }, "id":1}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.yahoo", "enabled": true }, "id":1}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "weather.gismeteo", "enabled": true }, "id":1}')