import csv

L = []

with open('RTE_2020.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
#        print(','.join(row))
        L.append(row)
del(L[0])   #efface la première valeur de la liste (ce sont que des str non utiles au traitement des données)
del(L[-1])  #efface la dernière valeur de la liste (ce sont que des str non utiles au traitement des données)
#print(L[0])    #permet de vérifier si la première valeur de la liste a bel et bien été éffacée 
#print(L[-1])    #permet de vérifier si la dernière valeur de la liste a bel et bien été éffacée
#print(len(L[0]))    #sert à connaitre le nombre de colonnes à traiter

# Les lignes qui suivent sont des initialisations de valeurs afin de connaître la quantité maximum utilisée d'une ressource lors de l'année 2020
 
 #########
# Maximum #
 #########


# Consommation :

init_conso_maxi = int(L[0][4])
for i in range(len(L)):
  if L[i][4] != '':
    maxi_conso = int(L[i][4])
    if init_conso_maxi < maxi_conso :
      init_conso_maxi = maxi_conso
      indice_max_conso = i


# Fioul :

init_fioul_maxi = int(L[0][7])
for i in range(len(L)):
  if L[i][7] != '':
    maxi_fioul = int(L[i][7])
    if init_fioul_maxi < maxi_fioul :
      init_fioul_maxi = maxi_fioul
      indice_max_fioul = i


# Charbon :

init_charb_maxi = int(L[0][8])
for i in range(len(L)):
  if L[i][8] != '':
    maxi_charb = int(L[i][8])
    if init_charb_maxi < maxi_charb :
      init_charb_maxi = maxi_charb
      indice_max_charb = i


# Gaz :

init_gaz_maxi = int(L[0][9])
for i in range(len(L)):
  if L[i][9] != '':
    maxi_gaz = int(L[i][9])
    if init_gaz_maxi < maxi_gaz :
      init_gaz_maxi = maxi_gaz
      indice_max_gaz = i


# Nucléaire :

init_nuc_maxi = int(L[0][10])
for i in range(len(L)):
  if L[i][10] != '':
    maxi_nuc = int(L[i][10])
    if init_nuc_maxi < maxi_nuc :
      init_nuc_maxi = maxi_nuc
      indice_max_nuc = i


# Eolien :

init_eol_maxi = int(L[0][11])
for i in range(len(L)):
  if L[i][11] != '':
    maxi_eol = int(L[i][11])
    if init_eol_maxi < maxi_eol :
      init_eol_maxi = maxi_eol
      indice_max_eol = i


# Solaire :

init_sol_maxi = int(L[0][12])
for i in range(len(L)):
  if L[i][12] != '':
    maxi_sol = int(L[i][12])
    if init_sol_maxi < maxi_sol :
      init_sol_maxi = maxi_sol
      indice_max_sol = i


# Hydraulique :

init_hyd_maxi = int(L[0][13])
for i in range(len(L)):
  if L[i][13] != '':
    maxi_hyd = int(L[i][13])
    if init_hyd_maxi < maxi_hyd :
      init_hyd_maxi = maxi_hyd
      indice_max_hyd = i


# Bioenergies :

init_bio_maxi = int(L[0][15])
for i in range(len(L)):
  if L[i][15] != '':
    maxi_bio = int(L[i][15])
    if init_bio_maxi < maxi_bio :
      init_bio_maxi = maxi_bio
      indice_max_bio = i


# Taux de Co2 :

init_tx_maxi = int(L[0][17])
for i in range(len(L)):
  if L[i][17] != '':
    maxi_tx = int(L[i][17])
    if init_tx_maxi < maxi_tx :
      init_tx_maxi = maxi_tx
      indice_max_tx = i




 #########
# Minimum #
 #########


# Consommation :

init_conso_mini = int(L[0][4])
for i in range(len(L)):
  if L[i][4] != '':
    mini_conso = int(L[i][4])
    if init_conso_mini > mini_conso :
      init_conso_mini = mini_conso
      indice_mini_conso = i


# Fioul :

init_fioul_mini = int(L[0][7])
for i in range(len(L)):
  if L[i][7] != '':
    mini_fioul = int(L[i][7])
    if init_fioul_mini > mini_fioul :
      init_fioul_mini = mini_fioul
      indice_mini_fioul = i


# Charbon :

init_charb_mini = int(L[0][8])
for i in range(len(L)):
  if L[i][8] != '':
    mini_charb = int(L[i][8])
    if init_charb_mini > mini_charb :
      init_charb_mini = mini_charb
      indice_mini_charb = i


# Gaz :

init_gaz_mini = int(L[0][9])
for i in range(len(L)):
  if L[i][9] != '':
    mini_gaz = int(L[i][9])
    if init_gaz_mini > mini_gaz :
      init_gaz_mini = mini_gaz
      indice_mini_gaz = i


# Nucléaire :

init_nuc_mini = int(L[0][10])
for i in range(len(L)):
  if L[i][10] != '':
    mini_nuc = int(L[i][10])
    if init_nuc_mini > mini_nuc :
      init_nuc_mini = mini_nuc
      indice_mini_nuc = i


# Eolien :

init_eol_mini = int(L[0][11])
for i in range(len(L)):
  if L[i][11] != '':
    mini_eol = int(L[i][11])
    if init_eol_mini > mini_eol :
      init_eol_mini = mini_eol
      indice_mini_eol = i


# Solaire :

init_sol_mini = int(L[0][12])
for i in range(len(L)):
  if L[i][12] != '':
    mini_sol = int(L[i][12])
    if init_sol_mini > mini_sol :
      init_sol_mini = mini_sol
      indice_mini_sol = i


# Hydraulique :

init_hyd_mini = int(L[0][13])
for i in range(len(L)):
  if L[i][13] != '':
    mini_hyd = int(L[i][13])
    if init_hyd_mini > mini_hyd :
      init_hyd_mini = mini_hyd
      indice_mini_hyd = i


# Bioenergies :

init_bio_mini = int(L[0][15])
for i in range(len(L)):
  if L[i][15] != '':
    mini_bio = int(L[i][15])
    if init_bio_mini > mini_bio :
      init_bio_mini = mini_bio
      indice_mini_bio = i


# Taux de Co2 :

init_tx_mini = int(L[0][17])
for i in range(len(L)):
  if L[i][17] != '':
    mini_tx = int(L[i][17])
    if init_tx_mini > mini_tx :
      init_tx_mini = mini_tx
      indice_mini_tx = i



fioul = 0
charbon = 0
gaz = 0
nucleaire = 0
eolien = 0
solaire = 0
hydraulique = 0
bioenergies = 0

for i in range(len(L)):
    if i>0:    
        if L[i][7] != '':
            fioul += int(L[i][7])
#print(fioul)

for i in range(len(L)):
    if i>0:    
        if L[i][8] != '':
            charbon += int(L[i][8])

for i in range(len(L)):
    if i>0:    
        if L[i][9] != '':
            gaz += int(L[i][9])

for i in range(len(L)):
    if i>0:    
        if L[i][10] != '':
            nucleaire += int(L[i][10])

for i in range(len(L)):
    if i>0:    
        if L[i][11] != '':
            eolien += int(L[i][11])

for i in range(len(L)):
    if i>0:    
        if L[i][12] != '':
            solaire += int(L[i][12])

for i in range(len(L)):
    if i>0:    
        if L[i][13] != '':
            hydraulique += int(L[i][13])
for i in range(len(L)):
    if i>0:    
        if L[i][15] != '':
            bioenergies += int(L[i][15])
#print(fioul,",", charbon,",", gaz,",", nucleaire,",", eolien,",", solaire,",", hydraulique,",", bioenergies)
certif = True
while certif == True:
    Question = input("Que voulez-vous savoir ? mettez list pour savoir la liste de commandes possibles. Mettez 'n' pour passer à la suite")


    if Question == 'list':
        print("Les commandes possibles sont : Maximum, Minimum")
        Q = input(" : ")
        Question = Q
    elif Question == "n":
       certif = False

    if Question == 'Maximum' :
        Q1 = input("Sur quoi voulez le maximum ? Consommation, Fioul, Charbon, Gaz, Nucléaire, Eolien, Solaire, Hydraulique, Bioenergies, TauxCo2 : ")
        if Q1 == 'Consommation':
            print(init_conso_maxi,"le", L[indice_max_conso][2])
        elif Q1 == 'Fioul':
            print(init_fioul_maxi,"le", L[indice_max_fioul][2])
        elif Q1 == 'Charbon':
            print(init_charb_maxi,"le", L[indice_max_charb][2])
        elif Q1 == 'Gaz':
            print(init_gaz_maxi,"le", L[indice_max_gaz][2])
        elif Q1 == 'Nucleaire':
            print(init_nuc_maxi,"le", L[indice_max_nuc][2])
        elif Q1 == 'Eolien':
            print(init_eol_maxi,"le", L[indice_max_eol][2])
        elif Q1 == 'Solaire':
            print(init_sol_maxi,"le", L[indice_max_sol][2])
        elif Q1 == 'Hydraulique':
            print(init_hyd_maxi,"le", L[indice_max_hyd][2])
        elif Q1 == 'Bioenergies':
            print(init_bio_maxi,"le", L[indice_max_bio][2])
        elif Q1 == 'TauxCo2':
            print(init_tx_maxi,"le", L[indice_max_tx][2])
        else :
            certif = False

    elif Question == 'Minimum':
        Q1 = input("Sur quoi voulez le maximum ? Consommation, Fioul, Charbon, Gaz, Nucléaire, Eolien, Solaire, Hydraulique, Bioenergies, TauxCo2 : ")
        if Q1 == 'Consommation':
            print(init_conso_mini,"le", L[indice_mini_conso][2])
        elif Q1 == 'Fioul':
            print(init_fioul_mini,"le", L[indice_mini_fioul][2])
        elif Q1 == 'Charbon':
            print(init_charb_mini,"le", L[indice_mini_charb][2])
        elif Q1 == 'Gaz':
            print(init_gaz_mini,"le", L[indice_mini_gaz][2])
        elif Q1 == 'Nucleaire':
            print(init_nuc_mini,"le", L[indice_mini_nuc][2])
        elif Q1 == 'Eolien':
            print(init_eol_mini,"le", L[indice_mini_eol][2])
        elif Q1 == 'Solaire':
            print(init_sol_mini,"le", L[indice_mini_sol][2])
        elif Q1 == 'Hydraulique':
            print(init_hyd_mini,"le", L[indice_mini_hyd][2])
        elif Q1 == 'Bioenergies':
            print(init_bio_mini,"le", L[indice_mini_bio][2])
        elif Q1 == 'TauxCo2':
            print(init_tx_mini,"le", L[indice_mini_tx][2])
        else :
            certif = False

#création d'un choix pour l'utilisateur, quelle donnée il souhaite voir
oui = True
print("Nous avons une liste des énergies utilisées afin de produire de l'électricité lors de l'année 2020, que voulez vous savoir ?")
while oui == True:
    Q1 = input("Fioul, Charbon, Gaz, Nucléaire, Eolien, Solaire, Hydraulique, Bioenergies  ")
    if Q1 == 'Fioul':
        print("La quantité d'électricité produit par le fioul est de : ", fioul)
    elif Q1 == 'Charbon':
        print("La quantité d'électricité produit par le charbon est de : ", charbon)
    elif Q1 == 'Gaz':
        print("La quantité d'électricité produit par le gaz est de : ", gaz)
    elif Q1 == 'Nucléaire':
        print("La quantité d'électricité produit par le nucléaire est de : ", nucleaire)
    elif Q1 == 'Eolien':
        print("La quantité d'électricité produit par l'eolien est de : ", eolien)
    elif Q1 == 'Solaire':
        print("La quantité d'électricité produit par l'énergie solaire est de : ", solaire)
    elif Q1 == 'Hydraulique':
        print("La quantité d'électricité produit par le hydraulique est de : ", hydraulique)
    elif Q1 == 'Bioenergies':
        print("La quantité d'électricité produit par les bioénergies est de : ", bioenergies)
    Q2 = input("Voulez-vous continuer votre recherche ? : oui/non  ")
    if Q2 == 'non':
        oui = False

from matplotlib import pyplot as plt
from pylab import*

name = ['Fioul', 'Charbon', 'Gaz', 'Nucléaire', 'Eolien', 'Solaire', 'Hydraulique', 'Bioenergies']
data = [1854049 , 2733784 , 68930419 , 670366814 , 79396818 , 24922373 , 129603428 , 19356189]
explode = (0.30,0.50,0,0,0,0,0,0)

rep = input('Voulez-vous un graphique représentant ces données ? Oui/Non : ')
if rep == 'Oui':
    plt.title("Répartition des ressources utilisées pour la production d'électricité (en 2020)")
    plt.pie(data,explode=explode, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.legend(name)
    plt.show()






















