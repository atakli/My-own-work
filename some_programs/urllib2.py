import urllib2 as ur
link = 'https://www.fonecope.com/downloads/android-data-recovery.exe'
u=ur.urlopen(link)
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])/1024/1024