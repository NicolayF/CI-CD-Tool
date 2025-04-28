import psutil
import sys
from datetime import datetime

def log(message):
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def monitor_system():
    ## Uso de CPU
    cpu = psutil.cpu_percent(interval=1)
    ## Uso de RAM
    ram = psutil.virtual_memory().percent

    log(f"CPU: {cpu}%, RAM: {ram}%")

    if cpu > 80 or ram > 80:
        log("Alerta: Uso de sistema.")
        return False
    return True

if __name__ == "__main__":
    ## En caso de Alerta retorna error.
    if not monitor_system():
        sys.exit(1)