from random import randint
import socket
import sys

HOST = '192.168.43.116'
PORT = 54321

network_connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    network_connector.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué")
    sys.exit()

print("Connexion établie avec le serveur SNT....")

toFind = randint(1, 100)
attempts = 0
number = -1

while toFind != number:
    attempts += 1
    number = int(network_connector.recv(1024).decode('UTF-8'))
    if number > toFind:
        network_connector.send("-".encode('UTF-8'))
    elif number < toFind:
        network_connector.send("+".encode('UTF-8'))
    else:
        network_connector.send("=".encode('UTF-8'))
        print("Le serveur a trouvé le nombre en {} coups !".format(attempts))
        break

# Fermeture de la connexion
print("Connexion interrompue ...")
network_connector.close()
