import serial
import serial.tools.list_ports
import time
import sys

def reboot_to_bootsel():
    # Raspberry Pi Pico's USB Vendor ID
    PICO_VID = 0x2e8a 
    
    # 1. Find the Pico's COM port automatically
    ports = serial.tools.list_ports.comports()
    pico_port = None
    
    for port in ports:
        if port.vid == PICO_VID:
            pico_port = port.device
            break
            
    if not pico_port:
        print("Error: No Raspberry Pi Pico found. Is it plugged in and running?")
        sys.exit(1)
        
    print(f"Found Pico on {pico_port}. Sending reboot command...")

    try:
        # 2. Open the serial port
        # Using a context manager ensures the port closes correctly
        with serial.Serial(pico_port, 115200, timeout=1) as ser:
            time.sleep(0.1) # Short buffer for the connection
            ser.write(b'b') # Send the 'b' character defined in your C code
            ser.flush()
            print("Command sent! Pico should now be in BOOTSEL mode.")
    except Exception as e:
        print(f"Failed to communicate with Pico: {e}")

if __name__ == "__main__":
    reboot_to_bootsel()
