import os
# import pdb
import time
zaman = time.time()
src = r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\from my phone\WhatsApp Voice Notes"
dst = r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\from my phone\WhatsApp_Voice_Notes"
say = 0
for i in os.listdir(src):
	yol = src+"\\"+i
	for k in os.listdir(yol):
		if k[-4:] == 'opus':
			# pdb.set_trace()
			text='ffmpeg -i "{}\{}" "{}\{}".mp3'.format(yol,k,dst,k[:-5])
			os.system(text)
			say += 1
print('\nGEÇEN SÜRE: ',time.time()-zaman)