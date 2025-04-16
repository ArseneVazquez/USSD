from functions import *
from datetime import datetime

ibidandazwa = charger_json()

def kuraba():
    for i in ibidandazwa:
        raba(i)

def gushiramwo():
    ikiranga_ikidandazwa = len(ibidandazwa) + 1
    izina = input("shiramwo izina ry'ikidandazwa: ")
    igiciro = reelle("shiramwo igiciro: ")
    igitigiri = reelle("shiramwo igitigiri: ")

    adding = input(f"murifuza vy'ukuri gushiramwo iki kidandazwa {izina}? emeza mugufyonda ego cank e: ").upper()

    if adding == "EGO" or adding == "E":
        ikidandazwa = shiramwo(ikiranga_ikidandazwa, izina, igiciro, igitigiri)
        ibidandazwa.append(ikidandazwa)
        json_sauv(ibidandazwa)

def guhanagura():
    for pr in ibidandazwa:
        print(f"{pr.get('id')} : {pr.get('izina')}")

    numero_yikidandazwa = entier("shiramwo numero yaco kugira ugikuremwo: ")
    for index, pr in enumerate(ibidandazwa):
        if pr.get("id") == numero_yikidandazwa:
            ibidandazwa.pop(index)
            json_sauv(ibidandazwa)
            print("igikorwa caheze")

    kubitondeka(ibidandazwa)

def guhindura():
    for pr in ibidandazwa:
        print(f"{pr.get('id')} : {pr.get('izina')}")

    numero = entier("shiramwo numero yaco kugira ugikugihindura: ")
    ico = entier("wipfuza guhindura iki? izina andika 1, igiciro 2 canke igitigiri 3 : ")

    if ico == 1:
        izina_rishasha = input("shiramwo izina rishasha: ")
        ico_guhindura("izina", izina_rishasha, numero, ibidandazwa)
    elif ico == 2:
        igiciro_gishasha = reelle("shiramwo igiciro gishasha: ")
        ico_guhindura("igiciro", igiciro_gishasha, numero, ibidandazwa)
    elif ico == 3:
        igitigiri_gishasha = reelle("shiramwo ikindi igitigiri: ")
        ico_guhindura("igitigiri", igitigiri_gishasha, numero, ibidandazwa)

def kudandaza():
    numero = entier("shiramwo numero y'ico ushaka kudandaza: ")
    quantite = reelle("shiramwo igitigiri ushaka kugurisha: ")

    for pr in ibidandazwa:
        if pr.get("id") == numero:
            pr["igitigiri"] -= quantite
            ubutunzi = quantite * pr["igiciro"]
            itariki = datetime.now().strftime("%d/%m/%Y %Hh%M")
            ibiguzwe = f"{itariki} {pr.get('izina')}    x {quantite} :  {ubutunzi}"
            change_file("ivyadandajwe.txt", ibiguzwe)
            json_sauv(ibidandazwa)
            print(ubutunzi)

def ivyakozwe():
    with open("ivyadandajwe.txt", "r", encoding="utf-8") as file:
        print(file.read())

def raporo():
    raporo("ivyadandajwe.txt", "ibidandazwa.json")

def byee():
    print("byeee")

ibikorwa = {
    "1": kuraba,
    "2": gushiramwo,
    "3": guhanagura,
    "4": guhindura,
    "5": kudandaza,
    "6": ivyakozwe,
    "7": raporo,
    "0": byee
}

while True:
    with open("menu.txt", "r") as menu:
        print(menu.read())

    choice = input("shiramwo igiharuro: ")

    try:
        ibikorwa[choice]()
    except KeyError:
        print("Mwihenze igiharuro shiramwo neza")

    if choice == "0":
        break