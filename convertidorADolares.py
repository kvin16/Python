
chino= "🇨🇳 yuan chino"
japones="🇯🇵 yen japonés"
core="🇰🇷 Ganó surcoreano"
a = int(input("Cuanto dinero tiene de " + chino + " "))
b = int(input("Cuanto dinero tiene de " + japones + " "))
c = int(input("Cuanto dinero tiene de " + core + " "))

print("usted tiene ", a, " Yuan chinos") #Cuando se quiera indicar diferentes tipos de variables en un solo print

yen = a * 0.14832083
jap = b * 0.0077689502
won = c * 0.00081494719

f1 = "Usted tiene " + str(yen) + " dolares en Yuanes"
f2 = "Usted tiene " + str(jap) + " dolares en Yenes"
f3 = "Usted tiene " + str(won) + " dolares en Wones"
print(f1)
print(f2)
print(f3)
total = yen + jap + won
f4 = "Usted tiene " + str(total) + " Dolares en total"
print(f4)


print("usted tieen ", a, " Yuan chinos")
