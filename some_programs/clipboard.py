import ctypes
from pytube import YouTube as yt
def winGetClipboard():
	ctypes.windll.user32.OpenClipboard(0)
	pcontents = ctypes.windll.user32.GetClipboardData(13) # CF_UNICODETEXT
	data = ctypes.c_wchar_p(pcontents).value
	ctypes.windll.user32.CloseClipboard()
	return data

vid = yt(winGetClipboard())
all_types = vid.streams.all()
size_listesi = []
for i in range(len(all_types)):
	size_listesi.append(round(all_types[i].filesize/1024/1024,1))
for i,k in zip(size_listesi,range(1,len(all_types)-1,2)):
	all_types.insert(k,i)
print(*all_types,sep='\n')
print('\nTitle: ',vid.title)
print('\nViews: ',vid.views)
try:
	print('\nLength: ',vid.length)
except:
	pass
if input('Do you like to download this video? (y/n): ') == 'y':
	inp = input('Enter the video sırası which you want to download: (0,1,2,...)')
	vid.streams.all()[int(inp)].download()
else:
	pass

# to be extended such that when a link is copied, automatcially its info is displayed on the bottom right of the screen.	
	