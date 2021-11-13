import socket

print("-" * 80)
print("ringwormGO private CHAT server v1.0.0")
print("-" * 80)

#PORUKA ZA SLANJE
poruka = input("Unesite poruku za slanje/Type message to send: ")

#HOST PODACI
host = input("Type IP: ")
port = int(input("Type port: "))

#PRIMPREMA POVEZIVANJA
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

#SLUŠANJE
s.listen(5)

#POVEZANO
konekcija, adresa = s.accept()
print("You are connect with:", adresa)
print("Sending message: ")
konekcija.sendall(poruka.encode())

#CHAT

while True:
    stiglo = konekcija.recv(1024)
    print("Recv. message", stiglo.decode())

    inp = input("ringwormGO>>> ")
    konekcija.sendall(inp.encode())

    if inp == "exit":
        print("Connection lost...")
        s.sendall(("Chat finished.").encode())
        s.close()
        break
