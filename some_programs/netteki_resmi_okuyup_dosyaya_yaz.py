import urllib2
helikopter = urllib2.urlopen("http://www.24saatgazetesi.com/wp-content/uploads/2018/07/atak2.jpg").read()
file = open("atak.jpg","w")
file.write(helikopter)
file.close()
################## aşağıdaki de farklı bi implementation:
import random
import urllib.request as ur

def download_web_image(url):
    name = random.randrange(1,10)
    full_name = str(name) + ".jpg"
    ur.urlretrieve(url, full_name)
metin = "https://www.google.com.tr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
download_web_image(metin)
