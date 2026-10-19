import math
import statistics

# Variables
PI = math.pi
E = math.e

def carre(x):
    return x*x

def cube(x):
    return x*x*x

def factorielle(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

def valeur_absolue(x):
    if x < 0 :
        return -(x)
    else :
        return x

def maximum(liste):
    return max(liste)

def minimum(liste):
    return min(liste)

def moyenne(liste):
    return sum(liste) / len(liste)

def ecart_type(liste):
    moy = moyenne(liste)
    somme = 0 
    for x in liste:
        somme += (x-moy)**2
    return math.sqrt(somme/len(liste))

def mediane(liste):
    return statistics.median(liste)

def somme_cumulee(liste):
    somme_cum = 0
    list_cum = []
    for element in liste:
        somme_cum += element
        list_cum.append(somme_cum)
    return list_cum

def compter_occurrences(liste):
    dico = {}
  
    for element in liste:
        dico[element] = liste.count(element)
    return dico

def inverser_dict(dictionnaire):
    dico_inverse = {}
    for k,v in dictionnaire.items():
        dico_inverse[v] = k
    return dico_inverse

def filtrer_pairs(liste):
    liste_pairs = []
    for n in liste:
        if n%2==0 :
            liste_pairs.append(n)
    return liste_pairs

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def trouver_doublons(liste):
    doublons = []
    for x in liste:
        if liste.count(x) > 1 and x not in doublons:
            doublons.append(x)
    return doublons

def calculer_moyenne_ponderee(valeurs, poids):
    sum_poids = sum(poids)
    somme = 0
    for i, note in enumerate(valeurs):
        for i2, coef in enumerate(poids):
            if i == i2:
                somme += (note*coef)
    return somme/sum_poids
 