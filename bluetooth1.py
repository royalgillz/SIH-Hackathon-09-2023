import bluetooth
import time  # You need to import the time module for sleep functionality

# Define the doctor's Bluetooth device address (you need to know this in advance).
doctor_device_address = "30:bb:7d:d9:45:16"  # Replace with the doctor's actual device address

# Function to detect the doctor's presence
def detect_doctor_presence():
    try:
        nearby_devices = bluetooth.discover_devices(duration=20, lookup_names=True, device_id=-1, device_name=None, duration_multiplier=1, flush_cache=True, lookup_class=False, device_class=None, device_id_max=-1, len=-1)
        for addr, name in nearby_devices:
            if addr == doctor_device_address:
                return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

# Main function to check the doctor's presence
def main():
    while True:
        is_doctor_present = detect_doctor_presence()
        if is_doctor_present:
            print("Doctor is present in the hospital.")
        else:
            print("Doctor is not present in the hospital.")
        
        # Delay for some time before checking again (e.g., every 5 minutes)
        time.sleep(300)  # 300 seconds = 5 minutes

if __name__ == "__main__":
    main()
