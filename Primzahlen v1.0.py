# Version 1.0:
# Testen auf ganzahlige Teilung und Zählung derselben
# Ermitteln von Primzahlen, wenn nur zwei ganzahlige Teilungen
# Ausgabe der Primzahlen

print("\n----- Version 1.0: -----")
var1 = 1         # Start-Variable 1 für die Zahl, die schrittweise um eines größer werden soll
var2 = 2         # Variable 2 ist für die Range der for-Schleife, die immer um eines größer sein muß, als die eigentliche Zahl
prim1 = 0        # Schleifenzähler, mit dem geprüft wird, ob eine Zahl öfter als zweimal durch irgendwas geteilt werden kann
rg = 100         # Der Zahlenraum, aus denen man die Primzahlen zu ermitteln sucht

while var1 < rg:     # Variable 1 muss erstmal kleiner als der Zahlenraum sein
    var1 += 1        # Variable 1 wird um 1 erhöht und startet somit mit der 2 als erste Primzahl
    var2 += 1        # Variable 2 wird ebenfalls um 1 erhöht, um so für die Range immer um 1 höher als die Zahl zu bleiben (exklusiver Endwert der Range)
    for i in range(1, var2):  # hier wird Variable 2 als Endwert für die Range benutzt, damit die Zahl in Variable 1 in genauso vielen Schritten geteilt wird
        if var1 % i == 0:     # Variable 1 wird überprüft, ob eine Zahl ganzzahlig hineinpasst
            prim1 += 1        # der Zähler wird dann erhöht
        else:
            prim1 += 0        # ansonsten bleibt der Zähler unverändert
    if prim1 < 3:             # nach der "Ganzzahl-Test"-Schleife wird der Zähler überprüft
        print(var1, ", ", sep="", end="")  # konnte eine Zahl nur zweimal geteilt werden (nämlich durch 1 und durch sich selbst), wird sie ausgegeben
    else:
        print("", sep="", end="")          # ansonsten erfolgt keine Ausgabe
    prim1 = 0                              # abschließend wird der Zähler zurückgesetzt, damit die nächstgrößere Zahl im Zahlenraum überprüft werden kann
print("\n--- Ende der Überprüfung ---")
