import socket
import sys
targets=["127.0.0.1","192.168.19.140","192.168.1.11"]

with open("results.txt","w") as f:
    for target in targets:
        print(f"Scanning {target}")
        f.write(f"\nScanning {target}")
        
        for port in range(20,81):
          try:
             with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
              s.settimeout(3)
              response=s.connect_ex((target,port))
          
             if response == 0:
                print(f"The port {port} on  {target} is open")
                f.write(f"\nThe port {port} on  {target} is open")
             elif response != 0:
                print(f"The port {port} on {target} is closed")
                f.write(f"\nThe port {port} on {target} is closed")
          
          except socket.timeout:
                print("Connection timed out")
           
          except OSError as e:
                print(f"{e}")
        
          except KeyboardInterrupt:
                print("program stopped")
                sys.exit()


"""This version of our tcp scanner is more improved compared to our previous simple-scanner ,because this 
scanner make us able to scan multiple targets depending on our requirement , as well as it store the scan 
result to a specific file for future use ,moreover this version handle multiple cases of errors exceptions """
