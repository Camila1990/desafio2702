
p= int(input("Ingrese el precio de subs: "))
u= int(input("Ingrese la cantidad de usuarios: "))
gt= int(input("Ingrese el gasto total: "))
utilidades_anteriores = int(input("Utilidades anteriores: "))

utilidades = p * u - gt
razon = utilidades_anteriores/utilidades

print(f"La razón de las utilidades del proyecto son {razon:.2f}")