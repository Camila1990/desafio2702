
p= int(input("Ingrese el precio de subs: "))
u= int(input("Ingrese la cantidad de usuarios: "))
up= int(input("Ingrese la cantidad de usuarios premium: "))
gt= int(input("Ingrese el gasto total: "))

preciopremium = 1.5 * p 

up = up * preciopremium

utilidades = p * u + up- gt

print(f"Las utilidades del proyecto son {utilidades}")