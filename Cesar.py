message = input("Entrez le message à chiffrer s'il vous plait: ")
decalage = int(input("Entrez le décalage s'il vous plait: "))

def chiffrer(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere.isalpha():
            decalage_base = ord('a') if caractere.islower() else ord('A')
            resultat += chr((ord(caractere) - decalage_base + decalage) % 26 + decalage_base)
        else:
            resultat += caractere
    return resultat

message_chiffre = chiffrer(message, decalage)
print("Message chiffré :", message_chiffre)


def dechiffrer(message, decalage):
    return chiffrer(message, 26 - decalage)


message_dechiffre = dechiffrer(message_chiffre, decalage)
print("Message déchiffré :", message_dechiffre)

