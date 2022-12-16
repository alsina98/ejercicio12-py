cantidad = int(input("Por favor pon el numero de paises que deseas agrgar a la lista"))
paises = []

i = 0
while i < cantidad:
    if cantidad > 1:
        pais = input(f"Escribe {cantidad} paises:")
        paises.append(pais)
    else:
        pais = input(f"Escribe {cantidad} pais:")
        paises.append(pais)
    i += 1

thisset = set(paises)


print(sorted(thisset))

# Ejemplo

# Por favor pon el numero de paises que deseas agrgar a la lista [5]

# Escribe 5 paises:Greece 
# Escribe 5 paises:France
# Escribe 5 paises:Spain <-
# Escribe 5 paises:Germany
# Escribe 5 paises:Spain <-

# ['France', 'Germany', 'Greece', 'Spain']