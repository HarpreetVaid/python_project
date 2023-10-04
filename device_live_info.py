import matplotlib.pyplot as plt
import system_hardware_info
import system_live_info
from matplotlib.animation import FuncAnimation
import random

data = 0

# Initialize lists to store historical data for CPU frequency and RAM
cpu_freq = []
ram_usage = []
parition = []

hardware_info = system_hardware_info.get_hardware_info()
for keys in hardware_info['partition']:
     parition.append(keys)

# Create two subplots (2 rows, 2 columns)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Initialize empty lists for data
x_data = []
y_data1 = []
y_data2 = []

# Function to generate random data (replace with actual data retrieval)
def generate_random_data():
    return [random.randint(0, 100) for _ in range(2)]
def update_data(i):
    live_info = system_live_info.get_live_info()  # Replace with actual data retrieval
    global data
    if data > 15:
        cpu_freq.pop(0)
        ram_usage.pop(0)

    data += 1

    # Update CPU frequency and RAM data
    cpu_freq.append(live_info['cpu_info']['cpu_usage'])
    ram_usage.append(live_info['used_ram'])

    # Limit the data to show only the last N points
    max_points = 10
    if len(cpu_freq) > max_points:
        cpu_freq.pop(0)
        ram_usage.pop(0)

    # Append new data to x_data, y_data1, and y_data2
    x_data.append(data)  # Use the 'data' variable as x-axis value
    y_data1.append(float(live_info['cpu_info']['cpu_usage']))  # Update with the actual CPU data
    y_data2.append(float(live_info['used_ram']))  # Update with the actual RAM data

    # Update the line plots
    ax1.clear()
    ax1.plot(x_data, y_data1, marker=None)
    ax1.set_title('CPU Usage')
    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('Y-axis')

    ax2.clear()
    ax2.plot(x_data, y_data2, marker=None)
    ax2.set_title('RAM Usage')
    ax2.set_xlabel('X-axis')
    ax2.set_ylabel('Y-axis')
    # Generate random data for the pie charts (replace with actual data)
    data1 =[hardware_info['partition'][parition[0]],live_info['partition'][parition[0]]]
    data2 = [hardware_info['partition'][parition[1]],live_info['partition'][parition[1]]]

    # Update the pie charts with appropriate labels
    ax3.clear()
    ax3.pie(data1, labels=['Used', 'Unused'], autopct='%1.1f%%', startangle=45)
    ax3.set_title(parition[0])

    ax4.clear()
    ax4.pie(data2, labels=['Used', 'Unused'], autopct='%1.1f%%', startangle=45)
    ax4.set_title(parition[1])

# Create an animation to update the plots
ani = FuncAnimation(fig, update_data, interval=1000, save_count=10)  # Update every 1 second

# Hide x and y axis tick labels (showing none)
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_xticks([])  # Remove x-axis tick marks
    ax.set_yticks([])# Remove y-axis tick marks
    
# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()