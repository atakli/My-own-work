import psutil
upload = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][0]
download = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][1]
print('upload: '+str(round(upload/1024/1024,2))+' MB'+'\n'+'download: '+str(round(download/1024/1024,2))+' MB')
print()