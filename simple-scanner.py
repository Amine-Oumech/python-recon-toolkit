import socket
import sys
host=input("enter your target ip:")
ports=range(20,10000)  #you can edit the range depending on your insight to the target.

for port in ports:
  try:
      port_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
      port_socket.settimeout(3) 
      port_socket.connect((host,port)) 
      print(f"The port {port} is open")

  except ConnectionRefusedError:
      print(f"The port {port} is closed")

  except socket.timeout:
      print(f"Connection timed out for port {port}")
  
  except KeyboardInterrupt:
      print("program stopped")
      sys.exit()
  except socket.error:
      print("The server do not respond")
  except OSError:
      print("system or network error")
  
  finally:
      port_socket.close()







""" port_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) in this line we create the socket that will cary 
our connection between us and the target ,we set AF_INET for using ipv4 instead of ipv6 ,while we use SOCK_STREAM
in order to use the TCP protocol rather than  UDP ,and if we want to include udp we use SOCK_DGRAM

port_socket.settimeout(3) here we use settimeout to prevent our scanner from waiting after 3 second if the target 
do not respond our scanner will return connection timed out for the specific port  and we handle that through raising 
a socket.timeout exception 

port_socket.connect((host,port))  we connect the socket with the host and the port variable that stor our ports through 
the range function.

except ConnectionRefusedError:
      print(f"The port {port} is closed")

  except socket.timeout:
      print(f"Connection timed out for port {port}")
  
  except KeyboardInterrupt:
      print("program stopped")
      sys.exit()
  except socket.error:
      print("The server do not respond")
  except OSError:
      print("system or network error")


in this line we create a bunch of exceptions that can handle our script to run perfectly a connection refused 
is considered by our program as closed port . """

"""note:this scanner is considered as a simple portscanner ,mostly generated for learning purposes. 
