import psutil,time
eski_d = 0
eski_t = 0
while True:
	upload = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][0]
	download = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][1]
	# upload = psutil.net_io_counters(pernic=True)['Yerel Ağ Bağlantısı 7'][0]
	# download = psutil.net_io_counters(pernic=True)['Yerel Ağ Bağlantısı 7'][1]
	bas = time.time()
	print('download rate: ',(download-eski_d)/(bas - eski_t))
	print('upload: '+str(round(upload/1024/1024,2))+' MB'+'\n'+'download: '+str(round(download/1024/1024,2))+' MB\n')
	eski_d = download
	eski_t = bas
	time.sleep(1)