from pytube import YouTube as yt
k = open('hatalilar.txt','w')
with open('indir_ihsan.txt') as f:
	l = f.readlines()
for i in l:
	try:
		yt(i[:-1]).streams.first().download()
	except:
		k.write('\n'+i)		# indiremediğini ayrı bi dosyaya yaz sonra elle indiririm
		pass			# yoksa continue mu olacak bilemedim. ama bence farketmez
k.close()