import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs
import re
import time

try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = xbmc.translatePath

packagesdir = translatePath(os.path.join('special://home/addons/packages',''))
thumbnails  = translatePath('special://thumbnails')
thumbnails1  = translatePath(os.path.join('special://thumbnails',''))
addondata   = translatePath('special://home/userdata/addon_data')
addons      = translatePath('special://home/addons')
temp        = translatePath('special://home/addons/temp')
database    = translatePath('special://database')
purgePath   = translatePath('special://home/addons/packages')
cache       = translatePath(os.path.join('special://home/cache',''))

total_size10 = 0
total_size6 = 0    
total_size5 = 0
total_size4 = 0
total_size3 = 0
total_size2 = 0
total_size  = 0
count = 0
files = folders = 0
files1 = folders1 = 0
files2 = folders2 = 0

for dirpath, dirnames, filenames in os.walk(packagesdir):
    count = 0
    for f in filenames:
        count += 1
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)
total_sizetext = "%.0f" % (total_size/1024000.0)

for dirpath2, dirnames2, filenames2 in os.walk(thumbnails):
    for f2 in filenames2:
        fp2 = os.path.join(dirpath2, f2)
        total_size2 += os.path.getsize(fp2)
total_sizetext2 = "%.0f" % (total_size2/1024000.0)

for dirpath3, dirnames3, filenames3 in os.walk(addondata):
    for f3 in filenames3:
        fp3 = os.path.join(dirpath3, f3)
        total_size3 += os.path.getsize(fp3)
total_sizetext3 = "%.0f" % (total_size3/1024000.0)

for dirpath4, dirnames4, filenames4 in os.walk(database):
    for f4 in filenames4:
        fp4 = os.path.join(dirpath4, f4)
        total_size4 += os.path.getsize(fp4)
total_sizetext4 = "%.0f" % (total_size4/1024000.0)

for dirpath5, dirnames5, filenames5 in os.walk(addons):
    for f5 in filenames5:
        fp5 = os.path.join(dirpath5, f5)
        total_size5 += os.path.getsize(fp5)
total_sizetext5 = "%.0f" % (total_size5/1024000.0)

for dirpath6, dirnames6, filenames6 in os.walk(temp):
    for f6 in filenames6:
        fp6 = os.path.join(dirpath6, f6)
        total_size6 += os.path.getsize(fp6)
total_sizetext6 = "%.0f" % (total_size6/1024000.0)

for dirpath7, dirnames7, filenames7 in os.walk(addondata):
  # ^ this idiom means "we won't be using this value"
        files += len(filenames7)
        folders += len(dirnames7)
        
for dirpath8, dirnames8, filenames8 in os.walk(thumbnails1):
  # ^ this idiom means "we won't be using this value"
        files1 += len(filenames8)
        folders1 += len(dirnames8)
        
for dirpath9, dirnames9, filenames9 in os.walk(addons):
  # ^ this idiom means "we won't be using this value"
        files2 += len(filenames9)
        folders2 += len(dirnames9)

for dirpath10, dirnames10, filenames10 in os.walk(cache):
    for f10 in filenames10:
        fp10 = os.path.join(dirpath10, f10)
        total_size10 += os.path.getsize(fp10)
total_sizetext10 = "%.0f" % (total_size10/1024000.0)

xbmcgui.Window(10000).setProperty('total_sizetext', total_sizetext)#packagesdir SIZE
xbmcgui.Window(10000).setProperty('total_sizetext2', total_sizetext2)#thumbnails SIZE
xbmcgui.Window(10000).setProperty('total_sizetext3', total_sizetext3)#addondata SIZE
xbmcgui.Window(10000).setProperty('total_sizetext4', total_sizetext4)#database SIZE
xbmcgui.Window(10000).setProperty('total_sizetext5', total_sizetext5)#addons SIZE
xbmcgui.Window(10000).setProperty('total_sizetext6', total_sizetext6)#temp SIZE
xbmcgui.Window(10000).setProperty('total_sizetext10', total_sizetext10)#CACHE SIZE
xbmcgui.Window(10000).setProperty('str(count)', str(count))#packages FILES
xbmcgui.Window(10000).setProperty('str(files)', str(files))#addondata FILES
xbmcgui.Window(10000).setProperty('str(folders)', str(folders))#addondata FOLDERS
xbmcgui.Window(10000).setProperty('str(files1)', str(files1))#thumbnails FILES
xbmcgui.Window(10000).setProperty('str(folders1)', str(folders1))#thumbnails FOLDERS
xbmcgui.Window(10000).setProperty('str(files2)', str(files2))#addons FILES
xbmcgui.Window(10000).setProperty('str(folders2)', str(folders2))#addons FOLDERS





