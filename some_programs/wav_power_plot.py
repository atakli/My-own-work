import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as siw
rate,audData=siw.read(r"C:\users\emre\desktop\test.wav")
#create a time variable in seconds
time = np.arange(0, float(audData[0:1000000].shape[0]), 1) / rate
channel1 = audData[0:1000000,0]     # left
channel2 = audData[0:1000000,1]     # right
#plot amplitude (or loudness) over time
plt.figure(1)
plt.subplot(211)
plt.plot(time, channel1, linewidth=0.05, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(time, channel2, linewidth=0.05, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# channel1 ve channel2'nun direk amplitude vermesini anlayamadım. frekans meselesi nerede?