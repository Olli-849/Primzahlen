# Testbereich:
# Zahl schrittweise durch ganzzahlige Zahlen-Anteile geteilt:
# 5 wird also durch 1, 2, 3, 4 und 5 geteilt

print("\n----- Testbereich - Version 0.5:-----")
var1 = 1    # die zu teilende Zahl
var2 = 2    # Endwert der Range um eines höher als var1 (Endwert der Range ist exklusiv)
rg = 5      # Zahlenraum und damit der Maximalwert der zu teilenden Zahl

while var1 < rg:
    var1 += 1
    var2 += 1
    print("\nZahl ", var1, ": ", sep="")      # die var1 als Zahl, die es zu teilen gilt
    for i in range(1, var2):                    # var2 als Endwert der Range (stets um 1 größer als die Zahl in var1)
        # print("/", i, " = ", sep="", end="")    # testweise Ausgabe von i als Teiler
        print(var1 / i, "  ", sep="",end="")    # i als Teiler
print()

