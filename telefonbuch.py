import random
from json_dict import json_dict

# Kein normales Dict, sondern ein json_dict (siehe ./json_dict.py)
eintraege = json_dict("./eintraege.json")  # String : String - Name : Telefonnummer
befehle = {}    # String : String - befehl : beschreibung

def init():
    befehle.update({'alle_anzeigen' :'Alle Einträge anzeigen', 'eintrag_hinzufuegen' : 'Neuer Eintrag','eintrag_suchen' : 'Name suchen', 'eintrag_entfernen' : 'Eintrag entfernen', 'inverse_suche': 'Nach Nummer suchen', 'buttcall' : 'zufällige Nummer wählen'})
    print('Drücken Sie h um eine Übersicht über die eingebauten Befehle zu erhalten')

init()

# 1
def dict_anzeigen(dictionary):
    for key in dictionary.keys():
        print(key, ':\t', dictionary.get(key))

# Test: dict_anzeigen({'John Cleese': '123', 'Eric Idle' : 456})

# 2
def alle_anzeigen():
    dict_anzeigen(eintraege)

# Test: alle_anzeigen()

# 3
def befehle_anzeigen():
    n = 0
    for key in befehle.keys():
        print(n, ':', befehle.get(key))
        n += 1

# Test: befehle_anzeigen()

# 4a
'''
def start():
    while True:
        eingabe = input('TB> ')
        if eingabe == 'h':
            befehle_anzeigen()
        elif eingabe == 'q':
            quit()
'''

# 4b
def start():
    befehlsliste = list(befehle.keys())    # Schlüsse aus dict befehle in liste speichern
    while True:
        eingabe = input('TB> ')            # Eingabe lesen
        if eingabe == 'h':                 # Eingabe mit h vergleichen
            befehle_anzeigen()                       # Befehl ausführen falls gleich
        elif eingabe == 'q':
            quit()
        else:                              # 
            try:
                nummer = int(eingabe)                # Eingabe in int umwandeln
                eval(befehlsliste[nummer] + '()')    # Funktionsname aus Liste bekommen und ausführen
            except:
                print('ungültige Eingabe.')

# 5
def lies_eingabe(prompt):
    eingabe = ''
    while len(eingabe) == 0:
        eingabe = input(prompt)
    return eingabe

# 6
def eintrag_hinzufuegen():
    name = lies_eingabe('Name: ')
    nummer = lies_eingabe('Nummer: ')	
    eintraege.update({name : nummer})

#7
def name_suchen(name):
    treffer = {}
    for key in eintraege.keys():
        if key.startswith(name):
            treffer.update({key : eintraege.get(key)})
    return treffer

# tr = name_suchen('Jo')
# dict_anzeigen(tr)

# 8
def eintrag_suchen():
    name = lies_eingabe('Name: ')
    treffer = name_suchen(name)
    if len(treffer) == 0:
	    print('Es wurde kein passender Eintrag gefunden')
    dict_anzeigen(treffer)


def eintrag_entfernen():
    print('in Eintrag entfernen')
    such_string = lies_eingabe("Bitte geben Sie den Namen ein: ")
    treffer = []
    for name in eintraege.keys():
        if name.startswith(such_string):
            treffer.append(name)
    if len(treffer) == 0:
        print('Kein passender Treffer gefunden')
    elif len(treffer) == 1:		# genau ein Treffer
        print('Eintrag', treffer[0], 'wurde entfernt')
        eintraege.pop(treffer[0])
    else:						# mehrere Treffer
        n = 0
        for name in treffer:
            print(n, ':', name)
            n += 1
        auswahl = lies_eingabe('Geben Sie die Nummer des zu löschenden Eintrags an: ')
        try:
            nummer = int(auswahl)
            print('Eintrag', treffer[nummer], 'wurde entfernt')
            eintraege.pop(treffer[nummer])
        except:
            print('ungültige Eingabe!')

# 10
def nummer_suchen(nummer):
    treffer = {}
    for key in eintraege.keys():
        value = str(eintraege.get(key))
        if value.startswith(nummer):
            treffer.update({key : value})
    return treffer


def inverse_suche():
    treffer = nummer_suchen(lies_eingabe('Bitte Nummer eingeben: '))
    dict_anzeigen(treffer)


def buttcall():
    values = list(eintraege.values())
    random.shuffle(values)
    print(values[0])


start()
        




