import os
import subprocess
import signal

def get_core_count():
    return os.cpu_count()

def start_stress_test(binary_path, count):
    processes = []
    for _ in range(count):
        proc = subprocess.Popen([binary_path])
        processes.append(proc)
    return processes

def stop_stress_test(processes):
    for proc in processes:
        proc.send_signal(signal.SIGINT)
        proc.wait()
