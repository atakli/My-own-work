import tkinter as tk
import time
import clipboardtan_vidyo_indir_main_ as ib
root = tk.Tk()
root.withdraw()
f = open(r"C:\Users\emre\Desktop\miscallaneous\python\muhtelif_yardımcı_dosyalar\clipboard_vidyo_log.txt","a")

while 1:   
	a=root.clipboard_get()
	time.sleep(0.1)
	b=root.clipboard_get()
	if not b == a and "youtu" in b:
		ib.start(b)
	if not b == a:
		print(b,file=f)
		#print(b)
	elif b == 'son':
		break
f.close()
