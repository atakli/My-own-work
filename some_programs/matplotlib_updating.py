import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil,time
# style.use('fivethirtyeight')
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs, ys = [],[]
# Initialize communication with TMP102
# tmp102.init()
# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
	# Read temperature (Celsius) from TMP102
	# temp_c = round(tmp102.read_temp(), 2)
	download = psutil.net_io_counters(pernic=True)['Kablosuz Ağ Bağlantısı'][1]
	# Add x and y to lists
	xs.append(dt.datetime.now().strftime('%H:%M:%S.%f')[:8])
	ys.append(round(download/1024/1024,2))
	# Limit x and y lists to 20 items
	# xs = xs[-20:]
	# ys = ys[-20:]
	# Draw x and y lists
	ax.clear()
	ax.plot(xs, ys)
	# Format plot
	plt.xticks(rotation=45, ha='right')
	ax.xaxis.set_major_locator(plt.MaxNLocator(10))
	plt.subplots_adjust(bottom=0.30)
	plt.title('Internet usage over Time')
	plt.ylabel('Temperature (deg C)')
	plt.tight_layout()
# Set up plot to call animate() function periodically
# bas = time.time()
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
# if time.time() - bas > 10:
	# fig.savefig('10.png')
plt.show()
