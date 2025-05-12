import psutil
import time
import os
from tabulate import tabulate
import csv
# Thresholds for suspicious processes
CPU_THRESHOLD = 50.0
MEMORY_THRESHOLD_MB = 500
SUSPICIOUS_NAMES = {"svch0st.exe", "backdoor.exe", "rat.exe", "keylogger.exe"}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    =======================
    Local Threat Analyzer
    =======================
    Real-Time System Monitoring
    """
    print(banner)

def get_process_info():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'exe']):
        try:
            info = proc.info
            pid = info['pid']
            name = info['name']
            cpu = info['cpu_percent']
            mem_mb = round(info['memory_info'].rss / (1024 * 1024), 2)
            path = info['exe'] if info['exe'] else "N/A"

            is_suspicious = (
                cpu > CPU_THRESHOLD or
                mem_mb > MEMORY_THRESHOLD_MB or
                path == "N/A" or
                name.lower() in SUSPICIOUS_NAMES
            )

            process_list.append([
                pid,
                name,
                f"{cpu}%",
                f"{mem_mb} MB",
                path if path != "N/A" else "Unknown",
                "SUSPICIOUS" if is_suspicious else "Normal"
            ])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_list


def log_suspicious_process(info_list):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"suspicious_log_{timestamp}.csv"
    
    with open(log_file, 'w', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(["PID", "Name", "CPU%", "Memory (MB)", "Path", "Status", "Timestamp"])
        for process in info_list:
            log_writer.writerow(process + [timestamp])
    
    print(f"\nSuspicious processes logged to {log_file}\n")


def display_loop(refresh_interval=5):
    while True:
        clear_screen()
        print_banner()
        processes = get_process_info()
        headers = ["PID", "Name", "CPU%", "Memory (MB)", "Path", "Status"]
        print(tabulate(processes, headers=headers, tablefmt="simple"))
        print(f"\nUpdating in {refresh_interval}s... (Ctrl+C to exit)\n")
        suspicious_only = [p[:-1] for p in processes if p[-1] == "SUSPICIOUS"]
        if suspicious_only:
            log_suspicious_process(suspicious_only)
        time.sleep(refresh_interval)

if __name__ == "__main__":
    try:
        display_loop(refresh_interval=60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
