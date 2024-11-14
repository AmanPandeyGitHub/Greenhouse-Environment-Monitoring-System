import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

plt.style.use('seaborn-v0_8')

fig, ((T_screen, H_screen), (L_screen, S_screen)) = plt.subplots(nrows=2, ncols=2)

def animate(i):
    data = pd.read_csv('data.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['seconds'] = (data['timestamp'] - data['timestamp'].min()).dt.total_seconds()

    x = data['seconds']
    y1 = data['temperature']
    y2 = data['humidity']
    y3 = data['ldr_value']
    y4 = data['soil_moisture']  

    if len(x) > 8:
        x = x.iloc[-8:]
        y1 = y1.iloc[-8:]
        y2 = y2.iloc[-8:]
        y3 = y3.iloc[-8:]
        y4 = y4.iloc[-8:]

    T_screen.cla()
    H_screen.cla()
    L_screen.cla()
    S_screen.cla()
    T_screen.plot(x, y1, color='r', marker=".", linewidth=0.7)
    H_screen.plot(x, y2, color='b', marker=".", linewidth=0.7)
    L_screen.plot(x, y3, color='g', marker=".", linewidth=0.7)
    S_screen.plot(x, y4, color='k', marker=".", linewidth=0.7)

    T_screen.set_title('Temperature')
    T_screen.set_xlabel('Time (Seconds)')
    T_screen.set_ylabel('Celsius')

    H_screen.set_title('Humidity')
    H_screen.set_xlabel('Time (Seconds)')
    H_screen.set_ylabel('Humidity %')

    L_screen.set_title('LDR Value')
    L_screen.set_xlabel('Time (Seconds)')
    L_screen.set_ylabel('Discharge Time (Seconds)')

    S_screen.set_title('Soil Moisture')
    S_screen.set_xlabel('Time (Seconds)')
    S_screen.set_ylabel('Discharge Time (Seconds)')

    plt.tight_layout()

ani = FuncAnimation(fig, animate, interval=1000, save_count=50)

plt.show()
