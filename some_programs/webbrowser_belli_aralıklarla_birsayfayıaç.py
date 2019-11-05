import webbrowser
import time
count = 4
link = r"C:\Users\emre\Desktop"
while count > 3:
    time.sleep(10)
    webbrowser.open(link)
    count -= 1
    
