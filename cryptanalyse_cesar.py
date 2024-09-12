message_chiffre = input("Entrez le message chiffré s'il vous plait: ")
decalage = int(input("Entrez le décalage s'il vous plait: "))

def dechiffrement_cesar(message_chiffre, decalage):
    texte_clair = ""
    for caractere in message_chiffre:
        if caractere.isalpha():
            decalage_base = ord('a') if caractere.islower() else ord('A')
            texte_clair += chr((ord(caractere) - decalage_base - decalage) % 26 + decalage_base)
        else:
            texte_clair += caractere
    return texte_clair

def attaque_brute_force(message_chiffre):
    propositions = []
    for decalage in range(26):
        texte_clair = dechiffrement_cesar(message_chiffre, decalage)
        propositions.append((decalage, texte_clair))
    return propositions



propositions = attaque_brute_force(message_chiffre)
for decalage, texte_clair in propositions:
    print(f"Décalage {decalage}: {texte_clair}")
