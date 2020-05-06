import socket
import sys


def average(a, b):
    return (a + b) // 2


# Adresse IP de la machine serveur (ipconfig sur Windows, ifconfig sinon)
HOST = '192.168.43.116'

# Choisir un port entre 49152 et 65535
# Ce sera votre n° de porte d'accès au serveur
PORT = 54321

# Creation du connecteur reseau
network_connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du connecteur à HOST en passant par PORT
try:
    network_connector.bind((HOST, PORT))
except socket.error:
    print("La liaison a échoué")
    sys.exit()

print("Serveur lancé .... en attente de requêtes d'un client")
network_connector.listen(1)
connexion, adresse = network_connector.accept()
print("Client connecté , adresse IP : %s , port: %s" % (adresse[0], adresse[1]))

minNumber = 0
maxNumber = 100
state = ""
count = 0

while state != "=":
    count += 1
    number = average(minNumber, maxNumber)
    connexion.send(str(number).encode(encoding='UTF-8'))
    state = connexion.recv(1024).decode('UTF-8')
    print("Proposition de " + str(number))
    if state == "-":
        maxNumber = number
        print("Le client m'indique que le nombre est plus petit")
    elif state == "+":
        minNumber = number
        print("Le client m'indique que le nombre est plus grand")
    else:
        connexion.close()
        exit("J'ai trouvé le nombre du client nombre en " + str(count) + " essais, c'était " + str(number))
