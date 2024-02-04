# Definieren einer Klasse namens Robot.
# Eine Klasse ist eine Vorlage für das Erstellen von Objekten mit ähnlichen Eigenschaften und Verhalten.
class Robot:
    
    # Der Konstruktor __init__ wird aufgerufen, wenn ein neues Objekt der Klasse erstellt wird.
    # Er initialisiert die Objekteigenschaften mit den übergebenen Werten.
    def __init__(self, name, use, company, is_working, points):   
        # self repräsentiert das jeweilige Objekt, das gerade erstellt wird.
        # Hier weisen wir den übergebenen Werten den Eigenschaften des Objekts zu.
        self.name = name  # Name des RobotersS
        self.use = use  # Verwendungszweck des Roboters
        self.company = company  # Unternehmen, das den Roboter besitzt oder hergestellt hat
        self.is_working = is_working  # Gibt an, ob der Roboter funktionstüchtig ist (True oder False)
        self.points = points  # Bewertung des Roboters auf einer Skala
        
    # Eine Methode namens awesome, die prüft, ob der Roboter eine hohe Bewertung hat.
    # Methoden sind Funktionen, die zu einer Klasse gehören und das Verhalten der Objekte bestimmen.
    def awesome(self):
        # Die if-Anweisung prüft, ob die Punktzahl des Roboters 9 oder höher ist.
        if self.points >= 4:
            return True  # Wenn die Punktzahl 9 oder höher ist, ist der Roboter "awesome" (großartig).
        else:
            return False  # Wenn die Punktzahl unter 9 ist, ist der Roboter nicht "awesome".
