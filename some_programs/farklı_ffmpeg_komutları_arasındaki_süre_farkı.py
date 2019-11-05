import time,os
os.chdir(r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\from my phone\SOUNDS")
a=time.time()
# os.system("""ffmpeg -i "İsmet Abi & Şevki Abi Hatıra.aac" -acodec libmp3lame son.mp3""")
os.system("""ffmpeg -i "İsmet Abi & Şevki Abi Hatıra.aac" "İsmet Abi & Şevki Abi Hatıra.mp3" """) # niyeyse yapmıyo bunu, kesiliyo
b=time.time()
c=b-a
print("{} dakika, {} saniye".format((c//60),(c%60)))
# d=time.time()
# os.system("ffmpeg -i yeni_test.wav -vn -f mp3 son1.mp3")
# e=time.time()
# f=e-d
# print("{} dakika, {} saniye".format((f//60),(f%60)))
# g=time.time()
# os.system("ffmpeg -i yeni_test.wav -f mp3 son2.mp3")
# h=time.time()
# k=h-g
# print("{} dakika, {} saniye".format((k//60),(k%60)))
18 MB'lıkı ses amr'ye çevirince 4 buçuğa indi
direk amr'ye çevirmeye kalkınca hata verdi, iki parametre ekledim düzeldi:
ffmpeg -i "son sınıf dersi zeki abi.3gp" -ar 8000 -ab 12.2k "son sınıf dersi zeki abi.amr"