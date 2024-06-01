#Variables e impresiones

name, surname, alias, age = "kevin", "cardenas", "kvin", 25
print ("Me llamo: " , name, surname, " Y mi apodo es ", alias, ", Actualmente tengo: ", age)

#Strings
print ("Este string \n tiene salto de linea")
print ("\t Este string tiene salto de linea")
print ("Me llamo: %s %s, y mi apodo es %s, Actualmente tengo: %d" %(name, surname, alias, age))#Mejor forma de trabajar

#Operadores

print(10 % 3) # El residuo de una division
print(10 // 3) #Una division aproximada 
print(2 ** 3) #Exponencial (Elevado al  ...)
print("Kvin " * (3)) #Multiplica 3 veces la palabra
print(10 <= 3 and "Hola" == "Hola") #falso y verdadero
print(10 <= 3 or "Hola" == "Hola") #falso y verdadero
print(not(3<4))#Cambia el resultado

