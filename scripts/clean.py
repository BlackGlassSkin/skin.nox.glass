import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs
import re
import time

try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = xbmc.translatePath

thumbnailPath = translatePath('special://thumbnails');
tempPath      = translatePath('special://temp')
purgePath     = translatePath('special://home/addons/packages')
cachePath     = os.path.join(translatePath('special://home'), 'cache')
THUMBS        = translatePath(os.path.join('special://home/userdata/Thumbnails',''))
addontemp     = translatePath(os.path.join('special://home/addons/temp',''))

time.sleep(1)

for root, dirs, files in os.walk(purgePath):
    file_count = 0
    file_count += len(files)
for root, dirs, files in os.walk(purgePath):
    file_count = 0
    file_count += len(files)
    if file_count > 0:
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    xbmcgui.Dialog().notification('Cleaning....' , 'Clean Packages Completed' , '3000')

time.sleep(2)

for root, dirs, files in os.walk(addontemp):
    file_count = 0
    file_count += len(files)
for root, dirs, files in os.walk(addontemp):
    file_count = 0
    file_count += len(files)
    if file_count > 0:
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    xbmcgui.Dialog().notification('Cleaning....' , 'Clean Addon Temp Completed' , '3000')

time.sleep(3)

for root, dirs, files in os.walk(tempPath):
    file_count = 0
    file_count += len(files)
    if file_count > 0:
        for f in files:
            try:
                if (f == "xbmc.log" or f == "xbmc.old.log" or f == "kodi.log" or f == "kodi.old.log" or f == "archive_cache" or f == "commoncache.db" or f == "commoncache.socket" or f == "temp"): continue
                os.unlink(os.path.join(root, f))
            except:
                pass
        for d in dirs:
            try:
                if (d == "archive_cache" or d == "temp"): continue
                shutil.rmtree(os.path.join(root, d))
            except:
                pass

    else:
        pass
xbmcgui.Dialog().notification('Cleaning....' , 'Clean Temp Completed' , '3000')

time.sleep(4)

for root, dirs, files in os.walk(thumbnailPath):
    file_count = 0
    file_count += len(files)
    if file_count > 0:
        for f in files:
            try:
                os.unlink(os.path.join(root, f))
            except:
                pass

if os.path.exists(THUMBS):
    try:
        for root, dirs, files in os.walk(THUMBS):
            file_count = 0
            file_count += len(files)
            # Count files and give option to delete
            if file_count > 0:
                for f in files: os.unlink(os.path.join(root, f))
                for d in dirs: shutil.rmtree(os.path.join(root, d))
    except:
        pass

    try:
        text13 = os.path.join(databasePath,"Textures13.db")
        os.unlink(text13)
    except:
        pass
xbmcgui.Dialog().notification('Cleaning....' , 'Clean Thumbs Completed' , '3000')

time.sleep(5)

for root, dirs, files in os.walk(cachePath):
        file_count = 0
        file_count += len(files)
        if file_count > 0:

                for f in files:
                    try:
                        if (f == "xbmc.log" or f == "xbmc.old.log" or f == "kodi.log" or f == "kodi.old.log" or f == "archive_cache" or f == "commoncache.db" or f == "commoncache.socket" or f == "temp"): continue
                        os.unlink(os.path.join(root, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        if (d == "archive_cache" or d == "temp"): continue
                        shutil.rmtree(os.path.join(root, d))
                    except:
                        pass

        else:
            pass

for root, dirs, files in os.walk(tempPath):
    file_count = 0
    file_count += len(files)
    if file_count > 0:
        for f in files:
            try:
                if (f == "xbmc.log" or f == "xbmc.old.log" or f == "kodi.log" or f == "kodi.old.log" or f == "archive_cache" or f == "commoncache.db" or f == "commoncache.socket" or f == "temp"): continue
                os.unlink(os.path.join(root, f))
            except:
                pass
        for d in dirs:
            try:
                if (d == "archive_cache" or d == "temp"): continue
                shutil.rmtree(os.path.join(root, d))
            except:
                pass

    else:
        pass

if xbmc.getCondVisibility('system.platform.ATV2'):
    atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')

    for root, dirs, files in os.walk(atv2_cache_a):
        file_count = 0
        file_count += len(files)

        if file_count > 0:
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        else:
            pass
    atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')

    for root, dirs, files in os.walk(atv2_cache_b):
        file_count = 0
        file_count += len(files)

        if file_count > 0:
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        else:
            pass

cacheEntries = []

for entry in cacheEntries:
    clear_cache_path = translatePath(entry.path)
    if os.path.exists(clear_cache_path)==True:
        for root, dirs, files in os.walk(clear_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
            else:
                pass
xbmcgui.Dialog().notification('Cleaning....' , 'Clean Cache Completed' , '3000')

time.sleep(10)
xbmc.executebuiltin('RunScript(special://skin/scripts/fsize.py)')