import os
import sys
import django
import random
import time

# Absolute path set cheyyunnu
sys.path.append('C:/xampp/htdocs/SmartEnv')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from monitor.models import SensorData

def run_simulation():
    print("Simulation Running...")
    while True:
        temp = round(random.uniform(20.0, 40.0), 2)
        hum = round(random.uniform(30.0, 80.0), 2)
        
        if temp > 35 or hum > 70:
            status = "ALERT"
            temp = -temp
            hum = -hum
            chem = "High Formaldehyde"
        else:
            status = "Safe"
            chem = "Normal Air"

        SensorData.objects.create(temperature=temp, humidity=hum, chemical_type=chem, status=status)
        print(f"Logged: {status}")
        time.sleep(5)

if __name__ == "__main__":
    run_simulation()