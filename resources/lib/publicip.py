# Cherry

import xbmcgui
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import json

publicip = None
publiccountry = None
publiccity = None
publicisp = None
timezone = None
utc = None
region = None
capital = None
currency = None
currencytwo = None
directional = None
flagUrlicon = None


if publicip == None:
    try:
        result = json.load(urlopen('https://ipapi.co/json/'))
        publicip = result['ip']
        publiccountry = result['country_name']
        publiccity = result['city']
        publicisp = result['org']
        timezone = result['timezone']
        utc = result['utc_offset']
        region = result['region']
        capital = result['country_capital']
        currency = result['currency']
        currencytwo = result['currency_name']
        directional = result['country_calling_code'].replace('+','')
        flagUrlicon = result['country_code'].lower()
    except: pass

if publicip == None:
    try:
        result = json.load(urlopen('https://ip-api.io/json/'))
        publicip = result['ip'] 
        publiccountry = result['country_name'] #panstwo
        publiccity = result['city'] #miasto
        publicisp = result['organisation'] #dostawca
        timezone = result['time_zone'] #strefa_czasowa
        region = result['region_name'] #panstwo
        capital = result['countryCapital'] #stolica
        currency = result['currencySymbol'] #WALURA SYMBOL
        currencytwo = result['currency']#WALUTA
        directional = result['callingCode']#KIERUNKOWY
        flagUrlicon = result['country_code'].lower()
    except: pass

if publicip == None: publicip = ''
if publiccountry == None: publiccountry = ''
if publiccity == None: publiccity = ''
if publicisp == None: publicisp = ''
if timezone == None: timezone = ''
if utc == None: utc = ''
if region == None: region = ''
if capital == None: capital = ''
if currency == None: currency = ''
if directional == None: directional = ''
if flagUrlicon == None: flagUrlicon = ''


xbmcgui.Window(10000).setProperty('publicnetwork', '%s %s %s' % (publicip, publiccountry, publiccity))
xbmcgui.Window(10000).setProperty('publicnetworkformat', '[COLOR FF73FFDE]%s[/COLOR] ||[COLOR FF73FFDE] %s[/COLOR] ||[COLOR FF73FFDE] %s[/COLOR]' % (publicip, publiccountry, publiccity))
xbmcgui.Window(10000).setProperty('publicip', publicip)
xbmcgui.Window(10000).setProperty('publiccountry', publiccountry)
xbmcgui.Window(10000).setProperty('publiccity', publiccity)
xbmcgui.Window(10000).setProperty('publicisp', publicisp)
xbmcgui.Window(10000).setProperty('timezone', timezone)
xbmcgui.Window(10000).setProperty('utc', utc)
xbmcgui.Window(10000).setProperty('region', region)
xbmcgui.Window(10000).setProperty('capital', capital)
xbmcgui.Window(10000).setProperty('currency', currency)
xbmcgui.Window(10000).setProperty('currencytwo', currencytwo)
xbmcgui.Window(10000).setProperty('directional', '+%s' % (directional))
xbmcgui.Window(10000).setProperty('flagUrlicon', flagUrlicon)