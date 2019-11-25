import pystray,sys,webbrowser
from pystray import Menu, MenuItem
from PIL import Image, ImageDraw
logintext = "Login"
state = False
state1 = False
state2 = False
def net_alisverisi():
	while 1:
		upload = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][0]
		download = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][1]
		time.sleep(3)
	# print('upload: '+str(round(upload/1024/1024,2))+' MB'+'\n'+'download: '+str(round(download/1024/1024,2))+' MB')
def create_image():
	color2 = 1
	# Generate an image and draw a pattern
	(width, height) = (100,100)
	image = Image.new('RGB', (width, height))#, color1)
	dc = ImageDraw.Draw(image)
	dc.rectangle(
		(width // 2, 0, width, height // 2),
		fill=color2)
	dc.rectangle(
		(0, height // 2, width // 2, height),
		fill=color2)

	return image
def on_monitor(icon, item):
	global state,logintext
	state = not item.checked
	url = 'www.youtube.com'
	# webbrowser.open_new_tab(url + '?i=' + str(uuid.uuid4()) )
	webbrowser.open_new_tab(url)
	print("Waiting for login to complete")
	logintext = "Logout"
	print("Logged In",icon.update_menu())
def on_settings(icon, item):
	global state
	state = not item.checked
def on_sync(icon, item):
	global state1
	state1 = not item.checked
def on_exit(icon, item):
	global state2
	state2 = not item.checked
	if state2 == False:
		sys.exit()
icon = pystray.Icon('Sample',create_image(),title="Icons",menu=Menu(
	MenuItem(lambda text: logintext,on_monitor),
	MenuItem('Settings',on_settings),
	MenuItem('Sync',on_sync,checked=lambda item: state1),
	MenuItem('Exit',on_exit,checked=lambda item: state2)))
icon.run()

# icon.icon = create_image()
# icon.visible = True
# icon.run(net_alisverisi())