import datetime
import json

#la fonction List_music() retourne la liste des différents types de musique qui existe dans le fichier data_rhobs.json
def List_music():
    #Lecture des données
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
    #Initialisation de la liste de retoure
        list_music = []
    #parcours du fichier
    for p in json_data:
        for k in json_data[p]["music"]:
            if k not in list_music:
                list_music.append(k)
    return list_music


'''La fonction Listner_by_music() retourne les différents types de musique et le nombre de personnes qui écoute à chaque type
sous la forme d'un dictionnaire qui prend comme clé le type de la musique et comme valeur le nombre de personnes'''
def Listner_by_music():
    #Lecture des données
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        #initialisation d'un compteur
        cpt = 0
        #initialisation d'un dictionnaire
        mon_dictionnaire={}
        #parcours de la liste des types de musique
        for music in List_music():
            for p in json_data:
        #incrémentation du compteur si le type de la musique existe dans List_music():
                if music in json_data[p]["music"]:
                    cpt += 1
            mon_dictionnaire[music]=cpt
            cpt = 0
    return mon_dictionnaire
'''La fonction Avg_age_by_music() retourne les différents types de musique et la moyenne de l'age des personnes qui écoute à chaque type
sous la forme d'un dictionnaire qui prend comme clé le type de la musique et comme valeur la moyenne de l'age'''
def Avg_age_by_music():
    #Lecture des données
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        #Initialisation d'un compteur de l'age et d'un dictionnaire
        age = 0
        cpt = 0
        mon_dictionnaire={}
        #Précision de la date d'aujourd'hui
        today = datetime.date.today()
        #parcous dans la liste des types de musique et le fichier des données
        for music in List_music():
            for p in json_data:
        #vérification de l'existence de la musique dans le fichier des données
                if music in json_data[p]["music"]:
        #calcule de l'age des personne
                    age += today.year - datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
                    cpt += 1
        #calcule de la moyenne des ages
            age_moyen = age/cpt
            mon_dictionnaire[music] = "%.2f" % age_moyen
            age = 0
            cpt = 0
    return mon_dictionnaire
#La fonction Year_city(city) retourne l'année de naissance de la première personne  dont la ville est donnée en paramétre
def Year_city(city):
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        for p in json_data:
            if json_data[p]["city"] == city:
                return datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
    return False
#La fonction Min_year_city(city) retourne l'année de naissance de la personne la plus vieille dont la ville est donnée en paramétre
def Min_year_city(city):
    if ( Year_city(city)== False):
        return False
    annee = Year_city(city)
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        for p in json_data:
            if json_data[p]["city"] == city:
                if datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year < annee:
                    annee = datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
    return annee
#La fonction Max_year_city(city) retourne l'année de naissance de la personne la plus jeune dont la ville est donnée en paramétre
def Max_year_city(city):
    if (Year_city(city)== False):
        return False
    annee = Year_city(city)
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        for p in json_data:
            if json_data[p]["city"] == city:
                if datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year > annee:
                    annee = datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
    return annee
'''La fonction Pyramid Age(city, Marge) prend en paramètre 2 arguments la ville et un entier qui représente la taille 
de la tranche et elle retourne un dictionnaire dont la clé est l'intervalle entre l'année début et l'année fin et 
la valeur sous forme d'une liste contenant les noms des personnes existant dans cet intervalle
 '''
def Pyramid_age(city,marge):
    if( Year_city(city)==False):
        print("la ville n'existe pas")
    else:
        min_annee=Min_year_city(city)
        max_annee=Max_year_city(city)
        liste=[]
        liste_p=[]
        mon_dictionnaire={}
        with open('data_rhobs.json', 'r') as j:
            json_data = json.load(j)
        while min_annee <= max_annee:
            for p in json_data:
                if json_data[p]["city"] == city:
                    if datetime.datetime.strptime(json_data[p]["birthdate"], '%Y-%m-%d').year >= min_annee and datetime.datetime.strptime(json_data[p]["birthdate"], '%Y-%m-%d').year <= min_annee + marge:
                        liste_p.append(p)
            #mon_dictionnaire = {"Noms ": liste_p, "anne_inf": min_annee, "anne_sup": min_annee + marge}
            mon_dictionnaire[str(min_annee)+ "-"+str(min_annee+marge)]=liste_p
            #print(mon_dictionnaire)
            #print(" ")
            #liste.append(mon_dictionnaire)
            liste_p=[]


            min_annee+=marge
    #return liste
    return mon_dictionnaire












print(Pyramid_age("Blin",4))
#print(Listner_by_music())
#print(Avg_age_by_music())


