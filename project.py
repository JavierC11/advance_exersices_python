##in This project we are gonna make a tool help us to know the place that we have to be for traveling in the time.

#Usa, mexico, guatemala, costarica, peru, argentinca, brazil
#españa, francia, Alemania, Russia.
## Ghana, Egipto, Sudafrica, Maruecos
# Iran, India, China, Japon, Australia
from optparse import Option
from typing import Dict
from datetime import date, datetime
from typing import Dict, List
import pytz
import time
import os

def time_latam(country: str):
    country_latam_tz = pytz.timezone("America/" + country)
    country_latam = datetime.now(country_latam_tz)
    return country_latam

def time_europe(country: str):
    country_europe_tz = pytz.timezone("Europe/" + country)
    country_europe = datetime.now(country_europe_tz)
    return country_europe

def time_asian(country: str):
    country_asia_tz = pytz.timezone("Asia/" + country)
    country_asia = datetime.now(country_asia_tz)
    return country_asia

def time_african(country: str):
    country_africa_tz = pytz.timezone("Africa/" + country)
    country_africa = datetime.now(country_africa_tz)
    return country_africa


def consolidate()-> Dict:
    country_latam_list =  ["Guatemala", "Mexico_City","Buenos_Aires", "Caracas", "Bogota"]
    new_time_latam = {}
    for country in country_latam_list:
        country2 = time_latam(country)
        new_time_latam[country] = int(country2.strftime("%H"))
    # print(new_time_latam)

    country_europe_list = ["Madrid", "Berlin", "London" , "kiev" ,"Minsk"]
    new_time_europe = {}
    for country in country_europe_list:
        country2 = time_europe(country)
        new_time_europe[country] = int(country2.strftime("%H"))
    # print(new_time_europe)

    country_asian_list = ["Tokyo", "Qatar", "Taipei"]
    new_time_asian = {}
    for country in country_asian_list:
        country2 = time_asian(country)
        new_time_asian[country] = int(country2.strftime("%H"))
    # print(new_time_asian)


    country_african_list = ["Dakar", "Tripoli" , "Cairo", "Accra", "Bangui"]
    new_time_african = {}
    for country in country_african_list:
        country2 = time_african(country)
        new_time_african[country] = int(country2.strftime("%H"))
    # print(new_time_african)

    dict_time = {}
    dict_time.update(new_time_latam)
    dict_time.update(new_time_europe)
    dict_time.update(new_time_asian)
    dict_time.update(new_time_african)

    return dict_time

def run():
    os.system("clear")
    
    while True:

        now = int(datetime.now().strftime("%H"))
        dict_time = consolidate()
        # print(dict_time)
        # print(now)
        print("\n\n--------------------------------------------")
        print("""🐸 Bienvenido a esta experiencia unica!! 
por unos momentos ignoraremos todas las leyes de la fisica para poder viajar en el tiempo!!
        """)

        Option = int(input("Dime si quieres viajar al pasado o futuro. \n*. Salir [9]\n*. Viajar el Pasado [0] \n*. Viajar al Futuro [1] \n👉 "))
                
        if Option == 9:
            exit()
            
        elif Option == 0:
            changed = False
            hours = int(input("\nCuantas horas quieres viajar al pasado? 👉 "))
            now = now - hours
            for key, value in dict_time.items():
                if  now == value:
                    changed = True
                    print("🟢Para viajar en el tiempo debes teletransportarte a " +key+ " pues ahi la hora es "+ str(value))
            if changed == False:
                print("🔴No existen ciudades en el mundo con esa hora. 😞")


        elif Option == 1:
            changed = False
            hours = int(input("\nCuantas horas quieres viajar al futuro? 👉 "))
            now = now + hours
            for key, value in dict_time.items():
                if  now == value:
                    changed = True
                    print("🟢Para viajar en el tiempo debes teletransportarte a " +key+ " pues ahi la hora es "+ str(value))
            if changed == False:
                print("🔴No existen ciudades en el mundo con esa hora. 😞")

        else:
            os.system("clear")
            print("Elije una opcion correcta!!")
            time.sleep(2)

if __name__ == "__main__":
    run()


