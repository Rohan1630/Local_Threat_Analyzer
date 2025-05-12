# Local Threat Analyzer

**Local Threat Analyzer** is a system monitoring tool designed to detect suspicious processes running on your local machine. It monitors CPU, memory usage, and known malicious processes or signatures. The tool provides real-time monitoring and logs suspicious activities for analysis.

---

## Features
- **Real-time monitoring** of running processes.
- **Log suspicious processes** in a **CSV** format with timestamps.
- Detect processes with **high CPU or memory usage**.
- Check processes against **known malware signatures**.
- Option to run as an **executable** for easier use.

---

## Requirements

- **Python 3.x**
- Required Python libraries:
    - `psutil` - For fetching system processes.
    - `tabulate` - For neat table formatting.
    - `csv` - For CSV log output.

You can install the required libraries using `pip`:

```bash
pip install psutil tabulate
```

---

## How to Use

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/local-threat-analyzer.git
cd local-threat-analyzer
```

### 2. **Run the Tool**

You can either run the tool in real-time or execute a one-time scan.

- **One-time scan** (Displays all running processes with their usage and status):
    ```bash
    python process_monitor.py
    ```

- **Real-time monitoring** (Monitors and updates every few seconds):
    ```bash
    python process_monitor.py --real-time
    ```

#### Options
- The tool will log suspicious processes (those exceeding CPU/memory thresholds or matching known signatures) into a **CSV file**. These logs will be saved with the timestamp as the file name, e.g., `suspicious_log_2025-04-29_10-25-15.csv`.
  
- **Malware Signature Scanning**: Matches running processes with known malicious file signatures. You can customize the list of signatures in the code (`MALWARE_SIGNATURES`).

### 3. **Real-Time Monitoring Output**
Once running, the tool will display the following information about each process:
- **PID**: Process ID.
- **Name**: Process name.
- **CPU%**: Percentage of CPU usage.
- **Memory (MB)**: Memory usage in MB.
- **Path**: Path to the executable.
- **Status**: Marked as either "Normal" or "SUSPICIOUS" based on defined thresholds.

### 4. **Log Files**
Suspicious processes will be logged in CSV format, including the following fields:
- **PID**: Process ID.
- **Name**: Process name.
- **CPU%**: CPU usage percentage.
- **Memory (MB)**: Memory usage in MB.
- **Path**: Path to the executable.
- **Status**: "SUSPICIOUS" if the process exceeds threshold values or matches a known malware signature.
- **Timestamp**: When the log was generated.

Example log entry:
```
PID,Name,CPU%,Memory (MB),Path,Status,Timestamp
5678,backdoor.exe,75%,250 MB,C:/...,SUSPICIOUS,2025-04-29_10-25-15
9102,explorer.exe,12%,100 MB,C:/...,Normal,2025-04-29_10-25-15
```

---

## Customization

### 1. **CPU and Memory Thresholds**
You can adjust the **CPU** and **Memory** usage thresholds for marking a process as suspicious by changing the following values in the code:
```python
CPU_THRESHOLD = 50.0  # CPU usage threshold in percentage
MEMORY_THRESHOLD_MB = 500  # Memory usage threshold in MB
```

### 2. **Malware Signature List**
The tool can detect known malware signatures by comparing the hashes of running processes to a predefined list. Add your known signatures to the `MALWARE_SIGNATURES` list:
```python
MALWARE_SIGNATURES = {"5d41402abc4b2a76b9719d911017c592", "c1d3f8f97e126bb046a78b3401d7fd5b"}
```

### 3. **Log Output Format**
The suspicious process logs are output in **CSV** format. You can modify the logging behavior or output format by adjusting the `log_suspicious_process` function.

---

## Running as an Executable

You can package this tool as a standalone **Windows executable** using `PyInstaller`. Here's how to do it:

1. **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2. **Build the executable**:
    ```bash
    pyinstaller --onefile --console process_monitor.py
    ```

3. The `.exe` will be located in the `/dist` folder. You can now run the tool directly without needing Python installed.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
