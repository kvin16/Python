my_list=list(("Kevin", "Gysela", "Wey")) #1ra opcion para crear lista
my_other_list = [ 25, 24 , 19, 'coco', 'lia', 'Estrella', 1.77] #2da opcion para crear lista

print(my_list)
print(my_other_list)
print(len(my_other_list))#tamaño de la lista
print(my_other_list[3])#trae el dato en la posicion indicada de la lista
print(my_other_list[-2])#trae el dato en la posicion indicada de la lista al reverso
print(my_list + my_other_list)

my_list.append("william")#añade otro campo a la lista
print(my_list)
my_list.insert(1,"Doris")#inserta un campo a la lista, en la posicion indicada
print(my_list)
my_list.remove("Doris")#elimina un campo de la lista
print(my_list)
my_list[2] = "Pampis"#Cambia el dato en la posicionindicada
print(my_list)