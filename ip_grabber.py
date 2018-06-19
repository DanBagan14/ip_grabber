import socket

restart = True



def enter_url():
    URL_input = input("Enter URL to Scan: ")
    print(socket.gethostbyname(URL_input))
    print("\n\n\n")

def intro():
    print("===========================================")
    print("D33BY IP GRABBER v 1.0")
    print("===========================================")

while True:
    intro()
    enter_url()
