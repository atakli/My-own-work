import os
link = "C:/Users/emre/Desktop/opencv/videos - opencv"
for i in os.listdir(link):
    k=1
    for j in range(21):
        if i.endswith(" "+str(j+1)+".mp4"):
            os.rename(link+'/'+i,link+'/'+str(k)+") "+i)
        else: k+=1
