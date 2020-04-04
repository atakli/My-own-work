import matplotlib.pyplot as plt
import numpy as np
# from statistics import mean
import wave
# import sys
import pickle

fig = plt.figure(1)
# fig, ax = plt.subplots()

class Audio:
	def __init__(self, audio):
		self.audio = wave.open(audio,'r')
		self.signal = self.audio.readframes(-1)
		self.signal = np.fromstring(self.signal, 'Int32')
		# self.fr = self.audio.getframerate()
		self.time = np.linspace(0, 100, num=(len(self.signal)))
		self.fft = np.fft.fft(self.signal)

	def plot(self):
		# i=0
		plt.title("Audio waveforms")
		try:
			# while True:
			# for i in range(135):
			# plt.plot(self.time[i*(100000):(i+1)*(100000)], self.signal[i*(100000):(i+1)*(100000)])#, '.')
			plt.plot(self.time, self.signal)
				# fig.figure()
				# ax.plot(self.time[i*(100000):(i+1)*(100000)], self.signal[i*(100000):(i+1)*(100000)])#, '.')
		# plt.plot(self.time[:len(self.time/2)], self.signal[:len(self.time/2)])#, '.')
		# plt.plot(self.time[len(self.time/2)+1:], self.signal[len(self.time/2)+1:])#, '.')
		# plt.savefig(r'C:\Users\Emre\Desktop\yeni\fft_'+str(i+1)+'.png')
		# plt.savefig(r'C:\Users\Emre\Desktop\fft.png')
				# print(str(i+1)+' tamam')
				# i+=1
		except:
			pass
import wave
import numpy as np
import matplotlib.pyplot as plt
audio = wave.open(r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\religion\Risale-i Nur\sesli dersler\RECORD\Fırat abi\out.wav",'r')
signal = audio.readframes(-1)
signal_32 = np.fromstring(signal, 'Int64')
time = np.linspace(0, 100, num=(len(signal_32)))
plt.plot(time, signal_32)
plt.show()

gana = Audio(r"C:\Users\Emre\Desktop\14.08.09_the_mechanic\religion\Risale-i Nur\sesli dersler\RECORD\Fırat abi\out.wav")
# humm = Audio('humm.wav')

gana.plot()
dosya = open(r'C:\Users\Emre\Desktop\FigureObject.fig.pickle', 'wb')
try:
	pickle.dump(fig,dosya)
except:
	pass
dosya.close()
# humm.plot()
plt.show()
