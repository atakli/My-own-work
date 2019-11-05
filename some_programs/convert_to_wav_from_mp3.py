import os
from pydub import AudioSegment
os.chdir('C:\\Users\\emre\\desktop')
# files                                                                         
src = "hulasa.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
