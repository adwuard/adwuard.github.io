---
title: 'Thermal and Performance Profiling Your System'
date: 2024-03-12
comments: true
tags:
    - Thermal
    - Linux
    - Python
    - Toolbox
    - Embeded
    - Hardware
---


Profiling is an essential technique for assessing software application performance. It provides detailed insights into various aspects, such as function call frequency, routine execution times, and the duration spent in different code segments. This information helps identify performance bottlenecks and inefficient sections, enabling effective improvements.

In this guide, we will focus on measuring the relationship between performance and thermal metrics. This approach helps us understand the impact of system load on thermal performance, which is crucial for developing reliable products. By understanding how thermal performance changes over time, we can make informed decisions to improve system reliability.

There are numerous profiling tools available, including summary and sampling-based tools like `perf`. Some tools also provide a UI for visualization. However, for this guide, we will use Python scripts to quickly achieve thermal logging and gain insights into thermal changes over time.

The objective is to log all critical data into a single CSV file, which can later be processed using Python's `matplotlib`. The two provided Python scripts are minimal and require few tools or dependencies.

# The Logger
This script records temperature and CPU frequency changes every second. Note that the specific thermal nodes and CPU frequency nodes may vary depending on your hardware and system drivers. Ensure you adjust the script accordingly to match your system's configuration.

## Usage
Run the following logger on your target machine:
```shell
python {path_to_script}/thermal_logger.py
```

It logs to the `/tmp` folder:
```
/tmp/temperature_curve{date_and_time}.csv
```

### thermal_logger.py
```python
#!/usr/bin/env python3
import os
import time

def get_cpu_usage():
        output = os.popen('top -bn1').read()
        cpu_line = [line for line in output.split('\n') if 'Cpu(s)' in line][0]
        cpu_usage = 100 - float(cpu_line.split()[7].strip('%id,'))
        return round(cpu_usage, 2)

def get_cpu_thermal(zone):
        thermal_file = f"/sys/class/thermal/thermal_zone{zone}/temp"
        with open(thermal_file) as file:
                thermal_temp = int(file.read().strip())
        return round(thermal_temp / 1000, 1)

def get_s1_cpu_frequency():
        with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") as file:
                frequency = int(file.read().strip())
        return round(frequency / 1000000, 2)

def get_s2_cpu_frequency():
        with open("/sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq") as file:
                frequency = int(file.read().strip())
        return round(frequency / 1000000, 2)

def get_l1_cpu_frequency():
        with open("/sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq") as file:
                frequency = int(file.read().strip())
        return round(frequency / 1000000, 2)

def get_l2_cpu_frequency():
        with open("/sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq") as file:
                frequency = int(file.read().strip())
        return round(frequency / 1000000, 2)

def get_gpu_usage_and_frequency():
        with open("/sys/class/devfreq/fb000000.gpu/load") as file:
                gpu_info = file.read().strip('Hz\n').split('@')
        return round(int(gpu_info[0]), 2), round(int(gpu_info[1])/1000000000, 2)

def main():
        filename = "/tmp/temperature_curve" + time.strftime('-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".csv"
        print("Saving thermal log to:")
        print(filename)

        header = (
                "Timestamp,CPU Usage(%),CPU Bigcore Thermal(C),CPU Littlecore Thermal(C),"
                "GPU Thermal(C),NPU Thermal(C),CPU L1-Core Frequency(GHZ),CPU L2-Core Frequency(GHZ),"
                "CPU S1-Core Frequency(GHZ),CPU S2-Core Frequency(GHZ),GPU Usage(%),GPU Frequency(GHZ),"
                "NPU Frequency(GHZ),NPU1 Usage(%),NPU2 Usage(%),NPU3 Usage(%)"
        )

        with open(filename, "w") as file:
                print(header, file=file)
                file.flush()
                while True:
                        try:
                                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                                cpu_usage = get_cpu_usage()
                                cpu_bigcore_thermal = get_cpu_thermal(1)
                                cpu_littlecore_thermal = get_cpu_thermal(3)
                                gpu_thermal = get_cpu_thermal(5)
                                npu_thermal = get_cpu_thermal(6)
                                s1_cpu_frequency = get_s1_cpu_frequency()
                                s2_cpu_frequency = get_s2_cpu_frequency()
                                l1_cpu_frequency = get_l1_cpu_frequency()
                                l2_cpu_frequency = get_l2_cpu_frequency()
                                gpu_usage, gpu_frequency = get_gpu_usage_and_frequency()

                                log_entry = (
                                        f"{timestamp},{cpu_usage:.2f},{cpu_bigcore_thermal:.2f},{cpu_littlecore_thermal:.2f},"
                                        f"{gpu_thermal:.2f},{npu_thermal:.2f},{l1_cpu_frequency:.2f},{l2_cpu_frequency:.2f},"
                                        f"{s1_cpu_frequency:.2f},{s2_cpu_frequency:.2f},{gpu_usage:.2f},{gpu_frequency:.2f},"
                                        f"{npu_frequency:.2f},{npu_usage[0]:.2f},{npu_usage[1]:.2f},{npu_usage[2]:.2f}"
                                )

                                print(log_entry, file=file)
                                file.flush()
                        except Exception as e:
                                print(e)
                        time.sleep(1)

if __name__ == "__main__":
        main()
```

### Captured Data Example
```text
Timestamp,CPU Usage(%),CPU Thermal 0(C),CPU Thermal 1(C),CPU Thermal 2(C),CPU Thermal 3(C),CPU Frequency(GHZ)
2024-04-17 15:56:26,9.30,60.10,60.10,60.10,60.10,0.60
2024-04-17 15:56:28,6.20,60.10,60.10,59.20,60.10,0.41
2024-04-17 15:56:29,6.30,60.10,60.10,60.10,60.10,0.41
.....
```

# Run Your Process to Increase System Load
You can run your desired "load" to increase system usage and temperature. This can be achieved using either a real application or stress testing tools.

Examples of stress tests include:
- CPU stress tests
- Memory stress tests
- GPU stress tests
- I/O stress tests

Alternatively, you can use real applications to generate system load.

## Plot the Data
```shell
python thermal_plot.py {logged_file_name}.csv
```

### thermal_plot.py
```python
import argparse
import os
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

def plot_data(log_path):
        data = pd.read_csv(log_path, parse_dates=['Timestamp'])
        fig, (ax_temperatures, ax_usage, ax_frequency) = plt.subplots(3, 1, figsize=(20, 15))

        # Add text to the plot
        fig.text(0.5, 0.95, "Data Name: "+ str(log_path), ha='center', fontsize=20, fontweight='bold')
        fig.text(0.5, 0.92, "Log Time: "+ str(data['Timestamp'][0]), ha='center', fontsize=20, fontweight='bold')
        
        # Plot CPU temperatures for each core
        ax_temperatures.plot(data['Timestamp'], data['CPU Bigcore Thermal(C)'], label='CPU L1-Core')
        ax_temperatures.plot(data['Timestamp'], data['CPU Littlecore Thermal(C)'], label='CPU S1-Core')
        ax_temperatures.plot(data['Timestamp'], data['GPU Thermal(C)'], label='GPU')
        ax_temperatures.plot(data['Timestamp'], data['NPU Thermal(C)'], label='NPU')
        ax_temperatures.set_ylabel('Temperature (C)')
        ax_temperatures.set_ylim(40, 120)
        ax_temperatures.axhline(y=90, color='orange', linestyle='--', label='High Temp Warning')
        ax_temperatures.axhline(y=115, color='r', linestyle='--', label='Panic Shutdown Temp')
        ax_temperatures.legend()
        ax_temperatures.set_title('CPU Temperatures')

        # Plot CPU usage
        ax_usage.plot(data['Timestamp'], data['CPU Usage(%)'], label='CPU Usage')
        ax_usage.plot(data['Timestamp'], data['GPU Usage(%)'], label='GPU Usage')
        ax_usage.set_ylabel('Usage %')
        ax_usage.set_ylim(0, 105)
        
        # Add dashed line at 80% CPU usage
        ax_usage.axhline(y=80, color='orange', linestyle='--', label='High Load')
        ax_usage.legend()
        ax_usage.set_title('CPU and GPU Usage in %')

        # Smooth CPU frequency using Savitzky-Golay filter
        l1_smoothed_frequency = savgol_filter(data['CPU L1-Core Frequency(GHZ)'], window_length=11, polyorder=3)
        l2_smoothed_frequency = savgol_filter(data['CPU L2-Core Frequency(GHZ)'], window_length=11, polyorder=3)
        s1_smoothed_frequency = savgol_filter(data['CPU S1-Core Frequency(GHZ)'], window_length=11, polyorder=3)
        s2_smoothed_frequency = savgol_filter(data['CPU S2-Core Frequency(GHZ)'], window_length=11, polyorder=3)

        # Plot smoothed CPU frequency
        ax_frequency.plot(data['Timestamp'], l1_smoothed_frequency, label='CPU L1-Core Frequency(GHZ)')
        ax_frequency.plot(data['Timestamp'], l2_smoothed_frequency, label='CPU L2-Core Frequency(GHZ)')
        ax_frequency.plot(data['Timestamp'], s1_smoothed_frequency, label='CPU S1-Core Frequency(GHZ)')
        ax_frequency.plot(data['Timestamp'], s2_smoothed_frequency, label='CPU S2-Core Frequency(GHZ)')
        ax_frequency.plot(data['Timestamp'], data['GPU Frequency(GHZ)'], label='GPU Frequency(GHZ)')
        ax_frequency.axhline(y=0.4, color='r', linestyle='--', label='Thermal Throttle Line')
        ax_frequency.set_ylabel('Frequency (GHz)')
        ax_frequency.legend()
        ax_frequency.set_title('CPU (Large/Small Core) Frequency GHZ')

        # Set y-axis limit to 0Hz to 2GHz
        ax_frequency.set_ylim(0, 3)

        fig.set_size_inches(25, 18)

        # Save the plot as a PNG file
        plot_file_path = os.path.splitext(log_path)[0] + '.png'
        plt.savefig(plot_file_path)

        # Show the plot
        plt.show()

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('log_path', help='Path to the log file')
        args = parser.parse_args()

        try: 
                plot_data(args.log_path)
        except Exception as

    fig.set_size_inches(25, 18)

    # Save the plot as a PNG file
    plot_file_path = os.path.splitext(log_path)[0] + '.png'
    plt.savefig(plot_file_path)

    # Show the plot
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('log_path', help='Path to the log file')
    args = parser.parse_args()

    try: 
        plot_data(args.log_path)
    except Exception as e:
        print("Parse/Plot error:", e)


if __name__ == "__main__":
    main()
```

## Output Plot
The example plot below demonstrates the thermal behavior of the system. Initially, the temperature rises until it reaches the thermal limit. At this point, the frequency is reduced to prevent overheating. 
The plot also shows how the system dissipates heat through passive cooling.

<img src="/images/posts/2024-03-12-thermal-logger/example_plot.png" style="width:100%; margin-right: 10px;">


## Conclusion
This guide demonstrated how to profile your system's thermal and performance characteristics using Python scripts. By logging CPU and GPU usage, thermal metrics, and frequency changes, you can identify performance bottlenecks and improve system reliability. Visualizing the data helps understand the relationship between system load and thermal performance, aiding in heat management and avoiding thermal throttling.

## What's Next:
If your system suffers from throttling, it's advisable to conduct further testing with a power meter. Connect your system to an ammeter to measure power usage and log the power consumption data alongside the thermal metrics. By analyzing the relationship between power usage and thermal performance, you can gain valuable insights to enhance hardware thermal designs and optimize software for better system efficiency.


