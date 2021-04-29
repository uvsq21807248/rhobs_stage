import datetime
import json

#
def List_music():
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        list_music = []
    for p in json_data:
        for k in json_data[p]["music"]:
            if k not in list_music:
                list_music.append(k)
    return list_music

def Listner_by_music():
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        cpt = 0
        mon_dictionnaire={}
        for music in List_music():
            for p in json_data:
                if music in json_data[p]["music"]:
                    cpt += 1
            mon_dictionnaire[music]=cpt
            cpt = 0
    return mon_dictionnaire

def Avg_age_by_music():
    with open('data_rhobs.json', 'r') as j:
        age = 0
        cpt = 0
        mon_dictionnaire={}
        today = datetime.date.today()
        json_data = json.load(j)
        for music in List_music():
            for p in json_data:
                if music in json_data[p]["music"]:
                    age += today.year - datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
                    cpt += 1
            age_moyen = age/cpt
            mon_dictionnaire[music] = "%.2f" % age_moyen
            age = 0
            cpt = 0
    return mon_dictionnaire

def Year_city(city):
    with open('data_rhobs.json', 'r') as j:
        json_data = json.load(j)
        for p in json_data:
            if json_data[p]["city"] == city:
                return datetime.datetime.strptime(json_data[p]["birthdate"],'%Y-%m-%d').year
    return False

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


