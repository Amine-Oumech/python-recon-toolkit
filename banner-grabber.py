
#! /usr/bin/python3

import socket

# The socket librarie is a networking module that contain crucial
# functions for creating tcp communication connection and etc.


host=input("enter the ip of your target:")

# here we tell the user to enter the targeted ip

port=int(input("enter the port targeted:"))

# also here we give the user the option to select the targeted port


banner_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

""" in this line we create the socket that we will need during our
connection with the target , also we can say that its the bridge between us and the target then,we call the socket object and we
give it two argument AF_INET for telling the system that we want
to use ipv4 and SOCK_STREAM for telling that we want to use the
tcp protocol"""


banner_socket.settimeout(2)

# here we tell the program to end  the connection if the server
# do not respond in 2 seconds


response=banner_socket.connect_ex((host,port))

if response == 0:

  """in the previous line we use the connect_ex function this is
  important because it return 0 number if the server responds
  and other numbers who are in opposite to 0 if the connection
  failed this will help us to detect whether a port is open or closed"""

  print(f"the Port {port} is open")

  s=banner_socket.recv(4096)

  """we use the recv function in order to receive and the spy on
  the banner that is expected to be on banner_socket variable
  who store our socket connection and we give the recv function
  one argument which is 4096 that's means 4096 is the number
  of maximuim bytes that the function can hold """

  decoding=s.decode(errors="ignore")

  """it is well known that the recv function return data in bytes
  this why we include the decode function in our script to turn
  data from bytes into string and we give it the argument
  errors="ignore" which mean also skipping errors if they happened
  along the way """


  portby_serv=socket.getservbyport(port)

  # in this line we use the getservbyport which is a function that
  # can recognise the service from the port entered by the user

  print(f"The version of the {portby_serv} service is {decoding}")

  banner_socket.close()


elif response !=0:

  """ as i said before if the connect_ex function return a number
  apart 0 it is considered as failed connection which mean
  the port is closed """

  print(f"the Port {port} is closed")




"""
note:it is very important to know that this simple script is not
relevant for all services because this script rely on receving
and reading the banner , some protocols send their banner
automatically once we connect to the server ,but

some protocols do not send their banner automatically for ex the
http protocol when he receive a connection he wait for an http
request ,so to handle this problem we need to make specific probes
for this kind of protocols

this script can work with ssh ftp smtp mysql telnet pop3 imap

while protocols such as http https dns smb snmp dhcp requires some
specific requests and interaction before sending their banner"""

