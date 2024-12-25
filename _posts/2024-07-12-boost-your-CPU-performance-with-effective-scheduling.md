---
title: 'Solved: Boost Your CPU Performance with Effective Scheduling'
date: 2024-07-12
comments: true
tags:
    - CPU Performance
    - Scheduling
    - Linux
    - Kernel
    - RK3588
    - Optimization

---

This guide provides techniques to optimize CPU performance on the CPU by adjusting scheduling parameters and thresholds.

## Problem
Ever wondered how your operating system decides which tasks get CPU time? This process, known as CPU scheduling, is crucial for optimizing system efficiency and resource utilization. By fine-tuning this process, you can significantly enhance your system's performance.

For more insights on understanding CPU scheduling, check out these resources:
- [CPU Scheduling in Operating Systems](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/)
- [Scheduling Period](https://www.sciencedirect.com/topics/computer-science/scheduling-period)

## Solution
In this guide, we'll explore how to improve CPU performance using scheduling techniques on the RK3588 SoC from Rockchip. This SoC features Big and Little Core scheduling, and by adjusting the scheduling period, you can boost overall performance. These methods are applicable to most Linux-based SoCs.

## CPU Performance Optimization

The CPU load sampling time affects the responsiveness of CPU frequency scaling and Big/Little core scheduling. The default system configuration is 32ms, which you can verify with:

### Set CPU Load Sampling Time
```bash
# cat /proc/sys/kernel/sched_pelt_period
32
```
**You can adjust the sampling time to either 32ms or 8ms. Setting it to 8ms makes CPU load frequency scaling and core scheduling more responsive, though it may increase power consumption. Use the following command to set it:**

```bash
# echo 8 > /proc/sys/kernel/sched_pelt_period
```

To modify this setting in the code, follow these steps:

```bash
device/rockchip/rk3588$ diff --git a/init.rk3588.rc b/init.rk3588.rc
index dcac552..e3f0005 100644
--- a/init.rk3588.rc
+++ b/init.rk3588.rc
@@ -56,6 +56,9 @@ on boot
    write /dev/cpuset/background/cpus 0-7
    write /dev/cpuset/system-background/cpus 0-7
    write /dev/cpuset/top-app/cpus 4-7
+
+   # Set CPU sampling time to 8ms, default value is 32ms
+   write /proc/sys/kernel/sched_pelt_period 8
```

### Set Threshold for Big/Little Core Switching

To adjust the threshold for Big/Little core switching, you'll need to modify the kernel code as follows:

```bash
--- a/kernel/sched/fair.c
+++ b/kernel/sched/fair.c
@@ -117,7 +117,7 @@ int __weak arch_asym_cpu_priority(int cpu)
    * (default: ~20%)
 */
-#define fits_capacity(cap, max)    ((cap) * 1280 < (max) * 1024)
+#define fits_capacity(cap, max)    ((cap) * 2048 < (max) * 1024)
```

This parameter determines when a task should switch from a small core to a big core. For example, a value of 1024/1280 means tasks switch at an 80% load threshold, while 1024/2048 means tasks switch at a 50% load threshold.

By implementing these changes, you can achieve a more responsive and efficient CPU performance, tailored to your specific needs. Happy optimizing!