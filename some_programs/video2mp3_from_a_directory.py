import os
src = r"/media/emre/Packard Bell/Users/deneme"
dst = r"/media/emre/Packard Bell/Users/deneme_out"
os.chdir(src)
for i in os.listdir():
	text='ffmpeg -i "{}" -f mp3 "{}\{}".mp3'.format(i,dst,i[:-4])
	os.system(text)
# ffmpeg komutunu cmd'de penceresiz çalıştırmayı aradım ama bulamadım (-hide_banner diye bişey var ama anlamadım)
# edit: pythonw ile çalıştırınca olmuyo mu işte
# 		ayrıca mp3'e çevirmek için o kadar kod gerekmiyodu sanki
# edit: evet -f mp3'e gerek yok. -f mp3 diye bişey varsa output'u .mp3 uzantısı olmadan yazabilmem lazım, halbuki onu yazmayınca
# uzantısız oluşturuyo dosyayı, sonra elle uzantıyı yazmam gerekiyo
