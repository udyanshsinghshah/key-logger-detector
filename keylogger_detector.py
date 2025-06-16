import psutil
import time

# Define some keywords that are often used by keyloggers
keylogger_keywords = ["keylogger", "keyboard", "pynput", "hook", "capture"]

def scan_processes():
    print("\n🔍 Scanning processes for suspicious activity...\n")
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name'].lower()
            for keyword in keylogger_keywords:
                if keyword in process_name:
                    found = True
                    print(f"⚠️  Suspicious process found: {process_name} (PID: {proc.info['pid']})")
                    ask = input("❓ Do you want to terminate this process? (y/n): ")
                    if ask.lower() == 'y':
                        psutil.Process(proc.info['pid']).terminate()
                        print("✅ Process terminated.\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    if not found:
        print("✅ No suspicious processes found.")

if __name__ == "__main__":
    while True:
        scan_processes()
        time.sleep(10)  # Scan every 10 seconds
