import json

# Das Telefonbuch selbst verwendet für die zu verwaltenden Einträge nun kein Dictionary mehr, sondern ein Objekt der Klasse json_dict
# Da wir im bereits geschriebenen Code ein Dictionary für die Verwaltung der Einträge verwenden ist diese Klasse eine Kindklasse von dict, sodass wir alle dict-Methoden verwenden können, ohne dass der komplette Code umgeschrieben werden muss. 
# Hier werden nur die Methoden überschrieben welche das Telefonbuch verwendet. Bei bedarf müssen weitere hinzugefügt werden

class json_dict(dict): # Kindklasse von dictionary

    def __init__(self, pfad, *args):
        super().__init__(args) # Constructor der Superklasse aufrufen
        self.file = open(pfad, "r+") # Datei öffnen (Lese- und Schreibzugriff; somit kann kein anderer die Datei verändern, währen das Programm läuft)

        try: # JSON laden und die Methode update der Superklasse aufrufen, damit die Einträge im Dictionary landen
            json_data = json.load(self.file)
            super().update(json_data)
        except: raise Exception("JSON konnte nicht geladen werden")

    def update(self, data):
        super().update(data) # Aufruf der Methode update der Superklasse dict
        self.__onupdate()

    def pop(self, object):
        super().pop(object)
        self.__onupdate()


    # __onupdate wird immer nach dem Verändern des dicts aufgerufen
    def __onupdate(self):
        self.file.seek(0) # Zum Anfang der Datei springen
        json.dump(self, self.file)
        self.file.truncate()