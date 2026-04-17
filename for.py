# explicacion y uso de for

# for i in range(7): }
#     print("hola")

# num=int(input("Ingrese un numero: "))

# for i in range(num):
#     print(i+1,"repeticion")
# print("segunda forma")
# for i in range(1,num+1):
#     print(i,"repeticion")


# Pedir un numero al usuario y 
# mostrar su tabla de multiplicar

# num=int(input("Ingrese un numero: "))
# # primera forma
# for i in range(10):
#     print(num, "x", i+1, "=",num*(i+1) )
#     print(f"{num}x{i+1}={num*(i+1)}")
# # con manipulacion de limites en range
# for i in range(1,11):
#     print(num, "x", i, "=",num*i )

# Preguntar cuantas notas son
# y sacar el promedio de ellas

# nme=4.567657
# print(round(nme,2))

# num=int(input("Cuantas notas son?: "))
# suma=0
# for i in range(num):
#     n=float(input("Ingrese la nota: "))
#     suma=suma+n
# prom = suma/num
# print(f"El prmedio es {prom}")

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")

# # sumatoria

# num=int(input("Ingrese un numero: "))
# total=0
# for i in range(num):
#     total=total+i+1
# print("LA sumatoria es: ", total)  # 1+2+3=6   4// 1+2+3+4=10


# # factorial

# num=int(input("Ingrese un numero: "))
# total=1
# for i in range(num):
#     total=total*(i+1)
# print("La sumatoria es: ", total) 


## Contador de vocales y consonantes
# vocales=0
# conso=0
# nombre=input("Ingrese su nombre: ")
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU":
#         # vocales=vocales+1
#         vocales+=1
#     elif i ==" ":
#         ''''''
#     else:
#         conso+=1
# print(f"El total de vocales es {vocales}")
# print(f"El total de consonantes es {conso}")
