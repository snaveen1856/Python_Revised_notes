"""
Network : Interconnection of computers is called network
Client : The computers that receive services
Server : The computers that provide services

3 requirements to establish network :
    Hardware : Includes Computers,cables,modems,routers,hubs
    Software : Includes programs to communicate between server and client
    Protocol : Representing way to establish connections and helps to send and receive data in standard format

Protocols:
--------------
TCP/IP and UDP(User Datagram Protocol)

TCP/IP : Transmission Control Protocol/Internet Protocol

            Application Layer
                |
                |           Data
                ^
            Transmission Protocol
                |
                |           Packets(group of data in bytes)
                ^
            Internet Protocol
                |
                |           Converts Packets into envelopes(Frames) 
                |           Each frame contains
                |                       Packet  +
                |                       IP Address of Source computer +
                |                       IP Address of Destination computer +
                |                       Additional data
                ^
            Data Link Layer
                |
                |           Dispatches data to correct destination
                ^
            Physical Layer  Physically transmits the data on the network using hardware


IP Address : unique identification number given to each computer on the network
             Ex : 216.58.194.197
                  www.google.com

                Domain name is automatically mapped to ip address is called DNS(Domain Naming Service)


Reserved port numbers and associated services :
-----------------------------------------------
Socket : Logical connecting point between client and server
         Each socket is given unique identification number called "port number"
         Port number can take 2 bytes(0 to 65532 bits)
Socket Programming : Establishing connection between client and server is called "Socker Programming"

Reserved port numbers and Associated Services:
----------------------------------------------
Port Number  Application/service 
===========  ================================================

13           Date,Time services
21           FTP, to transfer files
22*          ssh, The Secure Shell (SSH) Protocol
23           Telnet,  provides remote login
25           SMTP,  which delivers mails 
67           BOOTP, which provides configuration at boot time 
80*          HTTP, which transfer web PAGES
443*         HTTPS, which transfer web pages securely
"""