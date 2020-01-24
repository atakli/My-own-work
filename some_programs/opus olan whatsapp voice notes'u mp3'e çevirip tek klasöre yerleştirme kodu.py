import os
import pdb
import time
zaman = time.time()
src = r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\phone 9.10.19\Media\WhatsApp Voice Notes"
dst = r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\phone 9.10.19\Media\WhatsApp Voice Notes"
say = 0
for i in os.listdir(src):
	yol = src+"\\"+i
	for k in os.listdir(yol):
		if k[-4:] == 'opus':
			text='ffmpeg -i "{}\{}" "{}\{}.mp3"'.format(yol,k,dst,k[:-5])
			# pdb.set_trace()
			os.system(text)
			say += 1
print('\nGEÇEN SÜRE: ',time.time()-zaman)