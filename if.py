print("HOla Pipe") 

titulo="Clima de hoy"  #string
diaDelMes=17
mes=4       #int
tem=25.7  #float
llueve=True  #boolean
print(titulo, "temperatura:", tem,diaDelMes,"/",mes) 
print(f"{titulo} temperatura: {tem} {diaDelMes}/{mes}")

# tem>28 ---->False
# mes==4---->True

if llueve:
    print("Saca el paraguas")
else:
    print("Puede andar en polera")
