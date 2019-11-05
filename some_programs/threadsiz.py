import urllib
from time import time
import progressbar
pbar = progressbar.ProgressBar()
siteler = ("http://www.python.org",
           "http://yasararabaci.tumblr.com",
           "http://metehan.us",
           "http://blog.tanshaydar.com",
           "http://fatihmertdogancan.wordpress.com",
           "http://ozgurerdogdu.blogspot.com/"
		   )

start = time()

for site in pbar(siteler):
    f = urllib.urlopen(site)
    _ = f.read() # okudugum veriyi goz ardi ediyorum, bu ornekte gerek yok.
    f.close()
print "%f saniye surdu" % (time() - start)
# 8.600000 saniye surdu