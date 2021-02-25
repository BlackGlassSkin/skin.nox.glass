#!/usr/bin/env python
 
import xbmcgui
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import json

relative = None
queries = None
adsblocked = None
clients = None
status = None


if queries == None:
    try:
        f = urlopen('http://pi.hole/admin/api.php')
        json_string = f.read()
        parsed_json = json.loads(json_string)
        relative = parsed_json['domains_being_blocked']
        queries = parsed_json['dns_queries_today']
        adsblocked = parsed_json['ads_blocked_today']
        clients = parsed_json['unique_clients']
        status = parsed_json['status']
        
        f.close()
    except: pass

xbmcgui.Window(10000).setProperty('relative', '%s' % (relative))
xbmcgui.Window(10000).setProperty('queries', '%s' % (queries))
xbmcgui.Window(10000).setProperty('adsblocked', '%s' % (adsblocked))
xbmcgui.Window(10000).setProperty('clients', '%s' % (clients))
xbmcgui.Window(10000).setProperty('status', '%s' % (status))
