"""
A&G

Implémentation de ALGO1
"""


fichier = open("data1.txt")

lignes_fichier = fichier.readlines()

# print(lignes_fichier)

nb_loc = int(lignes_fichier[0].strip().split()[1])
nb_res = int(lignes_fichier[1].strip().split()[1])
nb_mac = int(lignes_fichier[2].strip().split()[1])
nb_pro = int(lignes_fichier[3].strip().split()[1])
nb_ser = int(lignes_fichier[4].strip().split()[1])

