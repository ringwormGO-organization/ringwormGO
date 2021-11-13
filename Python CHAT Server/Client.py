import socket

print("-" * 80)
print("Welcome!!")
print("-" * 80)

host = input("Type IP adress: ")
port = int(input("Type port to connect: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    podaci = s.recv(1024)
    print("-" * 40)
    print("Recv. message:", podaci.decode())

    inp = input("Type message: ")

    if inp == "exit":
        print("Connection lost...")
        s.sendall(("Chat finished.").encode())
        s.close()
        break
    s.sendall(inp.encode())
