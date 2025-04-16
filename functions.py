import re
import os
import json

def shiramwo(id, izina, igiciro, igitigiri):

    produits = {
        "id": id,
        "izina": izina,
        "igiciro": igiciro,
        "igitigiri": igitigiri
    }
    return produits


def raba(ikid):
    print("===================")

    print(f"id: {ikid.get("id")}\nizina: {ikid.get("izina")}\nigiciro: {ikid.get("igiciro")}\nigitigiri: {ikid.get("igitigiri")}")

    print("===================")


def igindurwa(ico_guhindura, igiciro, igitigiri):
    ico_guhindura["igiciro"] = igiciro
    ico_guhindura["igitigir"] = igitigiri
    return ico_guhindura


def change_file(fichier, ligne_nshasha):

   
    if not os.path.exists(fichier):
        with open(fichier, "w", encoding="utf-8") as f:
            f.write("               vyose hamwe : 0\n")

    with open(fichier, "r", encoding="utf-8") as f:
        lignes = f.readlines()

 
    for i, ligne in enumerate(lignes):
        if "vyose hamwe" in ligne:
            lignes.insert(i, ligne_nshasha + "\n")
            break

    total = 0
    for ligne in lignes:
        if "vyose hamwe" in ligne:
            continue
        texte_total = re.search(r":\s*([\d\s]+)", ligne)
        if texte_total:
            montant = int(texte_total.group(1).replace(" ", ""))
            total += montant

  
    for i, ligne in enumerate(lignes):
        if "vyose hamwe" in ligne:
            lignes[i] = f"                        vyose hamwe: {total:,}".replace(",", " ") + "\n"
            break

    with open(fichier, "w", encoding="utf-8") as f:
        f.writelines(lignes)


def raporo(fichier_ventes, fichier_produits):
    try:
        with open(fichier_ventes, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print("iyi fichier ntayibaho.")
        return

    try:
        with open(fichier_produits, "r", encoding="utf-8") as f:
            produits = json.load(f)

    except FileNotFoundError:
        print("iyi fichier ntayibaho.")
        return

    total_articles = 0
    total_argent = 0
    # montant = 0

    for ligne in lignes:
        if "vyose hamwe" in ligne:
            continue

        quantite = re.search(r"x\s*(\d+)", ligne)
        if quantite:
            total_articles += int(quantite.group(1))

        match_argent = re.search(r":\s*([\d\s]+)", ligne)
        if match_argent:
            montant = int(match_argent.group(1).replace(" ", ""))
            total_argent += montant

    total_produits = len(produits)
    produits_finis = sum(1 for p in produits if p.get("igitigiri", 1) <= 0)

    raporo_write = "------Ivyakozwe------\n"
    raporo_write += f"Ibidandazwa vyose          : {total_produits}\nIbidandazwa vyaheze        : {produits_finis}\nIgitigiri vyose vyaguzwe   : {total_articles}"
    raporo_write += f"\nUbutunzi bwose bwinjijwe   : {total_argent} Fbu"

    with open("raporo.txt", "w", encoding="utf-8") as f:
        f.write(raporo_write)


    print("\n------Ivyakozwe------")
    print(f"Ibidandazwa vyose          : {total_produits}")
    print(f"Ibidandazwa vyaheze        : {produits_finis}")
    print(f"Igitigiri vyose vyaguzwe   : {total_articles}")
    print(f"Ubutunzi bwose bwinjijwe   : {total_argent} Fbu")



def json_sauv(ibidandazwa, fichier="ibidandazwa.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(ibidandazwa, f, indent=4, ensure_ascii=False)

def charger_json(fichier="ibidandazwa.json"):
    if not os.path.exists(fichier):
        return []
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)


def ico_guhindura(igihindurwa, icoguhindura, ikiyiranga, produits):
    for pr in produits:
        if pr.get("id") == ikiyiranga:
            pr[igihindurwa] = icoguhindura
            json_sauv(produits)
            print(f"Ivyo mwakoze vyakunze.")


def entier(message):
    while True:
        try:
            choice = int(input(message))
            return choice
        except ValueError:
            print("shiramwo neza igiharuro.")

def reelle(message):
    while True:
        try:
            choice = float(input(message))
            return choice
        except ValueError:
            print("shiramwo neza igiharuro.")

def kubitondeka(produits):

    for index, pr in enumerate(produits):
        pr["id"] = index + 1
        json_sauv(produits)

