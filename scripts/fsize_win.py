import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, string
import re
import time
import shutil

try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = xbmc.translatePath

packagesdir = translatePath(os.path.join('special://home/addons/packages',''))
thumbnails1 = translatePath(os.path.join('special://thumbnails',''))
cache       = translatePath(os.path.join('special://home/cache',''))
kodi        = translatePath(os.path.join('special://home/',''))
thumbnails  = translatePath('special://thumbnails')
#Disk_C      = translatePath(os.path.join('C:', ''))
addondata   = translatePath('special://home/userdata/addon_data')
addons      = translatePath('special://home/addons')
temp        = translatePath('special://home/addons/temp')
database    = translatePath('special://database')
purgePath   = translatePath('special://home/addons/packages')

folder      = 'C:'
#folder1     = 'D:'



#total_size12 = 0
total_size11 = 0
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
files3 = folders3 = 0

BytesPerGiB = 1000 * 1000 * 1000
gb = 1024 * 1024 * 1024

for dirpath, dirnames, filenames in os.walk(packagesdir):
    count = 0
    for f in filenames:
        count += 1
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)
total_sizetext = "%.2f GiB" % (total_size/BytesPerGiB)

for dirpath2, dirnames2, filenames2 in os.walk(thumbnails):
    for f2 in filenames2:
        fp2 = os.path.join(dirpath2, f2)
        total_size2 += os.path.getsize(fp2)
total_sizetext2 = "%.2f GiB" % (total_size2/BytesPerGiB)

for dirpath3, dirnames3, filenames3 in os.walk(addondata):
    for f3 in filenames3:
        fp3 = os.path.join(dirpath3, f3)
        total_size3 += os.path.getsize(fp3)
total_sizetext3 = "%.2f GiB" % (total_size3/BytesPerGiB)

for dirpath4, dirnames4, filenames4 in os.walk(database):
    for f4 in filenames4:
        fp4 = os.path.join(dirpath4, f4)
        total_size4 += os.path.getsize(fp4)
total_sizetext4 = "%.2f GiB" % (total_size4/BytesPerGiB)

for dirpath5, dirnames5, filenames5 in os.walk(addons):
    for f5 in filenames5:
        fp5 = os.path.join(dirpath5, f5)
        total_size5 += os.path.getsize(fp5)
total_sizetext5 = "%.2f GiB" % (total_size5/BytesPerGiB)

for dirpath6, dirnames6, filenames6 in os.walk(temp):
    for f6 in filenames6:
        fp6 = os.path.join(dirpath6, f6)
        total_size6 += os.path.getsize(fp6)
total_sizetext6 = "%.2f GiB" % (total_size6/BytesPerGiB)

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
        
for dirpath10, dirnames10, filenames10 in os.walk(kodi):
  # ^ this idiom means "we won't be using this value"
        files3 += len(filenames10)
        folders3 += len(dirnames10)      

for dirpath10, dirnames10, filenames10 in os.walk(cache):
    for f10 in filenames10:
        fp10 = os.path.join(dirpath10, f10)
        total_size10 += os.path.getsize(fp10)
total_sizetext10 = "%.2f GiB" % (total_size10/BytesPerGiB)

for dirpath11, dirnames11, filenames11 in os.walk(kodi):
    for f11 in filenames11:
        fp11 = os.path.join(dirpath11, f11)
        total_size11 += os.path.getsize(fp11)
total_sizetext11 = "%.2f GiB" % (total_size11/BytesPerGiB)

#for dirpath12, dirnames12, filenames12 in os.walk(Disk_C):
#    for f12 in filenames12:
#        fp12 = os.path.join(dirpath12, f12)
#        total_size12 += os.path.getsize(fp12)
#total_sizetext12 = "%.2f GiB" % (total_size12/BytesPerGiB)

available_drives = [('[B]''%s:''[/B]' % d)
    for d in string.ascii_uppercase
if os.path.exists('%s:' % d)]


total_mem, used_mem, free_mem = shutil.disk_usage(folder)
print('Folder {}' .  format(folder))

total_mem = 'C://\r\n'+'Total Mem:' + '[B]'" %.2f GiB"'[/B]' % (total_mem/gb)
used_mem = 'Used Mem:' + '[B]'" %.2f GiB"'[/B]' % (used_mem/gb)
free_mem = 'Free Mem:' + '[B]'" %.2f GiB"'[/B]\n' % (free_mem/gb)
#total_mem1, used_mem1, free_mem1 = shutil.disk_usage(folder1)
#print('Folder1 {}' .  format(folder1))
#total_mem1 = 'D://\r\n'+'Total Mem1:' + '[B]'" %.2f GiB"'[/B]' % (total_mem1/gb)
#used_mem1 = 'Used Mem:' + '[B]'" %.2f GiB"'[/B]' % (used_mem1/gb)
#free_mem1 = 'Free Mem:' + '[B]'" %.2f GiB"'[/B]' % (free_mem1/gb)

#xbmcgui.Window(10000).setProperty('str(available_drives)', str(available_drives).replace("'", "").replace(":", "://")+'\r\n')
xbmcgui.Window(10000).setProperty('str(free_mem)', str(free_mem))
xbmcgui.Window(10000).setProperty('str(total_mem)', str(total_mem))
xbmcgui.Window(10000).setProperty('str(used_mem)', str(used_mem))
#xbmcgui.Window(10000).setProperty('str(free_mem1)', str(free_mem1))
#xbmcgui.Window(10000).setProperty('str(total_mem1)', str(total_mem1))
#xbmcgui.Window(10000).setProperty('str(used_mem1)', str(used_mem1))
xbmcgui.Window(10000).setProperty('total_sizetext', total_sizetext)#packagesdir SIZE
xbmcgui.Window(10000).setProperty('total_sizetext2', total_sizetext2)#thumbnails SIZE
xbmcgui.Window(10000).setProperty('total_sizetext3', total_sizetext3)#addondata SIZE
xbmcgui.Window(10000).setProperty('total_sizetext4', total_sizetext4)#database SIZE
xbmcgui.Window(10000).setProperty('total_sizetext5', total_sizetext5)#addons SIZE
xbmcgui.Window(10000).setProperty('total_sizetext6', total_sizetext6)#temp SIZE
xbmcgui.Window(10000).setProperty('total_sizetext10', total_sizetext10)#CACHE SIZE
xbmcgui.Window(10000).setProperty('total_sizetext11', total_sizetext11)#KODI SIZE
#xbmcgui.Window(10000).setProperty('total_sizetext12', "[B]C:// " + total_sizetext12 + "[/B]")#Disk_C SIZE
xbmcgui.Window(10000).setProperty('str(count)', str(count))#packages FILES
xbmcgui.Window(10000).setProperty('str(files)', str(files))#addondata FILES
xbmcgui.Window(10000).setProperty('str(folders)', str(folders))#addondata FOLDERS
xbmcgui.Window(10000).setProperty('str(files1)', str(files1))#thumbnails FILES
xbmcgui.Window(10000).setProperty('str(folders1)', str(folders1))#thumbnails FOLDERS
xbmcgui.Window(10000).setProperty('str(files2)', str(files2))#addons FILES
xbmcgui.Window(10000).setProperty('str(folders2)', str(folders2))#addons FOLDERS
xbmcgui.Window(10000).setProperty('str(files3)', str(files3))#addons FILES
xbmcgui.Window(10000).setProperty('str(folders3)', str(folders3))#addons FOLDERS





